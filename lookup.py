#!/usr/bin/env python 
import os,sys,string,re
import time,signal
import pyperclip


# Interupt Handler
is_sigint_up = False
def sigint_handler(signum, frame):
 	global is_sigint_up
 	is_sigint_up = True
 	print ('Existing ...')
signal.signal(signal.SIGINT, sigint_handler)

def welcom():
	print('+-------------------------------------------------+')
	print('| Lookup, a more convenient tool for translation. |') 
	print('+-------------------------------------------------+\n')
welcom()
# lookup_cmd = "trans -sp  :zh info_to_lookup"
lookup_cmd = "trans   :zh info_to_lookup"
notify_cmd = "notify-send -i face-glasses TITLE \"`trans  -brief :zh info_to_lookup`\""
speak_cmd = 'echo \'info_to_speak\' | festival --tts'
# speak_cmd = 'pico2wave -l=en-US -w=/tmp/test.wav \'info_to_speak\' && aplay /tmp/test.wav '
primary_cmd = 'echo \'info_to_add\' | xsel'
# notify_cmd = "notify-send -i face-glasses TITLE \"`trans -p  -brief :zh info_to_lookup`\""
recent_value = pyperclip.paste()
counter = 0
print('[0]>> usage: Copy an English word to the clipboard.')
while not is_sigint_up:
	tmp_value = pyperclip.paste()
	if tmp_value != recent_value:
		counter += 1
		recent_value = tmp_value
		cmd_0 = lookup_cmd.replace('info_to_lookup',recent_value)
		cmd_speak = speak_cmd.replace('info_to_speak', recent_value)
		cmd_1 = notify_cmd.replace('info_to_lookup', recent_value).replace('TITLE',recent_value)
		os.system(cmd_speak)
		# Print Translations to terminal 
		translations = os.popen(cmd_0).read()
		translations = re.findall(r'[\u4e00-\u9fff]+', translations)
		print('['+str(counter)+']>>',recent_value, '\n',translations[2:],'\n')
		cmd_add_to_primary = primary_cmd.replace('info_to_add',translations[0])
		os.system(cmd_1)
		os.system(cmd_add_to_primary)
	time.sleep(0.1)
