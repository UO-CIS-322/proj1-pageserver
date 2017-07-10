# Makefile for simple page server. 
#

# Define lists of files we need
CONFIGURATION = config/host.ini

# 'make run' will run our program
# 
run:	$(CONFIGURATION) pageserver.py 
	python3 pageserver.py || true
	## The "or true" tells Make not to complain about ending the 
	## program with control-C

# 'make configure' will run the configuration script, 
# but only if config/host.ini doesn't already exist. 
# 
configure: $(CONFIGURATION)  

$(CONFIGURATION):
	bash ./configure
	echo "Configuration complete"

# 'clean' and 'veryclean' are typically used before checking 
# things into git.  'clean' should leave the project ready to 
# run, while 'veryclean' may leave project in a state that 
# requires re-running installation and configuration steps
# 
clean:
	rm -f *.pyc
	rm -rf __pycache__

veryclean:
	make clean
	rm -f config/host.ini

