'''Validation Processes for arguments'''

import sys

from colours import prettier_print

def arg_vali():
	arguments = sys.argv[1:]
	valid_args_output = ['-w','--wordlist','-ap','--associated_passwords','-e','--emails','-s','--stats','-A','--All']
	valid_args_input = ['-d','--domain','-se','--single_email','-el','--email_list']
	if len(list(set(arguments).intersection(valid_args_output))) > 0 and len(list(set(arguments).intersection(valid_args_input))) == 1:
		return arguments
	else:
		target = arguments.pop()
		arguments = ["-d","-A",target]
		print(f"\n{prettier_print.WARNING}{prettier_print.UNDERLINE}{prettier_print.BOLD}Incorrect Arguments Specified, defaulting to '-d -A [target]'!{prettier_print.ENDC}")
		return arguments