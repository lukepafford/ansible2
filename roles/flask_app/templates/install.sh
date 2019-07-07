#!/bin/bash
conda env update -f environment.yml --json --quiet --verbose 2>&1 | grep 'LINKING PACKAGE'

if [[ "$?" -eq 0 ]]; then
  echo "flask_app was updated. Now restarting flask_app"
	systemctl restart flask_app
fi 
