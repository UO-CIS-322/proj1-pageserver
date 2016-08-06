"""
Configuration of pageserver.py.

We "factor out" configuration-specific values from
pageserver.py and keep them in a configuration file
like this.  CONFIG.base.py is under configuration control;
on each installation (e.g., on the development machine and
on the deployment machine) it must be edited and saved
as CONFIG.py.

Fall 2016: Keeping some standard target configurations in
targets.d, and selecting one with ./configure
(see lecture notes on dependence management for rationale)

"""

#
# We will 'listen' for HTTP requests on a particular network
# port.  Ports have integer numbers between 0 and 65535, but
# the ports we can use are between 1024 and 49151.  Some ports
# may already be in use for something else, but a random integer
# between 5000 and 8000 has a pretty good chance of being avaiable.
#
PORT = 8000  # A common "non-privileged" stand-in for privileged port 80

