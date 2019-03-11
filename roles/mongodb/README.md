mongodb
=========

mongodb

Requirements
------------

Role Variables
--------------
```
variables:
	- name: mongdb_sclVersion
		type: string
		required: no
		default: rh-mongo36
		description: Which software version of mongodb to install

	- name: mongdb_port
		type: int
		required: no
		default: 27017
		description: Port the server should listen on

	- name: mongdb_sslTrust
		type: file
		required: no
		default: /etd/pki/tls/cert.pem
		description: Path to the SSL Trust file
								 WARNING: This option is currently not used

	- name: mongdb_sslCert
		type: file
		required: yes
		default: 
		description: Path to the SSL Public Certificate

	- name: mongdb_sslKey
		type: file
		required: yes
		default: 
		description: Path to the SSL Private Key

	- name: mongdb_sslPem
		type: path
		required: yes
		default: 
		description: Path to the concatenated file containing the 
							{{ mongodb_sslCert }} and {{ mongodb_sslPem }}.
							This file will be created
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
