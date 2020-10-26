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



def listparsed(text,target):
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
        return None
    

def concat(text):
    checkls,dic=[],{}
    for i in text:
        email=i.split(':')[0].lower()
        password=i.split(':')[1]
        if email not in checkls:
            checkls.append(email)
            dic["%s:"%email]=password
        else:
            dic["%s:"%email] = "%s, %s"%(dic["%s:"%email],password)
    return dic