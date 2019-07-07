#!/bin/bash
echo "Checking for flask_app update..."
/var/anaconda/bin/conda env update -f {{ flask_app_installDir }}/environment.yml --json --quiet --verbose 2>&1 | grep 'LINKING PACKAGE'

if [[ "$?" -eq 0 ]]; then
  echo "flask_app was updated. Now restarting flask_app"
	systemctl restart flask_app
else
  echo "No version update was detected"
fi
