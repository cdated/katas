#!/usr/bin/env sh

echo "Cleaning env"
rm -rf .tox venv *.egg-info

FROM=kata
TO=example

echo "Renaming file and directories"
find . -exec rename -s $FROM $TO {} \;

echo "Replacing strings in files"
find . -type f -exec sed -i "s/$FROM/$TO/g" {} \;
