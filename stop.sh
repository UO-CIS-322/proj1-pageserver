#! /bin/bash
# 
# Stop server started with start.sh
# (Run from same directory as start.sh so that 
#  path to ,pid is the same)
#
pid=`cat ,pid`
kill ${pid}
echo "${pid} should be dead now"
