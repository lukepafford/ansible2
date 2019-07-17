fips
=======

Configures fips on the system. The system will need to be rebooted to take effect.

* Warning - this role relis on the "ANSIBLE_MOUNTS" fact to determine the UUID of the boot partition
 
 Role Variables
 ---------------
 ```
 variables:
   - name: fips_enabled
     required: no
     type: bool
     default: True
     description: Boolean to determine whether fips should be enabled or disabled on the system
```
