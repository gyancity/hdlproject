# REST-BITER
A micro-tool for quickly testing REST endpoints by automatically issuing multiple GET requests randomly distributed over time.

Requires
-------
Python 2.7+

Install
-------
Just copy the Python script file where needed.

Usage
-------
Run the Python script with the needed parameters.
The results of the calls are both printed in the console and saved into a log file in the file system.

Usage example
-------
```
python restBiter.py http://www.ivanomalavolta.com 10 0 2000 20000
```

Analizes the "http://www.ivanomalavolta.com" URL by making 10 GET requests every *t* milliseconds, where *t* is a random number between 0 and 2 seconds; sometimes the requests will be made after 20 seconds (outlier waiting time).


Command line parameters
-------
Parameter | Description
----------|------------
url | the URL of the REST endpoint to call (an HTTP GET request will be performed)
num_requests | the number of requests to be done, -1 for making an unbounded number of requests
t_min | minimum waiting time in milliseconds
t_max | maximum waiting time in milliseconds
t_outlier | outlier waiting time in milliseconds
