custom_webhooks
=========

Deploys custom flask app for receiving events from Github

Requirements
------------

Role Variables
--------------
```
variables:
	- name: custom_webhooks_installDir
		type: directory
		required: yes
		default:
		description: Directory to install app into

	- name: custom_webhooks_secret
		type: file
		required: yes
		default:
		description: Secret to verify notification s come from Github webhooks

	- name: custom_webhooks_pipelineScript
		type: file
		required: yes
		default:
		description: path to script that will run our pipeline. This must
								 be configured on its own

	- name: custom_webhooks_user
		type: user
		required: yes
		default:
		description: User to run the app

	- name: custom_webhooks_port
		type: int
		required: yes
		default:
		description: Port to run the custom_webhook app on

	- name: custom_webhooks_condaEnvironment
		type: str
		required: yes
		default:
		description: Name of Anaconda environment
```
Dependencies
------------
anaconda Role

License
-------

BSD

Author Information
------------------
Name: Luke Pafford 
Email: lukepafford@gmail.com
