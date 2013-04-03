#! /usr/bin/python
import os
import argparse
from subprocess import check_output


def ask_to_proceed(message):
		response = raw_input(message + ' (y/n): ').lower()[0]
		if response == 'n':
			exit()
		elif response != 'y':
			print 'Invalid Response'
			ask_to_proceed()


def vhost_data(doc_root, server_name):
	return """
<VirtualHost *:80>
   DocumentRoot "{0}"
   ServerName {1}
</VirtualHost>""".format(doc_root, server_name)


def add_to_vhosts(path, server_name):
	create_vhost = """sudo sh <<EOF
echo '{0}' >> /private/etc/apache2/extra/httpd-vhosts.conf
EOF""".format(vhost_data(path, server_name))

	os.system(create_vhost)


def add_to_hosts(server_name):
	add_host = """sudo sh <<EOF
echo '127.0.0.1 {0}' >> /private/etc/hosts
EOF""".format(server_name)

	os.system(add_host)


def set_vhost(path, server_name):
	path = os.path.abspath(path)
	if server_name == '':
		server_name = check_output(['basename', path])[:-1].lower() + '.dev'

	if not os.path.isfile(path + '/index.php') and not os.path.isfile(path + '/index.html'):
		ask_to_proceed('!!! No index file exists. Continue anyway?')

	add_to_vhosts(path, server_name)
	add_to_hosts(server_name)

	ask_to_proceed('Restart apache?')
	os.system('sudo apachectl restart')


class Params(object):
	pass

params = Params()

parser = argparse.ArgumentParser(description='Creates an apache vhost pointing to the specified directory')
parser.add_argument('path', type=str, help='Path to the desired document root')
parser.add_argument('--name', action='store', dest='server_name', help='specify desired server name (defaults to foldername.dev)', default='')
parser.parse_args(namespace=params)

set_vhost(params.path, params.server_name)
