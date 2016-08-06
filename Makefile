# Makefile for simple page server. 
#
run:	CONFIG.py
	python3 pageserver.py

CONFIG.py:
	./configure

