'''Deals with the requests to the dehashed API'''
import requests
from requests.auth import HTTPBasicAuth
import json
import sys

from misc import parsed
from data_print import output
from colours import prettier_print
from validation import cred_fetch

def results(parsed_args):
    ls,count = [],1
    target = parsed_args[::-1][0]
    email,key = cred_fetch(parsed_args)
    headers_dict = {'Accept':'application/json'}
    print(f"\r {prettier_print.OKPINK}Starting!!{prettier_print.ENDC}",end="")
    while True:
        if '-d' in parsed_args or '--domain' in parsed_args:
            request = requests.get('https://api.dehashed.com/search?query=email:@%s&page=%s'%(target,count),auth=HTTPBasicAuth(email,key),headers=headers_dict)
        elif '-se' in parsed_args or '--single_email' in parsed_args:
            request = requests.get('https://api.dehashed.com/search?query=%s&page=%s'%(target,count),auth=HTTPBasicAuth(email,key),headers=headers_dict)

        elif '-el' in parsed_args or '--email_list' in parsed_args:
            try:
                with open(target,'r') as targets:
                    for i in targets.readlines():
                        request = requests.get('https://api.dehashed.com/search?query=%s&page=1'%(i),auth=HTTPBasicAuth(email,key),headers=headers_dict)
                        returned = json.loads(request.text)
                        response = parsed(returned['entries'],i)
                        ls.extend(response)
                        print(f"\r {prettier_print.OKPINK}|Requests:{count}|Parsed:{len(ls)}|Requests Remaining:{returned['balance']}{prettier_print.ENDC}",end="")
                        count+=1
                    break
            except:
                print(f"\n\n{prettier_print.FAIL}{prettier_print.UNDERLINE}File not found!{prettier_print.ENDC}\n\n")
            break

        if request.text =='{"message":"You hit your monthly query limit! Contact support to upgrade plan.","success":false}\n':
            print(f"\r\n\n{prettier_print.FAIL}{prettier_print.UNDERLINE}OUT OF CREDIT! EXITING...{prettier_print.ENDC}\n\n")
            output(ls)
            sys.exit()
        elif request.text == '{"message":"Invalid API credentials.","success":false}\n':
            print(f"\r\n\n{prettier_print.FAIL}{prettier_print.UNDERLINE}Invalid credentials passed!!!{prettier_print.ENDC}\n\n")
            sys.exit()
        elif request.status_code != 200:
            print(f"\r\n\n{prettier_print.FAIL}{prettier_print.UNDERLINE}Request failed with a status code of {request.status_code}.{prettier_print.ENDC}\n\n")
            sys.exit()
        else:
            returned = json.loads(request.text)
            response = parsed(returned['entries'],target)
            ls.extend(response)
            print(f"\r {prettier_print.OKPINK}|Requests:{count}|Parsed:{len(ls)}|Requests Remaining:{returned['balance']}{prettier_print.ENDC}",end="")
        
        if len(response)<5000:
                break
        else:
            count+=1
            time.sleep(0.06)
    output(ls,parsed_args)

    