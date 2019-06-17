anaconda_app
=========

Performs shared tasks involved in installing all anaconda apps such as
creating the environment, installing packages, creating the user, etc

Requirements
------------

Role Variables
--------------
```
variables:
	- name: anaconda_app_user
		type: str
		required: yes
		default:
		description: name of the user who will be created to run the app

	- name: anaconda_app_installDir
		type: directory
		required: yes
		default:
		description: Directory to install everything

	- name: anaconda_app_condaEnvironment
		type: str
		required: yes
		default:
		description: Name of the environment to create

	- name: anaconda_app_dependencies
		type: list
		required: yes
		default:
		description: List of packages to be installed into the environment

	- name: anaconda_app_condaHome
		type: str
		required: yes
		default:
		description: Path to the installation of anaconda

	- name: anaconda_app_dependencies
		type: list
		required: yes
		default:
		description: List of packages to be installed into the environment
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
