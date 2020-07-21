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
		arguments.extend(["-d","-A",target])
		print(f"\n{prettier_print.WARNING}{prettier_print.UNDERLINE}{prettier_print.BOLD}Incorrect Arguments Specified, defaulting to '-d -A [target]'!{prettier_print.ENDC}")
		return arguments

def cred_fetch(parsed_args):
    if parsed_args[::-1][0] in ['-c','--credentials','-u','--username','-k','--key']:
        print(f"\n{prettier_print.FAIL}{prettier_print.UNDERLINE}{prettier_print.BOLD}Specify credentials correctly!!{prettier_print.ENDC}")
        sys.exit()
    try:
        if '-c' in parsed_args:
            with open(parsed_args[parsed_args.index('-c')+1],'r') as file:
                value = file.readlines()[0]
                try:
                    email,key = value.split(' ')
                except:
                    email,key = value.split(':')
        elif '--credentials' in parsed_args:
             with open(parsed_args[parsed_args.index('--credentials')+1],'r') as file:
                value = file.readlines()[0]
                try:
                    email,key = value.split(' ')
                except:
                    email,key = value.split(':')
        elif '-u' in parsed_args:
            email = parsed_args[parsed_args.index('-u')+1]
            if '-k' in parsed_args:
                key = parsed_args[parsed_args.index('-k')+1]
            elif '--key' in parsed_args:
                key = parsed_args[parsed_args.index('--key')+1]
        elif '--username' in parsed_args:
            email = parsed_args[parsed_args.index('--username')+1]
            if '-k' in parsed_args:
                key = parsed_args[parsed_args.index('-k')+1]
            elif '--key' in parsed_args:
                key = parsed_args[parsed_args.index('--key')+1]
        return email,key
    except:
        print(f"\n{prettier_print.FAIL}{prettier_print.UNDERLINE}{prettier_print.BOLD}Specify credentials correctly!!{prettier_print.ENDC}")
        sys.exit()