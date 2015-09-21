# README #

A "getting started" project for CIS 322, software engineering 1 at University of Oregon.

### What is this repository for? ###

* The objectives of this mini-project are:
  * Initial experience with GIT workflow:  Fork the project, make and test changes locally, commit;  turn in repository URL
  * Extend a tiny web server in Python, to check understanding of basic web architecture

### What do I need?  Where will it work? ###

* Designed for Unix, mostly interoperable on Linux (Ubuntu) or MacOS.  May also work on Windows, but no promises.  Consider creating a Linux virtual machine under Windows if you have trouble there, or just work on ix. 
* You will need Python version 3.4 or higher. 
* Designed to work in "user mode" (unprivileged).  Randomly chooses a port, so it could occasionally fail because the port is already in use.  

### Assignment ###
* Fork this repository to create your own repository on Github.  (Read the 'git' documentation as needed, and create an account on Github if you don't have one.) 
* Clone your repository onto the machine you want to work on.
* Make and test your changes
  * Your pageserver should serve web pages (text files with names that end with .html) and style sheets (text files that end with .css) from the directory in which the server is run.  It should reject URLs that contain '~' or '..' or '//', so that it cannot be used to read files outside of that directory.  For any rejected URL, as well as for URLs that do not match a file in the current directory, your pageserver should respond with 'I don't handle this request', followed by the request.
  *  Test your pageserver on ix.cs.uoregon.edu, even if you use a different machine to develop it.  (You can use git to develop on one machine and test on others.) 
* Commit and push your changes to github
* Give repository access to the instructor (user MichalYoung on github)
* Turn in the URL to your repository so I can clone and test it for grading.  We will use Canvas for turn-in, but you turn in only the URL of your Github repository, not your files. 

### Who do I talk to? ###

* Maintained by Michal Young, michal@cs.uoregon.edu
* Use our Piazza group for questions. Make them public (anonymous or not as you prefer) unless you have a good reason to make them private, so that everyone benefits from answers and discussion. 
