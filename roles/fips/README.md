fips
=======

Configures fips on the system. The system will need to be rebooted to take effect.

Warnings
============
* This role relies on the "ANSIBLE_MOUNTS" fact to determine the UUID of the boot partition
* This can be potentially destructive to your system, and cause booting issues. You should absolutely test FIPS changes on a system you don't care about first.
* The role was created for and tested on RedHat 7. The hard requirements are having grub2 intalled, and having the dracut-fips, and dracut-fips-aesni packages available to you.
 
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
