#! /bin/bash
# 
# Guess what machine we are running on.  We generate
# a .ini file "host.ini" that is used to choose values from
# app.ini.  The idea is that we run this once, at installation,
# rather than each time we run the application. 
#
# If this fails, you can create the host.ini file manually
#


# What machine is this?  Use uname to find hardware
# 
architecture=`uname -m`
node=`uname -n`
processor=`uname -p`
opsys=`uname -v`

if [[ $architecture =~ "arm" ]]; then
   echo "Configuring for Raspberry Pi versions 2 or 3"
   target="Pi322"
elif [[ $opsys =~ "Darwin" ]]; then 
   echo "Configuring for Mac OS X, a development machine"
   target="Dev"
elif [[ $node =~ "ix" ]]; then 
   echo "Configuring for CIS host ix-trusty or ix-dev"
   echo "You must editing app.ini for this target"
   target="Ix"
else
   echo "Unknown host type; I'm guessing it's a development machine"
   target="Dev"
fi;
cat >host.ini <<EOF
[DEFAULT]
target=${target}
EOF



