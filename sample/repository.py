from ast import Try
import requests

URL = 'http://127.0.0.1:8000'
headers = {'content-type': 'application/json'}

def internt_verify():
	#This function the key who is press, when is press
    try:
        requests.get(URL, headers=headers)
        return True
    except requests.RequestException as e:
        return False

def post_log(date: str=''):
    """Function to post log's"""
    data = {'log' : date}
    try:
        response = requests.post(URL + '/send_log', json=data, headers=headers)
        print(response.text)
    except Exception as error:
        print(error)

def send_log():
    #Read the senteces file
	with open('senteces.txt', 'r') as f:
		for line in f.readlines():
			post_log(date=line)



