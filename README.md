# ansible2
New repository for my Ansible roles

# Repository Conventions
 This document follows patterns from the [Ansible best practices document](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html) and [This great post by Michel Blanc](https://leucos.github.io/ansible-files-layout)

## Pending documented processes
 * Dealing with conflicting, and legacy roles
 * Properly documenting applications that can't be managed through ansible
 
   (e.g Java applications that are configured through the web interface)
   
## Variables
  * Site wide variables (domain, realm) should all exist in `group_vars/all`
  
  * Unique variables (ip address) should exist in `host_vars`
  
  * Role variables should be defined by groups in `group_vars/group`
  
  See the 'Secrets' section for how to handle encrypted values
  
## Playbooks
  * Playbooks will have the following directory structure
  ```
  playbook-proj1/
    ansible.cfg
    inventories/
      development/
        group_vars/
          all
        group01/
          vars
          vault
       production/
         group_vars/
           all
         group02/
           vars
           vault
     site.yml
     playbooks/
       base.yml
       database.yml
       reverse_proxy.yml
       webserver.yml
       ...
 ```
 
 ## Roles
   * Roles should have a standard directory structure
   ```
   role-name/
     defaults/
       main.yml
     files/
     handlers/
       main.yml
     tasks/
       main.yml
     meta/
       main.yml
     templates/
   ```
   
   * All roles must have a README.md. Go into detail of what the role does if it isn't obvious
   
   * **ALL_VARIABLES** used in the role must be defined in `defaults/main.yml`.
   
     This is the most **critical** step for role consistency
     
   * variables must use pseudo-namespacing for their naming convention (E.G if the
     role name is "postgresql" and the variable is "port" then the real variable
     name must be "postgresql_port"
   ```
   # postgresql/defaults/main.yml
   ---
   postgresql_port = 5432
   postgresql_server = db01
   postgresql_user = user01
   ```
   
   * Tasks must contain a `tasks/main.yml` that **only** imports other tasks.
   
     This is where we will add tags so they inherit throughout the role
   ```
   ---
   - import_tasks: postgresql.yml
     tags:
       - postgresql
   ```
   
## Secrets
  Read the section on 'Variables and Vaults' at 
  
  https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html#best-practices-for-variables-and-vaults
  
  I will be following this practice verbatim
  
## gitignore
 The following files should be ignored because they contain local 
 
 configurations that won't work for anyone else.
 
 * ansible.cfg
 
## Host Lifecycle
  Steps to perform when adding or removing a host
  
### Host creation
 Add the host to the Ansible inventory, and appropriate `host_vars` and `group_vars`
 
#### Linux Hosts
  * Specify the bootproto variable
  * If bootproto is static then:
    - Set the ipv4 variable
    - Ensure the host has a DNS entry

## Tips
  * If you use a lot of tags to limit what your playbook runs, then you will want to have the config setting

    ```gathering = smart```
  
    or set the ansible environment variable **ANSIBLE_GATHERING**
  
    your choices are [ 'smart', 'explicit', 'implicit'] (default: implicit)

    This is so facts aren't gathered for each and every play, and it wastes a lot of time

    if you just want to run a small fraction of your playbook

# WARNING
 I run Centos7 on all my servers, and my roles reflect this for simplicity.
Running a different OS likely means you'll run into problems. ex - The repos role
pulls down the "el7" repos for Enterprise Linux

# ABOUT
I've gotten better with Ansible, and scripting, and wanted to redo a lot of functionality. A lot of previous roles didn't consistently abstract the data through templates, making them pretty useless.
Rather then fix my git repo (lukepafford-ansible), I'm just pushing everything to this new one. 

Feel free to use any roles in here if they look like something you need. I'm going to try and make sure each role has a *readme* specifying what variables need to be provided

# CODEBASE
Custom scripts used in roles will primarily consist of Bash, Python, and NodeJS
