# Makefile for simple page server. 
#
# Define lists of files we need
CONFIGURATION = config/host.ini

# 'make configure' triggers a build of the
# phony target 'configure', which builds 
# the $(CONFIGURATION) file(s) if needed. We
# record the dependency, but no separate action. 
# 
configure: $(CONFIGURATION)  

# The configuration action is performed for any command that
# depends on host.ini (or anything in $(CONFIGURATON)). 
#
$(CONFIGURATION):
	bash ./configure
	echo "Configuration complete"

# 'make run' will run our program, provided we
# already have the $(CONFIGURATION) files.  If $(CONFIGURATION)
# does not already exist, it will be built.
# The "or true" tells 'make' not to complain about shutting down with Ctrl-C
# 
run:	$(CONFIGURATION) pageserver.py 
	python3 pageserver.py || true 


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
	rm -f config/host.ini

