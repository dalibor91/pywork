#!/bin/bash

version=$(python -c 'import platform; print(platform.python_version())')

if ! [ "$1" = "" ];
then 
	echo -e "Current version: ${version}\nProject version: `cat $1`"
else
	echo $version
fi

