nexus3
=========

nexus3

Role Variables
--------------
```
variables:
	- name: nexus3_downloadUrl
		type: url
		required: no
		default: https://download.sonatype.com/nexus/3/latest-unix.tar.gz
		description: Remote url to download the nexus3 software

	- name: nexus3_downloadChecksum
		type: str
		required: no
		default: sha256:ae8cc7891942d71cf12c11e1a98d70c1310e788ab44aa95c5d1e7671cc0187e2
		description: Checksum of the url. The checksum must be in ansible format ( <algorithm:checksum> )

	- name: nexus3_downloadDir
		type: directory
		required: no
		default: /opt
		description: Directory to download the nexus3 tarball

	- name: nexus3_installDir
		type: directory
		required: no
		default: /opt/nexus
		description: Directory to install nexus3

	- name: nexus3_port
		type: int
		required: no
		default: 8081
		description: TCP port for the application to listen on
```

License
-------

BSD

Author Information
------------------
Name: Luke Pafford 
Email: lukepafford@gmail.com
