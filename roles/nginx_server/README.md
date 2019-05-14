nginx_server
=========

nginx_server

Assumes you have created a TLS certificate with LetsEncrypt using the certbot utility and provided the hosts domain name

Requirements
------------

Role Variables
--------------
```
variables:
	- name: nginx_server_rootDir
		type: directory
		required: no
		default: /var/www/html
		description: Root directory where content will be served

	- name: nginx_server_cachePath
		type: directory
		required: yes
		default: 
		description: Path to cache Nginx content
```
Dependencies
------------

License
-------

BSD

Author Information
------------------
Name: Luke Pafford 
Email: lukepafford@gmail.com
