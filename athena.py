import requests, time, sys, re, numpy, json


from dhashd_req import results
from data_print import output
from colours import prettier_print
from validation import arg_vali
   

if __name__ == '__main__':
    try:
        owl = '''\n            !WWWWWeeu..   ..ueeWWWWW!
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
        print(f"{prettier_print.OKGREEN}{owl}")
        print("\n============ Athena: Dehashed API CLI ============")
        print(f"     Scrape Dehashed's database via their API {prettier_print.ENDC}\n")
        if '-h' in sys.argv or '--help' in sys.argv or sys.argv[::-1][0] == "athena.py":
            print("Useage: python3 athena.py [ARGUMENTS] [SEARCH_TERM]")
            print("Example: python3 athena.py -A -d example.com")
            print("Argument:                      Explanation:")
            print("   -u/--username                  - Passing your dehashed username/email")
            print("   -k/--key                       - Passing your dehashed API key")
            print("   -c/--credentials               - Pass a file with email and api key seperated by a space/colon")
            print("   -w/--wordlist                  - Email and Password pairs seperated by a colon (:) for bruteforcing")
            print("   -ap/--associated_passwords     - Email addresses given with all associated passwords found")
            print("   -e/--emails                    - Just the emails")
            print("   -s/--stats                     - Totals and averages for extra value")
            print("   -A/--All                       - Output all the above formats (default)")
            print("   -d/--domain                    - Specifies the search term is a domain (default)")
            print("   -se/--single_email             - Specifies the search term is a single email address")
            print(f"   -el/--email_list               - Specifies the seach term is a text file of email address, and checks for associated passwords {prettier_print.WARNING}(WARNING: credit intensive){prettier_print.ENDC}")
            print(f"   -h/--help                      - Displays this menu.\n")
            sys.exit()
        else:
            parsed_args = arg_vali()
            results(parsed_args)
    except KeyboardInterrupt:
        print(f"\n{prettier_print.FAIL}{prettier_print.UNDERLINE}{prettier_print.BOLD}Keyboard Interrupt detected from user. Quitting!{prettier_print.ENDC}")
        sys.exit()

