Installs docker-ce and ensures docker service is running

variables:
  - name: docker_ce_admins
    required: no
    type: list
    default: []
    description: List of users to be appended to the "docker" group
