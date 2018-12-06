Installs docker-ce and ensures docker service is running

variables:
  - 'docker_ce_admins': { type: 'list', default: [], description: 'List
      of users to be appended to the "docker" group' }
