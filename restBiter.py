#!/usr/bin/env python

__author__ = "Ivano Malavolta"
__organization__ = "Gran Sasso Science Institute"
__copyright__ = "Copyright 2015"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Ivano Malavolta"
__email__ = "ivano.malavolta@gssi.infn.it"
__status__ = "Prototype"

import logging
import httplib2
import sys
import random
from time import sleep

def printUsageAndExit():
	print("Usage: python restBiter.py url num_requests t_min t_max t_outlier")
	print("where:")
	print("url: the REST endpoint to call")
	print("num_requests: the number of requests to be done, -1 for making an unbounded number of requests")
	print("t_min, t_max, t_outlier: waiting times in milliseconds")
	exit()

logFileName = 'restBiter.log'

## Here we setup the logger
rootLogger = logging.getLogger()
logFormatterString = '%(asctime)s [%(levelname)-5.5s] --- %(message)s'
logFormatter = logging.Formatter(logFormatterString)
logging.basicConfig(format=logFormatterString, filemode='w', filename=logFileName, level=logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

## Here we manage the arguments passed via the command line
if(len(sys.argv) != 6):
	printUsageAndExit()
else:
	try:
		restUrl = sys.argv[1]
		numRequests = int(sys.argv[2])
		t_min = int(sys.argv[3])
		t_max = int(sys.argv[4])
		t_outlier = int(sys.argv[5])
	except:
		printUsageAndExit()

## Loop
i = 0
while((numRequests == -1) | (i<numRequests)):
	i += 1
	# let's compute the waiting time
	waitingTime = random.randrange(t_min, t_max)
	if(waitingTime >= (t_max / 8.0) * 7):
		waitingTime = t_outlier
	waitingTime = waitingTime / 1000.0

	# sleeping...
	logging.info("Waiting time (in seconds): " + str(waitingTime))
	sleep(waitingTime)

    # let's make the call!
	# response = the header of the response
	# payload = the payload of the response
	logging.info("Calling URL: " + restUrl)
	response, payload = httplib2.Http().request(restUrl)

	# log the response from the server
	logging.info("Header: " + str(response))
	logging.info("Payload: " + str(payload))
