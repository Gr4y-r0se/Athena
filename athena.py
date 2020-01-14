import requests
import time
from requests.auth import HTTPBasicAuth
import sys
import re

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def results(valuetext):
    global ls
    print(f"{bcolours.OKGREEN}{owl}")
    print("\n============ Athena: Dehashed API CLI ============")
    print(f"     Scrape Dehashed's database via their API \n{bcolours.ENDC}\n\n")
    ls,count = [],1
    headers_dict = {'Accept':'application/json'}
    while True:
        request = requests.get("https://dehashed.com/search?query='%s'&page=%s"%(valuetext,count),auth=HTTPBasicAuth(email,key),headers=headers_dict)
        if request.text =='{"message":"You hit your monthly query limit! Contact support to upgrade plan.","success":false}\n':
            print(f"\n\n{bcolours.FAIL}{bcolours.UNDERLINE}OUT OF CREDIT! EXITING...{bcolours.ENDC}\n\n")
            output(ls)
            sys.exit()
        elif request.text == '{"message":"Invalid API credentials.","success":false}\n':
            print(f"\n\n{bcolours.FAIL}{bcolours.UNDERLINE}Invalid credentials passed!!!{bcolours.ENDC}\n\n")
            sys.exit()
        else:
            response=parsed(request.text)
            for i in response:
                ls.append(i)
            if len(response)<5:
                break
            count+=1
            text_progress_bar(count)
            time.sleep(0.06)
    output(ls)

def text_progress_bar(count):
    print(f"\r {bcolours.OKBLUE}|Requests:{count}|",end="")
        
def parsed(text):
    returnable=[]
    for i in str(text).split('},{'):
        try:
            if i.split('"password":"')[1].split(",")[0][:-1] != "null":
                returnable.append('%s:%s'%(i.split('"email":"')[1].split(",")[0][:-1],i.split('"password":"')[1].split(",")[0][:-1]))
            elif i.split('"hashed_password":"')[1].split(",")[0][:-1] != "null":
                returnable.append('%s:%s'%(i.split('"email":"')[1].split(",")[0][:-1],i.split('"hashed_password":"')[1].split(",")[0][:-1]))
            else:
                returnable.append('%s:<no_associated_passwords_found>'%(i.split('"email":"')[1].split(",")[0][:-1]))
        except:
            pass
    return returnable

def concat(text):
    checkls,dic=[],{}
    for i in text:
        email=i.split(':')[0]
        password=i.split(':')[1]
        if email not in checkls:
            checkls.append(email)
            dic["%s:"%email]=password
        else:
            dic["%s:"%email] = "%s, %s"%(dic["%s:"%email],password)
    return dic
    
def output(response):
    concatd = concat(response)
    
    if '-A' in sys.argv or '--All' in sys.argv:
        wordlist(response)
        assoc_passwords(response,concatd)
        emails(response,concatd)
        stats(response,concatd)
        sys.exit()
        
    if '-w' in sys.argv or '--wordlist' in sys.argv:
        wordlist(response)

    if '-a' in sys.argv or '--wordlist' in sys.argv:
        assoc_passwords(response,concatd)
        
    if '-e' in sys.argv or '--emails' in sys.argv:
        emails(response,concatd)

    if '-s' in sys.argv or '--stats' in sys.argv:
        stats(response,concatd)
    
    
         
def wordlist(value):
    print(f"\n\n\n{bcolours.HEADER}[+] ===WORDLIST=== \n{bcolours.ENDC}    Email and Password pairs seperated by a colon (:) for bruteforcing\n")
    for i in sorted(value):
        if i[::-1][0] == ':':
            pass
        else:
            print(i)

    
def assoc_passwords(value,concatd):
    print(f"\n\n\n{bcolours.HEADER}[+] ===ASSOCIATED PASSWORDS==={bcolours.ENDC}\n    Email addresses given with all associated passwords found\n")
    orderedkeys = sorted(concatd, key=lambda k: len(concatd[k].split(',')), reverse=True)
    for i in orderedkeys:
        try:
            if len(concatd[i].split(','))>5:
                print(f"{bcolours.FAIL}{i}{concatd[i]}{bcolours.ENDC}")
            elif len(concatd[i].split(','))>2:
                print(f"{bcolours.WARNING}{i}{concatd[i]}{bcolours.ENDC}")
            else:
                print(f"{bcolours.OKBLUE}{i}{concatd[i]}{bcolours.ENDC}")
        except:
            print("%s%s"%(i,concatd[i]))

def emails(value,concatd):
    print(f"\n\n\n{bcolours.HEADER}[+] ===EMAILS==={bcolours.ENDC}\n    Just the emails\n")
    for i in concatd:
        print(i[:-1])

def stats(value,concatd):
    print(f"\n\n\n{bcolours.HEADER}[+] ===STATISTICS=== \n{bcolours.ENDC}    Totals and averages for extra value\n")
    print(" Total Records Found: %s"%(len(value)))
    print(" Total Unique Records found: %s\n"%(len(concatd)))

def arg_vali():
    
    valid_args = ['-w','--wordlist','-ap','--associated_passwords','-e','--emails','-s','--stats','-A','--All']
    for i in sys.argv:
        for it in valid_args:
            if i == it:
                return True
    return False

def emailvalidation(email):
    if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
        return True
    else:
        return False

def cred_fetch():
    global email,key
    if sys.argv[::-1][0] in ['-c','--credentials','-u','--username','-k','--key']:
        print(f"\n{bcolours.FAIL}{bcolours.UNDERLINE}{bcolours.BOLD}Specify credentials correctly!!{bcolours.ENDC}")
        sys.exit()
    if '-c' in sys.argv:
        with open(sys.argv[sys.argv.index('c')+1],'r') as file:
            email,key = file.readlines()[0].split(' ')
    elif '--credentials' in sys.argv:
         with open(sys.argv[sys.argv.index('c')+1],'r') as file:
            email,key = file.readlines()[0].split(' ')
    elif '-u' in sys.argv:
        email = sys.argv[sys.argv.index('-u')+1]
        if '-k' in sys.argv:
            key = sys.argv[sys.argv.index('-k')+1]
        elif '--key' in sys.argv:
            email = sys.argv[sys.argv.index('--key')+1]
    elif '--username' in sys.argv:
        email = sys.argv[sys.argv.index('--username')+1]
        if '-k' in sys.argv:
            key = sys.argv[sys.argv.index('-k')+1]
        elif '--key' in sys.argv:
            key = sys.argv[sys.argv.index('--key')+1]
    else:
        print(f"\n{bcolours.FAIL}{bcolours.UNDERLINE}{bcolours.BOLD}Specify credentials correctly!!{bcolours.ENDC}")
        sys.exit()
    

if __name__ == '__main__':
    try:
        owl = '''\n!WWWWWeeu..   ..ueeWWWWW!
 "$$(    R$$e$$R    )$$"
  "$8oeeo. "*" .oeeo8$"
  .$$#"""*$i i$*"""#$$.
  9$" @*c $$ $$F @*c $N
  9$  NeP $$ $$L NeP $$
  `$$uuuuo$$ $$uuuuu$$"
  x$P**$$P*$"$P#$$$*R$L
 x$$   #$k #$F :$P` '#$i
 $$     #$  #  $$     #$k
d$"     '$L   x$F     '$$
$$      '$E   9$>      9$>
$6       $F   ?$>      9$>
$$      d$    '$&      8$
"$k    x$$     !$k    :$$
 #$b  u$$L      9$b.  $$"
 '#$od$#$$u....u$P$Nu@$"
 ..?$R)..?R$$$$*"  #$P
 $$$$$$$$$$$$$$@WWWW$NWWW
 `````""3$F""""#$F"""""""
        @$.... '$B
       d$$$$$$$$$$:
       ````````````'''
        cred_fetch()
        if '-h' in sys.argv or '--help' in sys.argv:
            print(f"{bcolours.OKGREEN}{owl}")
            print("\n============ Athena: Dehashed API CLI ============")
            print("     Scrape Dehashed's database via their API \n")
            print(f"{bcolours.OKBLUE}Useage: python3 Athena.py [ARGUMENTS] [SEARCH_TERM]")
            print("Argument:                      Explanation:")
            print("-u/--username                  - Passing your dehashed username/email")
            print("-k/--key                       - Passing your dehashed API key")
            print("-c/--credentials               - Pass a file with email and api key seperated by a space")
            print("-w/--wordlist                  - Email and Password pairs seperated by a colon (:) for bruteforcing")
            print("-ap/--associated_passwords     - Email addresses given with all associated passwords found")
            print("-e/--emails                    - Just the emails")
            print("-s/--stats                     - Totals and averages for extra value")
            print("-A/--All                       - Output all the above formats (Default)")
            print(f"-h/--help                      - Displays this menu.{bcolours.ENDC}\n")
        
            sys.exit()
        elif arg_vali() == False:
            print(f"\n{bcolours.FAIL}{bcolours.UNDERLINE}{bcolours.BOLD}Specify valid arguments, or use -h for more info!{bcolours.ENDC}")
        elif emailvalidation(sys.argv[::-1][0]) == True:
            results(sys.argv[::-1][0])
        else:
            print(f"\n{bcolours.FAIL}{bcolours.UNDERLINE}{bcolours.BOLD}Specify a valid searchterm, or use -h for more info!{bcolours.ENDC}")
    except KeyboardInterrupt:
        output(ls)
        sys.exit()

