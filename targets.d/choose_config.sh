#! /bin/bash
# 
# choose a configuration file:  
#     We install one of the CONFIG_machine.py files as ../CONFIG.py 
#     selecting by known host names (e.g., ix), architecture names
#     (e.g., armv7 or armv8 for pi), operating system (darwin for MacOSX). 
#     The default is chosen if none of the known architectures matches. 
# 
# This scheme was chosen partly to make grading easier. 
# See lecture notes on dependence management for a rationale, including 
# some drawbacks of this approach.  
# 

# What machine is this?  Use uname to find hardware
# 
architecture=`uname -m`
node=`uname -n`
processor=`uname -p`
opsys=`uname -v`

if [[ $architecture =~ "arm" ]]; then
   echo "Configuring for Raspberry Pi versions 2 or 3"
   cp CONFIG_pi.py ../CONFIG.py
elif [[ $opsys =~ "Darwin" ]]; then 
   echo "Configuring for Mac OS X"
   cp CONFIG_macosx.py ../CONFIG.py
elif [[ $node =~ "ix" ]]; then 
   echo "Configuring for CIS host ix-trusty or ix-dev"
   cp CONFIG_ix.py ../CONFIG.py
   echo "You must editing CONFIG.py to use a different port"
else
   echo "Unknown host type; using default configuration file"
   echo "Edit CONFIG.py to set appropriate port"
   cp CONFIG.skel.py ../CONFIG.py
fi;




