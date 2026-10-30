#!/bin/bash

set -e

UID=${UID:-""}
GID=${GID:-""}
USER=${USER:-""}

if [ -z "$USER" ]; then
    echo "USER env is required by --env USER=\$USER"
    exit 1
fi

if [ -z "$UID" ]; then
    echo "UID env is required by --env UID=\`id -u\`"
    exit 1
fi

if [ -z "$GID" ]; then
    echo "GID env is required by --env GID=\`id -g\`"
    exit 1
fi

# if group $USER not exists, add group
if ! grep -q "^$USER:" /etc/group; then
    addgroup --gid "$GID" "$USER"
fi

# if user $UID not exists, add user
if ! grep -q "^$USER:" /etc/passwd; then
    adduser --gecos "" --uid "$UID" --gid "$GID" --no-create-home --disabled-password "$USER"
    mkdir -p /home/"$USER"
    cp -r /etc/skel/. /home/"$USER"
    # default password is maixcdk
    echo "$USER:maixcdk" | chpasswd
    usermod -aG sudo "$USER"
fi
chown "$UID":"$GID" /home/"$USER"

# add /maixapp directory and chown to $USER
mkdir -p /maixapp
chown "$UID":"$GID" /maixapp

echo "###########################################################"
echo "##"
echo "##  ███    ███  █████  ██ ██   ██  ██████ ██████  ██   ██"
echo "##  ████  ████ ██   ██ ██  ██ ██  ██      ██   ██ ██  ██"
echo "##  ██ ████ ██ ███████ ██   ███   ██      ██   ██ █████"
echo "##  ██  ██  ██ ██   ██ ██  ██ ██  ██      ██   ██ ██  ██"
echo "##  ██      ██ ██   ██ ██ ██   ██  ██████ ██████  ██   ██"
echo "##"
echo "##  ${USER}! Welcome to MaixCDK Docker Container!"
echo "###########################################################"
echo "##"

# if $MAIXCDK_PATH exists and is a directory and is not empty
if [ -n "$MAIXCDK_PATH" ] && [ -d "$MAIXCDK_PATH" ] ; then
    echo "## MAIXCDK_PATH is set to '$MAIXCDK_PATH'"
else
    echo "## MAIXCDK_PATH is not set or ${MAIXCDK_PATH} not exists"
    echo "## Please set MAIXCDK_PATH to MaixCDK path in container"
    echo "## e.g. add args \`--env MAIXCDK_PATH=/path/to/MaixCDK -v /path/to/MaixCDK:/path/to/MaixCDK\` to docker run command"
fi
echo "## The default password of user ${USER} is 'maixcdk'"
echo "###########################################################"
echo ""

cd /home/"$USER"

su "$USER"


