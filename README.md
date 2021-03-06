# *vhosts*
An unimaginatively named command line utility for managing Apache vhosts on Mac OS X.
## vhosts manages vhosts

When developing for the web locally, you probably find yourself loading up files from really long file paths in the browser. The typing of these takes time, looks ugly and only works for static sites.

If you want to work with dynamic sites in languages such as PHP, you have to mess around with apache configuration files, add vhosts and whatnot. It's boring and tedious.

The aim of vhosts is to do it all for you.

*__vhosts lets you easily create and manage Apache VirtualHosts__*

## Usage
The four basic commands are `add`, `remove`, `edit` and `list`.

Currently, `add` is the only option.

	$ vhosts add path/to/directory/

By default, the server name will be set to the name of the folder provided.  
i.e. `~/Sites/app` would be accessible at `app.dev` in the browser.

You can optionally pass an additional argument to specify the desired hostname.

	$ vhosts add path/to/directory/ --name webapp.local
This would now be accessible at `webapp.local` in the browser
