# README #

A "getting started" project for CIS 322, software engineering 1 at University of Oregon.

### What is this repository for? ###

* The objectives of this mini-project are:
  * Initial experience with GIT workflow:  Fork the project, make and test changes locally, commit;  turn in repository URL
  * Initial experience with automated configuration for turnkey installation
  * Extend a tiny web server in Python, to check understanding of basic web architecture
  * Use automated tests to check progress (plus manual tests for good measure)

### What do I need?  Where will it work? ###

* Designed for Unix, mostly interoperable on Linux (Ubuntu) or MacOS.
  Target environment is Raspberry Pi. 
  ** May also work on Windows, but no promises.  A Linux virtual machine
   may work, but our experience has not been good; if you don't have a 
   Raspberry Pi in hand yet, you may want to test on shared server ix. 
* You will need Python version 3.4 or higher. 
* Designed to work in "user mode" (unprivileged), therefore using a port 
  number above 1000 (rather than port 80 that a privileged web server would use)

### Assignment ###
* Fork this repository to create your own repository on Github.  (Read the 'git' documentation as needed, and create an account on Github if you don't have one.) 
* Clone your repository onto the machine you want to work on.
* Make and test your changes.  Use both automated tests (the script in
the 'tests' directory) and some manual tests.  In addition to your
development environment, test on a Raspberry Pi running Ubuntu. 
* Revise this README.md file:  Erase what is no longer relevant and 
  add identifying information. 
  ### Author: Lil (Nancy) Magill , jill@uoregon.edu ###

* Commit and push ALL your changes to github (except those not under 
  revision control)
* Test deployment to other environments including Raspberry Pi.  Deployment 
  should work "out of the box" with this command sequence: 
  ** git clone <yourGitRepository> <targetDirectory>
  ** cd <targetDirectory>
  ** make configure
  ** make run 
  ** (control-C to stop program)
* Turn in the github or URL to your repository

### Who do I talk to? ###

* Maintained by Michal Young, michal@cs.uoregon.edu
* Use our Piazza group for questions. Make them public (anonymous or not as you prefer) unless you have a good reason to make them private, so that everyone benefits from answers and discussion. 
