from ast import Try
import requests

url = 'http://127.0.0.1:8000/'

def internet_verify():
	""" This method is to verify internet connection """
	url = 'http://127.0.0.1:8000/'
	timeout = 4
	try:
		requests.get(url, timeout=timeout)
		return True
	except (requests.ConnectionError, requests.Timeout) as exception:
		return False

def read_file():
	with open('senteces.txt', 'r') as file:
		for line in file:
			print(line)

def send_log():
    if(internet_verify()):
        with open('senteces.txt', 'r') as f:
            for line in f.readlines():
                print('data in post')
                requests.post(url, json={"value" : "eu sou mbora nem mau"})
    else:
        print('dont goo')

send_log()