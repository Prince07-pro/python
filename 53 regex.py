import re

def validate(str):
    str = input("enter a : ")
    pat= r"^[a-z]+[!@#$%]+[0-9]+$"
    
    if re.fullmatch(pat , str):
        return True
    else:
        return False

### re is module to use complex search , pattern and apply to strings
#-> found to a when keyword found in string or not
#  ^ start a string and $ end with string


# \d is found a any digit
###import re
#def numberMatcher(str):
    #pat=r"\d+"
    #match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
    #if(match): 
   #     for i in match:
  #          print(i, end=" ")
 #   else:
#        print(-1,end="")


# [] a set of  a characters means any vowel[a,e,i,o,u]