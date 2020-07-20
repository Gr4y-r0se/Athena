'''Misc Functions'''
import sys

from colours import prettier_print

def parsed(text,target):
    returnable=[]
    try:
        for i in text:
            obj = dict(i)
            try:
                if obj['password'] == None or obj['password'] == '':
                    pass
                else:
                    if target in obj['email']:
                        returnable.append('%s:%s'%(obj['email'],obj['password']))
                    elif target in obj['password']:
                        returnable.append('%s:%s'%(obj['password'],obj['email']))
                    else:
                        pass
            except:
                pass
        return returnable
    except:
        return ['NoRecordsFound:WellDone!']
    

def concat(text):
    checkls,dic=[],{}
    for i in text:
        email=i.split(':')[0].lower()
        password=i.split(':')[1].lower()
        if email not in checkls:
            checkls.append(email)
            dic["%s:"%email]=password
        else:
            dic["%s:"%email] = "%s, %s"%(dic["%s:"%email],password)
    return dic



def cred_fetch(parsed_args):
    if parsed_args[::-1][0] in ['-c','--credentials','-u','--username','-k','--key']:
        print(f"\n{prettier_print.FAIL}{prettier_print.UNDERLINE}{prettier_print.BOLD}Specify credentials correctly!!{prettier_print.ENDC}")
        sys.exit()
    if '-c' in parsed_args:
        with open(parsed_args[parsed_args.index('-c')+1],'r') as file:
            try:
                email,key = file.readlines()[0].split(' ')
            except:
                email,key = file.readlines()[0].split(':')
    elif '--credentials' in parsed_args:
         with open(parsed_args[parsed_args.index('--credentials')+1],'r') as file:
            try:
                email,key = file.readlines()[0].split(' ')
            except:
                email,key = file.readlines()[0].split(':')
    elif '-u' in parsed_args:
        email = parsed_args[parsed_args.index('-u')+1]
        if '-k' in parsed_args:
            key = parsed_args[parsed_args.index('-k')+1]
        elif '--key' in parsed_args:
            email = parsed_args[parsed_args.index('--key')+1]
    elif '--username' in parsed_args:
        email = parsed_args[parsed_args.index('--username')+1]
        if '-k' in parsed_args:
            key = parsed_args[parsed_args.index('-k')+1]
        elif '--key' in parsed_args:
            key = parsed_args[parsed_args.index('--key')+1]
    else:
        print(f"\n{prettier_print.FAIL}{prettier_print.UNDERLINE}{prettier_print.BOLD}Specify credentials correctly!!{prettier_print.ENDC}")
        sys.exit()
    return email,key