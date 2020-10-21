#Say "Hello, World!" With Python

print("Hello, World!")

#Python If-Else

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
if n%2!=0 :
    print("Weird")
else :
    if 2<=n<=5 :
        print("Not Weird")
    else :
        if 6<=n<=20 :
            print("Weird")
        else :
            if n>20 :
                print("Not Weird")
                
  

#Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print(a+b)
print(a-b)
print(a*b)


#Python: Division

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(int(a/b))
print(float(a/b))


#Loops

if __name__ == '__main__':
    n = int(raw_input())
i=0
while i<n:
    print(i*i)
    i=i+1
    

#Write a function

 def is_leap(year):
    leap = False
    if year%4==0 and year%100!=0:
        leap=True
    if year%4==0 and year%100==0 and year%400==0:
        leap=True
    return leap
  
  
  #Print Function

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

for i in range(1,n+1):
    print(i,end=''),
    
   
  
  #sWAP cASE

def swap_case(s):
    return s.swapcase()
  
  
  #String Split and Join

def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line
  
  
  #What's Your Name?

def print_full_name(a, b):
    print("Hello "+ a+ " " +b+"! You just delved into python.") 
    return
  
  
  #Mutations

def mutate_string(string, position, character):
    string=string[:position]+character+string[position+1:]
    return string
  
  
  #Find a string
  
def count_substring(string, sub_string):
    cont=0
    for i in range(0,len(string)):
        if i+len(sub_string)<=len(string):
           if string.find(sub_string,i,i+len(sub_string))!=-1:
              cont=cont+1    
    return cont
  
  
  #String Validators
  
  if __name__ == '__main__':
    s = raw_input()
is_isalnum=False
is_isalpha=False
is_isdigit=False
is_islower=False
is_isupper=False
for i in range(0,len(s)):
    if s[i].isalnum():
        is_isalnum=True
    if s[i].isalpha():
        is_isalpha=True
    if s[i].isdigit():
        is_isdigit=True
    if s[i].islower():
        is_islower=True
    if s[i].isupper():
        is_isupper=True
print(is_isalnum)
print(is_isalpha)
print(is_isdigit)
print(is_islower)
print(is_isupper)



#Text Wrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
  
  
  
  #Capitalize!

def solve(s):
    a = s.split(' ')
    for i in range(len(a)):
        a[i]= a[i].capitalize()
    return ' '.join(a)
  
  
  
  #List Comprehensions

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])



#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
lis=[] 
for i in range(0,len(arr)):
    lis.append(arr[i])
num_max=lis.count(max(lis))
for j in range(num_max):
    lis.remove(max(lis))
print(max(lis))



#Nested Lists

score_list=[]
nested_list=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    score_list.append(score)
    nested_list.append([name,score])
second_min_score=sorted(list(set(score_list)))[1]
stamp_name=[]
for k in range(len(score_list)):
    if nested_list[k][1]==second_min_score:
        stamp_name.append(nested_list[k][0])
stamp_name.sort()
for h in range(len(stamp_name)):
    print(stamp_name[h])
    
    
    
#Finding the percentage

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
result=list(student_marks[query_name])
average=sum(result)/len(result)
print("%.2f" %  average)


#Tuples

import hashlib
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
tup=()
for i in range(n):
    tup=tup+(integer_list[i],)
print(hash(tup))



#Lists

if __name__ == '__main__':
    N = int(raw_input())
lis=[]
for i in range(0,N):
    req=raw_input().split()
    if req[0]=="insert":
        lis.insert(int(req[1]),int(req[2]))
    elif req[0]=="print":
        print(lis)
    elif req[0]=="remove":
        lis.remove(int(req[1]))
    elif req[0]=="append":
        lis.append(int(req[1]))
    elif req[0]=="sort":
        lis.sort()
    elif req[0]=="pop":
        lis.pop()
    elif req[0]=="reverse":
        lis.reverse()

        
        
#Text Alignment

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)

    
    
  #Designer Door Mat

N, M = raw_input().split()
t='-'
text='.|.'
text5='WELCOME'
for i in range(int(int(N)/2)):
    print (text*2*i+text).center(int(M),t)
print text5.center(int(M),t)
for i in range(int(int(N)/2)):
    j=int(int(N)/2)-i-1
    print (text*2*j+text).center(int(M),t)
    
    
    
   #String Formatting

def print_formatted(number):
    width=len(str(bin(number))[2:])
    for i in range(1,number+1):
        d=str(i)
        o=oct(i)[1:]
        h=hex(i)[2:].upper()
        b=bin(i)[2:]
        print d.rjust(width),o.rjust(width),h.rjust(width),b.rjust(width)
        
        
        
  #Merge the Tools!
  
  def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sub_string=string[i:i+k]
        final_string=''
        for el in sub_string:
            if el not in final_string:
                final_string+=el
        print(final_string)
        
        
        
  #Introduction to Sets

def average(array):
    no_rip=set(array)
    somma=sum(no_rip)
    
    output=somma/len(no_rip)
    return output
   
    
   
 #Symmetric Difference

M=int(raw_input())
set1= set(map(int, raw_input().split()))
N=int(raw_input())
set2=set(map(int, raw_input().split()))
union=set1.union(set2)
intersection=set1.intersection(set2)
out=sorted(union.difference(intersection))
for el in out:
    print(el)
    
    
    
  #No Idea!

n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))


 #Set .add()

N=int(raw_input())
set_c=set()
for i in range(N):
    i_country=raw_input()
    set_c.add(i_country)
print(len(set_c))



 #Set .discard(), .remove() & .pop()

n = input()
s = set(map(int, raw_input().split()))
N=input()
for i in range(N):
    text=raw_input().split()
    if text[0]=="pop":
        s.pop()
    elif text[0]=="discard":
        s.discard(int(text[1]))
    elif text[0]=="remove":
        s.remove(int(text[1]))
add=0
for el in s:
    add+=el
print(add)



 #Set .union() Operation

n=int(raw_input())
A=set(raw_input().split())
m=int(raw_input())
B=set(raw_input().split())
inters=A.intersection(B)
A2=A.difference(inters)
output=A2.union(B)
cont=0
for el in output:
    cont+=1
print(cont)



 #Set .intersection() Operation

n=int(raw_input())
A=set(raw_input().split())
b=int(raw_input())
B=set(raw_input().split())
output=A.intersection(B)
cont=0
for el in output:
    cont+=1
print(cont)



 #Set .difference() Operation

n=int(raw_input())
A=set(raw_input().split())
b=int(raw_input())
B=set(raw_input().split())
inters=A.intersection(B)
output=A.difference(inters)
cont=0
for el in output:
    cont+=1
print(cont)



 #Set .symmetric_difference() Operation

n=int(raw_input())
A=set(raw_input().split())
b=int(raw_input())
B=set(raw_input().split())
output=A.symmetric_difference(B)
cont=0
for el in output:
    cont+=1
print(cont)


 #Set Mutations

n=int(raw_input())
A=set(raw_input().split())
N=int(raw_input())
for i in range(N):
    text=raw_input().split()
    set_i=set(raw_input().split())
    if text[0]=="intersection_update":
       A.intersection_update(set_i)
    elif text[0]=="update":
        A.update(set_i)
    elif text[0]=="symmetric_difference_update":
        A.symmetric_difference_update(set_i)
    elif text[0]=="difference_update":
        A.difference_update(set_i)
        
        
     
 #The Captain's Room

K=int(raw_input())
rooms=list(map(int,raw_input().split()))
no_rip=set(rooms)
for el in no_rip:
    cont=0
    for i in rooms:
        if el==i:
            cont+=1
        if cont==2:
            break
    if cont==1:
        print(el)
        exit()  
        
        
    
 #Check Subset

T=int(raw_input())
for i in range(T): 
    a = int(raw_input())
    A = set(raw_input().split())
    b = int(raw_input())
    B = set(raw_input().split())
    print A <= B
    
    
 
 #Alphabet Rangoli

import string

def print_rangoli(size):
    if size == 1:
        print('a')
        exit()
    A = list(string.ascii_lowercase)
    numero_stanghe = (size)*4-3
    t = '-'
    first = A[size-1].center(numero_stanghe, t)
    print A[size-1].center(numero_stanghe, t)
    last = A[size-1].center(numero_stanghe, t)
    countrary = []
    # your code goes here
    for i in range(size):
        #t = '-'*numero_stanghe
        if i == 0 :
            next 
        else:
            center = A[size-i-1]
            K = i
            costruisci = A[size-1]
            sinistra = ""
            for k in range(K, 0, -1):
                sinistra += '-'+A[size-k]
            sinistra = sinistra[::-1]
            destra = sinistra[::-1]
            final = sinistra+center+destra
            countrary.insert(0, final.center(numero_stanghe, t))
            print final.center(numero_stanghe, t)
    countrary.pop(0)
    for elem in countrary:
        print(elem)
    print last
    
    
    
    
  #collections.Counter()

X=int(raw_input())
shoe_size=map(int,raw_input().split())
N=int(raw_input())
earn=0
for i in range(N):
    customer=map(int,raw_input().split())
    if customer[0] in shoe_size:

        earn+=customer[1]
        shoe_size.remove(customer[0])
print(earn)


  
  #DefaultDict Tutorial

from collections import defaultdict
d = defaultdict(list)
n , m=raw_input().split()

for i in range(int(n)):
    a=raw_input()
    d[a].append(i+1)
for j in range(int(m)):
    b=raw_input()
    if b in d:
       print (' '.join(map(str, d[b])))
    else:
        print(-1)
        
        
        
   #Collections.namedtuple()

from collections import namedtuple
summ=0
N=int(input())
students=namedtuple("students",input().split())
for i in range(N):
    #stud=input().split()
    summ+=int(students(*input().split()).MARKS)
print(float(summ/N))



  #Collections.OrderedDict()

from collections import OrderedDict
N=int(input())
od = OrderedDict()
for i in range(N):
    item=input().split()
    item_name=' '.join(item[:-1])
    sum_item=0
    if item_name in od:
        sum_item+=int(item[-1])
        od[item_name]=sum_item+int(od[item_name])
    else: 
        od[item_name]=item[-1] 
for key, value in od.items(): 
    print(key, value)    
    
    
    
  #Word Order

from collections import Counter
lst=[]
n=int(input())
for i in range(n):
     lst.append(input())
no_rip_lst=set(lst)
print(len(no_rip_lst))
print(*Counter(lst).values())



  #Collections.deque()

from collections import deque
d=deque()
n=int(input())
for i in range(n):
    text=input().split()
    if text[0]=='append':
        d.append(text[1])
    elif text[0]=='appendleft':
        d.appendleft(text[1])
    elif text[0]=='pop':
        d.pop()
    elif text[0]=='popleft':
        d.popleft()
print(*d)



 #Company Logo
  
from collections import Counter
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    s = list(input())
    s_sort=sorted(s)
    c=Counter(Counter(s_sort).most_common(3))
    for key in c.keys():
      print(*key)
      
      
  
 #Piling Up!

from collections import deque
T=int(input())
for i in range(T):
    num_cubes=int(input())
    side_cubes=deque(map(int,input().split()))
    if side_cubes[0]<side_cubes[-1] :
        m=side_cubes[-1]
        side_cubes.pop()
    else :
        m=side_cubes[0]
        side_cubes.popleft()   
    bool=True
    while side_cubes:
        if side_cubes[0]<side_cubes[-1]: #è più grande l'ultimo elemento
            if side_cubes[-1]<=m:        #posso impilarlo
                m=side_cubes[-1]
                side_cubes.pop()
            else:                        #non posso impilarlo                     
              print('No')
              bool=False
              break
        else:                           #è più grande il primo elemento
            if side_cubes[0]<=m:
                m=side_cubes[0]
                side_cubes.popleft()
            else:
               print('No')
               bool=False
               break
    if bool==True:
        print('Yes')
        
      
     
  #Calendar Module

import calendar
date=input().split()
w_d=calendar.weekday(int(date[2]),int(date[0]),int(date[1]))
print(calendar.day_name[int(w_d)].upper())




 #Time Delta

import math
import os
import random
import re
import sys
import datetime
from datetime import timedelta
from datetime import datetime

def time_delta(t1, t2):
    time_1=datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time_2=datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff=time_1-time_2
    return (str(abs(int(diff.total_seconds()))))
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

    
    
    
  #Exceptions

T=int(input())
for i in range(T):
    a_b=input().split()
    try:
        a=int(a_b[0])  
    except ValueError as v:
        print("Error Code:", v) 
    else:
        
        try:
            b=int(a_b[1])          
        except ValueError as v:
            print("Error Code:", v)   
        else:  
            try:
               print (int(int(a_b[0]) / int(a_b[1])))
            except ZeroDivisionError :
               print ("Error Code: integer division or modulo by zero") 
                
                
                
    
 #Zipped!

s_m=input().split()
X=[]
for i in range(int(s_m[1])):
    A=map(float, input().split())
    X+=[A]

Z=zip(*X)
for j in Z:
    print(sum(j)/int(s_m[1]))
    
    
    
    
 #Input()
x_k=raw_input().split()
pol=raw_input()
x=int(x_k[0])

if eval(pol)==int(x_k[1]):
    print('True')
else:
    print('False')
    
    
    
 #Python Evaluation

inp=str(input())
var=inp[5:len(inp)]
print(eval(var))



 #Map and Lambda Function
  
cube = lambda x: pow(x,3)
def fibonacci(n):
    if n==0:
        return([])
    if n==1:
        return([0])
    fib=[0,1]
    for i in range(n-2):
        fib.append(int(fib[-1]+fib[-2]))
    return(fib)
  
  
  
  #Detect Floating Point Number

def is_float(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False

n = int(input())
lines = [input().strip() for _ in range(n)]
for l in lines:
    if(l=='0'): print(False)
    else:
        print(is_float(l))
  
 
    
 #Re.split()

regex_pattern = r'[,.]+'



 #Group(), Groups() & Groupdict()

string=input()
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        
        if string[i].isalnum():
            print(string[i])
            exit()
print('-1')



 #Re.findall() & Re.finditer()

import re
txt=str(input())
v=re.findall(r'(?<=[b-df-hj-np-tv-xz])([AEIOUaeiou]{2,})[?=b-df-hj-np-tv-z]',txt)
if v:
    for i in v:
        print(i)
else:
    print('-1')
    
    
    
 #Re.start() & Re.end()

import re
string=str(input())
sub_string=input()
#pattern=re.compile(input())
m=re.finditer(r'(?=('+sub_string+'))',string)
s=re.search(r'(?=('+sub_string+'))',string)
if s:
    for i in m:
        print((i.start(1),i.end(1)-1))
else:
    print ('(-1, -1)')
    
    
    
    
#Regex Substitution

import re
for i in range(int(input())):
    string=''
    string=re.sub(r'(?<= )&&(?= )','and',input())   
    string=re.sub(r'(?<= )\|\|(?= )','or',string)
    print(string)
    
    
    
#Validating phone numbers

import re
n=input()
for i in range(int(n)):
    number=input()    
    if len(number)==10:
        if number.isdigit():
           if re.match(r'7|8|9',number):
               print('YES')
           else: 
               print('NO')
        else:
            print('NO')
    else:
        print('NO')
        
        
        
#Validating and Parsing Email Addresses

import re
n=int(input())
for i in range(n):
    inp=input()
    e=inp.split()
    email=e[1]
    m=re.match(r'^<[A-Za-z]+[0-9a-zA-Z._-]+@[A-Za-z]+\.[a-z]{1,3}>$',str(email))
    if m:
        print(inp)
        
        
        
        
#Hex Color Code

import re
for i in range(int(input())):
    txt=input()
    if len(txt.split())>1 and  '{' not in txt:
        r=re.findall(r'#[0-9A-Fa-f]{3,6}',str(txt))
        for el in r:
            print(el)
            
            
            
#Validating Roman Numerals

regex_pattern = r"^(?=[MDCLXVI])(M{0,3})(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"



 #HTML Parser - Part 1

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
parser = MyHTMLParser()
for i in range(int(input())):
     parser.feed(input())
    
    
    
    
#Validating UID

import re
n=int(input())
for i in range(n):
    UID=str(input())
    if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})(?!.*(.).*\1)',UID):
        if len(UID)==10:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
        
        
        
        
 #Validating Credit Card Numbers

import re
N=int(input())
for i in range(N):
    card=str(input())
    if re.match(r'^[4-6]',card): #primo numero 4 5 o 6
    #16 numeri o 19 numeri e trattino
        if re.match(r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{16}$',card):
            if '-' in card:
                card.replace('-','',4)              
            if re.search(r'(.)(-?\1){3}',card):#ci sono più di 3 ripetizioni consecutive
                print('Invalid')
            else:
                if len(card.replace('-','',4))==16:#ho tolto i trattini e controllo siano 16 numeri
                    print('Valid')
                else:
                    print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
        
        
        
 #Validating Postal Codes

regex_integer_in_range = r"^[0-9]{6}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"



 #Matrix Script
  
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
txt=''
for i in range(m):
    c_i=[row[i] for row in matrix] #accedo alla i-esima colonna della matrice
    string=''.join(c_i)
    txt=txt+string
    r=re.sub(r"(?<=\w)[!@#$%&\s]+(?=\w)"," ",txt)
print(r)



 #HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)   
    def handle_data(self,data):
        if data!='\n':
           print('>>> Data')
           print(data)    
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()



 #Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()
for i in range(int(input())):
     parser.feed(input())




 #Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(el[-10:-5],el[-5:])for el in l)
    return fun

  
  
  
#Decorators 2 - Name Directory

from operator import itemgetter

def person_lister(f):
    def inner(people):
       return( map(f, sorted(people, key=lambda p: int(p[2]))))
    return inner





#Arrays

def arrays(arr):
    arr.reverse()
    a=numpy.array(arr,float)
    return a
  
  
 
#Shape and Reshape

import numpy
lst=input().split()
arr=numpy.array(lst,int)
print(numpy.reshape(arr,(3,3)))



 #Transpose and Flatten

import numpy
n_m=input().split()
raw=[]
for i in range(int(n_m[0])):
    inp=input().split()
    raw.append(inp)
M=numpy.array(raw,int)
print(numpy.transpose(M))
print(M.flatten())



 #Concatenate

import numpy
n_m=input().split()
raw1=[]
raw2=[]
for i in range(int(n_m[0])):
    inp=input().split()
    raw1.append(inp)
M1=numpy.array(raw1,int)
for i in range(int(n_m[1])):
    inp=input().split()
    raw2.append(inp)
M2=numpy.array(raw2,int)
print(numpy.concatenate((M1,M2),axis=0))



 #Eye and Identity

import numpy
import numpy as np
n_m=input().split()
M=str(numpy.eye( int(n_m[0]) , int(n_m[1]),k=0 )).replace('0', ' 0').replace('1', ' 1')
print(M)



 #Sum and Prod

import numpy
n_m=input().split()
raw=[]
for i in range(int(n_m[0])):
    inp=input().split()
    raw.append(inp)
M=numpy.array(raw,int)
s=numpy.sum(M,axis=0)
print(numpy.prod(s))



 #Min and Max

import numpy
n_m=input().split()
raw=[]
for i in range(int(n_m[0])):
    inp=input().split()
    raw.append(inp)
M=numpy.array(raw,int)
mini=numpy.min(M,axis=1)
print(numpy.max(mini))



 #Mean, Var, and Std

import numpy
numpy.set_printoptions(sign=' ')
n_m=input().split()
raw=[]
for i in range(int(n_m[0])):
    inp=input().split()
    raw.append(inp)
M=numpy.array(raw,int)
print(numpy.mean(M,axis=1))
print(numpy.var(M,axis=0))
print(round(numpy.std(M),12))



 #Dot and Cross

import numpy

n=int(input())
raw_A=[]
raw_B=[]
for i in range(n):
    inp=input().split()
    raw_A.append(inp)
A=numpy.array(raw_A,int)
for i in range(n):
    inp=input().split()
    raw_B.append(inp)
B=numpy.array(raw_B,int)
#prodotto righe per colonne
print(numpy.dot(A,B))




 #Inner and Outer
  
import numpy
A=numpy.array(input().split(),int)
B=numpy.array(input().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))



 #Polynomials
  
import numpy
P=numpy.array(input().split(),float)
x=float(input())
print(numpy.polyval(P,x))



 #Linear Algebra

import numpy
n=int(input())
raw=[]
for i in range(n):
    raw.append(input().split())
A=numpy.array(raw,float)
print(round(numpy.linalg.det(A),2))


#Zeros and Ones

import numpy
shape=tuple(map(int,input().split()))
print(numpy.zeros(shape,dtype=numpy.int))
print(numpy.ones(shape,dtype=numpy.int))



 #The Minion Game
  
def minion_game(string):
    Stuart_score=0
    Kevin_score=0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            Kevin_score+=len(string)-i
        else:
            Stuart_score+=len(string)-i
    if Stuart_score>Kevin_score:
        print('Stuart', Stuart_score)
    elif Stuart_score<Kevin_score:
        print('Kevin', Kevin_score )
    else:
        print('Draw')
        

    
    
 #XML 1 - Find the Score

def get_attr_number(node):
    s=len(root.attrib)
    for child in root:
       s+=len(child.attrib)
       for subchild in child:
         s+=len(subchild.attrib)
    return s
  
  
  
  
#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem):
        level+=1
    if maxdepth<=level+1:
        maxdepth=level+1
    for child in elem:
        if len(child):
           depth(child,level) 
        
        
        
#Birthday Cake Candles

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    m=max(candles)
    return (candles.count(m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

    
    
    
 #Number Line Jumps

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1!=v2: #evito la divisione per zero
        k=int(abs((x1-x2)/(v1-v2)))
        if x1+v1*k==x2+v2*k: #stampa Yes se esite k intero t.c. x1+k*v1=x2+k*v2 
            return 'YES'
        else:
            return 'NO'
    else:
        if x1==x2: #se v1=v2 'YES ses x1=x2
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    
    
    
 #Athlete Sort

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sorted_arr=sorted(arr,key=lambda athlete: athlete[k])
    for el in sorted_arr:
        str_el = [str(a) for a in el]
        print(' '.join(str_el))
        
        
        
        
#ginortS

txt=input()
lower_letter=[]
upper_letter=[]
even_digit=[]
odd_digit=[]
for el in txt:
    if el.islower():
        lower_letter.append(el)
    elif el.isupper():
        upper_letter.append(el)
    elif int(el)%2==0:
        even_digit.append(el)
    else:
        odd_digit.append(el)
        
   

 #Insertion Sort - Part 1
  
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    k=arr[-1]
    j=n-2
    while(j>=0 and k<=arr[j]):
        arr[j+1]=arr[j]
        j=j-1
        str_arr=[str(el) for el in arr]
        print(" ".join(str_arr))
    arr[j+1]=k
    str_arr=[str(el) for el in arr]
    print(" ".join(str_arr))
    
if __name__ == '__main__':
    n = int(input()) 
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

    
    
    
#Insertion Sort - Part 2
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(n):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:  
            arr[j+1]=arr[j]
            j=j-1        
        arr[j+1]=k
        if i>0:
           str_arr=[str(el) for el in arr]
           print(" ".join(str_arr))   
            
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
    str_arr=[str(el) for el in arr]
    
    
    
    
#Viral Advertising

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    total_liked=0
    shared=5
    for i in range(1,n+1):
        liked=math.floor(shared/2)
        total_liked+=liked 
        shared=liked*3
    return total_liked        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()
















  
