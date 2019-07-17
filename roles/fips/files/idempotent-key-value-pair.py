#!/usr/bin/env python
import sys, re, shutil
import tempfile

if len(sys.argv) < 4:
  print('{0} file matching_key key [value]'.format(sys.argv[0]))
  print("""
  file: Path to file we need to ensure the key value pair exists in.
  matching_key: Regex to match the key of the line we want to insert the key pair into
  key: Name of the key in the key pair
  value (optional): Name of the value in the key pair
  
  This script will ensure that the key value pair idempotently exists
  for a line in a file that contains the following pattern:
  
    key="space seperated list of values"
    
  The script is originally intended to configure /etc/default/grub, but can
  be used for any file that contains this pattern.
  
  If no value is provided, then just the key will be inserted.
  
  Example:
    1. line in /etc/default/grub:
       GRUB_CMDLINE_LINUX="rd.lvm.lv=vg/lv_root rd.lvm.lv=vg/lv_swap rhgb fips=0 quiet"
       
    2. Execute script
       idempotent-key-value-pair.py /etc/default/grub GRUB_CMDLINE_LINUX fips 1
       
    3. Resulting line in /etc/default/grub
       GRUB_CMDLINE_LINUX="rd.lvm.lv=vg/lv_root rd.lvm.lv=vg/lv_swap rhgb fips=1 quiet"
  """)
  sys.exit(1)
  
mod_file = sys.argv[1]
matching_key = sys.argv[2]
key = sys.argv[3]
value = sys.argv[4] if len(sys.argv) == 5 else None

def join_key_value(key, value=None):
  if value:
    pair = '='.join([key, value])
  else:
    pair = key
  return pair
  
# Read lines of file
modified_lines = []
with open(mod_file, 'r') as f:
  for line in f:
    if re.match(matching_key, line):
      _,_,values = line.partition('=')
      # Remove quotes from value list
      settings = re.sub('^\W', '', values)
      settings = re.sub('\W$', '', settings)
      
      # Split values on spaces
      settings = settings.split(' ')
      
      new_values = []
      setting_exists = False
      for setting in settings:
        # If the key is already set, we want to overwrite it
        if re.match(key, setting):
          setting_exists = True
          new_values.append(join_key_value(key, value))
        # No match, add the setting unmodified
        else:
          new_values.append(setting)
      else:
        if not setting_exists:
          # Append key value pair to end of settings
          new_values.append(join_key_value(key, value))
          
      # Set the modified line to match the original format
      modified_line = '{0}="{1}"\n'.format(matching_key, ' '.join(new_values))
      modified_lines.append(modified_line)
    else:
      # Don't modify any other lines
      modified_lines.append(line)
        
# Write modified file to temp file
with tempfile.NamedTemporaryFile(delete=False) as f:
  f.writelines(modified_lines)
  temp = f.name
  
# Replace the original file
shutil.move(temp, mod_file)
