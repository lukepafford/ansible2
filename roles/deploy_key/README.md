deploy_key
=========

deploy_key

Requirements
------------

Role Variables
--------------
```
variables:
	- name: deploy_key_account
		type: str
		required: no
		default: git.svc
		description: Account that contain the private key used to authenticate with
		Github deploy key

	- name: deploy_key_owner
		type: str
		required: yes
		default: 
		description: Owner of the Github repository

	- name: deploy_key_name
		type: str
		required: yes
		default:
		description: Name of the deploy key
	
	- name: deploy_key_token
		type: str
		required: yes
		default: 
		description: API key used to authenticate to the repo

	- name: deploy_key_repository
		type: str
		required: yes
		default: 
		description: repository name to deploy key to
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
