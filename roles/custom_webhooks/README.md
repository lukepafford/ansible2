custom_webhooks
=========

Deploys custom flask app for receiving events from Github

WARNING. Despite requiring `redis` as a dependency for anaconda,
Python was still not able to find the library. The automation appeared
to work, the conda environment showed that redis was installed. Despite this,
no `redis` module could be found. I had to use `pip install redis` to get it to 
see this. I should not have had to use pip to install the library when I had anaconda,
but I did. Find out why this was.

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

	- name: custom_webhooks_celeryPath
		type: directory
		required: yes
		default:
		description: Path containing celery module. The celery app
								 should really be packaged and installed so we can
								 just import it! (NEEDS WORK)

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
