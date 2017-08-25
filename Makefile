# Makefile for simple page server. 
#

# Nothing to install for this project. There will be more
# starting from project 2.
install:
	echo "Nothing to install"

# 'make run' will run our program, provided we
# already have the $(CONFIGURATION) files.  If $(CONFIGURATION)
# does not already exist, it will be built.
# The "or true" tells 'make' not to complain about shutting down with Ctrl-C
# 
run:	pageserver/pageserver.py 
	python3 pageserver/pageserver.py & echo $$! >,pypid
	echo "----> Kill with: kill: " `cat ,pypid`

kill:	,pypid
	kill `cat ,pypid`

# 'clean' and 'veryclean' are typically used before checking 
# things into git.  'clean' should leave the project ready to 
# run, while 'veryclean' may leave project in a state that 
# requires re-running installation and configuration steps. 
# 
clean:
	rm -f *.pyc
	rm -rf __pycache__

veryclean:
	make clean
	rm -f pageserver/credentials.ini

