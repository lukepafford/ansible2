#!/bin/bash

if [[ "$#" -eq 0 ]]; then
	echo "$0: dir"
	exit 1
fi

find "$1" -not -regex ".*node_modules.*" -print0 | while read -r -d $'\0' _file; do
	
	oldName="${_file}"

	if echo $(basename "${oldName}") | grep -q '-'; then
		newName=$(echo ${oldName} | sed -e 's/-/_/g')
		git mv "${oldName}" "${newName}"
	fi
done
