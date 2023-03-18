# Pull recent changes from GitHub repository to make them available
# in the present Binder session. Transferred data are public,
# hence performing this operation brings no privacy issues.
if [ -n "$1" ]
then
    git checkout -b "$1" origin/"$1"
else
    git pull
fi
