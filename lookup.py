import os,sys,string
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
	print("+----------------------+")
	print("|       查词帮         |")
	print("|  一个更方便的查词工具|") 
	print("+----------------------+")

welcom()
lookup_cmd = "trans -sp  :zh info_to_lookup"
notify_cmd = "notify-send -i face-glasses TITLE \"`trans -p  -brief :zh info_to_lookup`\""
recent_value = pyperclip.paste()
while not is_sigint_up:
	tmp_value = pyperclip.paste()
	if tmp_value != recent_value:
		recent_value = tmp_value
		cmd_0 = lookup_cmd.replace('info_to_lookup',recent_value)
		cmd_1 = notify_cmd.replace('info_to_lookup', recent_value).replace('TITLE',recent_value)
		os.system(cmd_0)
		os.system(cmd_1)
	time.sleep(0.1)