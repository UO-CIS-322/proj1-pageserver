"""
  A trivial web server in Python. 

  Based largely on https://docs.python.org/3.4/howto/sockets.html
  This trivial implementation is not robust:  We have omitted decent
  error handling and many other things to keep the illustration as simple
  as possible. 

  FIXME:
  Currently this program always serves an ascii graphic of a cat.
  Change it to serve files if they end with .html or .css, and are
  located in ./pages  (where '.' is the directory from which this
  program is run).  
"""

import configparser # Read .ini files for configuration
import argparse  # Command line options (may override configuration options)
import logging   # Better than print statements
  # See configuration of logging in get_options

import socket    # Basic TCP/IP communication on the internet
import _thread   # Response computation runs concurrently with main program 

def listen(portnum):
    """
    Create and listen to a server socket.
    Args:
       portnum: Integer in range 1024-65535; temporary use ports
           should be in range 49152-65535.
    Returns:
       A server socket, unless connection fails (e.g., because
       the port is already in use).
    """
    # Internet, streaming socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to port and make accessible from anywhere that has our IP address
    serversocket.bind(('', portnum))
    serversocket.listen(1)    # A real server would have multiple listeners
    return serversocket

def serve(sock, func):
    """
    Respond to connections on sock.
    Args:
       sock:  A server socket, already listening on some port.
       func:  a function that takes a client socket and does something with it
    Returns: nothing
    Effects:
        For each connection, func is called on a client socket connected
        to the connected client, running concurrently in its own thread.
    """
    while True:
        logging.info("Attempting to accept a connection on {}".format(sock))
        (clientsocket, address) = sock.accept()
        _thread.start_new_thread(func, (clientsocket,))


##
## Starter version only serves cat pictures. In fact, only a
## particular cat picture.  This one.
##
CAT = """
     ^ ^
   =(   )=
"""

## HTTP response codes, as the strings we will actually send. 
##   See:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
##   or    http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
## 
STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
STATUS_NOT_IMPLEMENTED = "HTTP/1.0 401 Not Implemented\n\n"

def respond(sock):
    """
    This server responds only to GET requests (not PUT, POST, or UPDATE).
    Any valid GET request is answered with an ascii graphic of a cat. 
    """
    sent = 0
    request = sock.recv(1024)  # We accept only short requests
    request = str(request, encoding='utf-8', errors='strict')
    logging.info("\nRequest was {}\n".format(request))

    parts = request.split()
    if len(parts) > 1 and parts[0] == "GET":
        transmit(STATUS_OK, sock)
        transmit(CAT, sock)
    else:
        logging.info("Unhandled request: {}".format(request))
        transmit(STATUS_NOT_IMPLEMENTED, sock)        
        transmit("\nI don't handle this request: {}\n".format(request), sock)

    sock.close()
    return

def transmit(msg, sock):
    """It might take several sends to get the whole message out"""
    sent = 0
    while sent < len(msg):
        buff = bytes( msg[sent: ], encoding="utf-8")
        sent += sock.send( buff )
    

###
#
# Run from command line
#
###

def get_options():
    """
    Options from command line or configuration file.
    Returns namespace object with option value for port
    """
    # Defaults from configuration files;
    #   on conflict, the last value read has precedence
    config = configparser.ConfigParser(inline_comment_prefixes=("#", ";"))
    config.read("config/app.ini")    # General for this application
    config.read("config/host.ini")   #  ... specific to this host
    config.read("config/credentials.ini")  # ... author of program 
    target = config["DEFAULT"]["target"]
    port = int(config[target]["port"])
    docroot = config["DEFAULT"]["docroot"]
    loglevel = config["DEFAULT"]["logging"]
    
    # Command line arguments override configuration file
    parser = argparse.ArgumentParser(description="Run trivial web server.")
    parser.add_argument("--port", "-p",  dest="port", 
                        help="Port to listen on; default is {}"
                            .format(port),
                        type=int, default=port)
    parser.add_argument("--docroot", "-r", dest="docroot", default=docroot, 
                       help="Root of web documents directory; default {}"
                         .format(docroot))
    parser.add_argument("--logging", "-l", dest="logging", default=loglevel,
                            choices=["debug", "warning", "info"],
                            help="Log to level, warning < info < debug")
    options = parser.parse_args()

    if options.logging == "debug":
        logging.basicConfig(level=logging.DEBUG)
    elif options.logging == "warning":
        logging.basicConfig(level=logging.WARNING)
    elif options.logging == "info":
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.warning("Bad logging level '{}', defaulting to debug"
                            .format(options.logging))
    

    if options.port <= 1000:
        logging.warning(  ("Port {} selected. " + 
                           " Ports 0..1000 are reserved \n" + 
                           "by the operating system").format(options.port))

    return options
    

def main():
    options = get_options()
    port = options.port
    sock = listen(port)
    logging.info("Listening on port {}".format(port))
    logging.info("Socket is {}".format(sock))
    serve(sock, respond)

if __name__ == "__main__":
    main()
    
