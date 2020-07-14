"""All data processing functions
                       
Just processes the data.

"""

import numpy
import sys

from colours import prettier_print
from misc import concat

def output(response,parsed_args):
    concatd = concat(response)
    
    if '-A' in parsed_args or '--All' in parsed_args:
        wordlist(response)
        assoc_passwords(response,concatd)
        emails(response,concatd)
        stats(response,concatd)
        sys.exit()
        
    if '-w' in parsed_args or '--wordlist' in parsed_args:
        wordlist(response)

    if '-ap' in parsed_args or '--associated_passwords' in parsed_args:
        assoc_passwords(response,concatd)
        
    if '-e' in parsed_args or '--emails' in parsed_args:
        emails(response,concatd)

    if '-s' in parsed_args or '--stats' in parsed_args:
        stats(response,concatd)

def wordlist(value): 
    print(f"\n\n\n{prettier_print.HEADER}[+] ===WORDLIST=== \n{prettier_print.ENDC}    Email and Password pairs seperated by a colon (:) for bruteforcing\n")
    for i in numpy.unique(value):
        if i[::-1][0] == ':':
            pass
        else:
            print(i)

    
def assoc_passwords(value,concatd):
    print(f"\n\n\n{prettier_print.HEADER}[+] ===ASSOCIATED PASSWORDS==={prettier_print.ENDC}\n    Email addresses given with all associated passwords found\n")
    orderedkeys = sorted(concatd, key=lambda k: len(concatd[k].split(',')), reverse=True)
    for i in orderedkeys:
        try:
            if len(concatd[i].split(','))>5:
                print(f"{prettier_print.FAIL}{i}{concatd[i]}{prettier_print.ENDC}")
            elif len(concatd[i].split(','))>2:
                print(f"{prettier_print.WARNING}{i}{concatd[i]}{prettier_print.ENDC}")
            else:
                print(f"{prettier_print.OKPINK}{i}{concatd[i]}{prettier_print.ENDC}")
        except:
            print("%s%s"%(i,concatd[i]))

def emails(value,concatd):
    print(f"\n\n\n{prettier_print.HEADER}[+] ===EMAILS==={prettier_print.ENDC}\n    Just the emails\n")
    placeholderls = []
    for i in concatd.keys():
        placeholderls.append(i.lower())
    for i in sorted(placeholderls):
        print(i[:-1])

def stats(value,concatd):
    print(f"\n\n\n{prettier_print.HEADER}[+] ===STATISTICS=== \n{prettier_print.ENDC}    Totals and averages for extra value\n")
    print(" Total Records Found: %s"%(len(value)))
    print(" Total Unique Records found: %s\n"%(len(concatd)))


