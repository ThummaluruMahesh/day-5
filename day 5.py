'''
# ! -----> common function for list

l1 = [6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))
'''
'''
l1 = [6,7,8,9,"p", "u"]
print(max(l1)) # ---> error coz its a combination of int and string
print(min(l1)) # ---> error coz its a combination of int and string
'''
'''
l1 = [6,7,8,9,0, 8.89, -5, 0.78]
index() --> to get index value of specific element
print(l1.index(9))
'''
'''
l1 = [6,6,6,7,8,9,0, 8.89, -5, 0.78]
# count() --> how meny non of times an element is repeated
print(l1.count(6))

3
'''


# ! some functions which is specifically used for list
'''
# To add element inside list
# ! insert(index_value, element) --> to add element at specific index position
l1 = [6,6,6,7,8,9,0, 8.89, -5, 0.78]
l1.insert(2,"cars")
print(l1)

[6, 6, 'cars', 6, 7, 8, 9, 0, 8.89, -5, 0.78]

'''
'''
# to delete element from list
l1 = [6,6,6,7,8,9,0, 8.89, -5, 0.78]
# pop () --->alt element will be deleted
l1.pop()
print(l1)

[6, 6, 6, 7, 8, 9, 0, 8.89, -5]

'''

# pop(index_value) --> used to delete element at specific index
'''
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
l1.pop(4)
print(l1)

[6, 6, 6, 7, 9, 0, 8.89, -5, 0.78]
'''

# remove(element) --> used to delete element directly
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.remove(6.76)
print(l1)

[2, 3, 2, 3, 4, 32, 98.5, -94]
'''
# clear() --> to complete delete all element in list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.clear()
print(l1)

[]
'''


# del -> to delete the list
# del l1 # or del(l1)
# print(l1)

# ? join 2  lists
'''
l1 = [9, 0, 8]
l2 = ["p", "0", "t", 34]
print(l1+l2)

[9, 0, 8, 'p', '0', 't', ]
'''

# ! or

# * extend() --> to combine 2 lists
'''
l1 = [9, 0, 8]
l2 = ["p", "0", "t", 34]
l1.extend(l2)
print(l1)

[9, 0, 8, 'p', '0', 't', 34]
'''

# ? -----> copy()
'''
l1 = [6,7,8,9,3]
l2 = l1.copy()
print(l2)
print(l1)

[6, 7, 8, 9, 3]
[6, 7, 8, 9, 3]

'''

# ! diff between shallow copy and  deep copy
#shallow copy
'''
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

[8, 9, 0, [5, 6], [3, 2, 1], 890]
[8, 9, 0, [5, 6], [3, 2, 1]]
'''

# * deep copy
'''
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])---> to index nested value
'''
'''
l2 = copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''

# ? sort --> arrange elements in list in ascending or descending order
'''
l1 = [9,7, 45,0,-6,5,12]
l1.sort()  # to arrenge in ascending order
print(l1)

[-6, 0, 5, 7, 9, 12, 45]
'''

'''
l1 = ['z','i','o','p',9]
l1.sort()
print(l1) # --> error
'''

# ? list constructor
# * list() --> to cover other collection datatype to list
'''
l3 = ((8, 9,0))
print(list(l3))

[8, 9, 0]

'''
'''
l4 = (8,9)
print(list(l4))

[8, 9]

'''

# ! ---> nested list
'''
l1 = [8,9,[0,8,7],["p","o","y"],[8, 't']]
print(l1[-2][1])

o

'''
'''
l1 = [8,9,[0,8,7],["p","o","y"],[8, 't']]
print(l1[1:4])
print(l1[1:-1])
[9, [0, 8, 7], ['p', 'o', 'y']]
[9, [0, 8, 7], ['p', 'o', 'y']]

'''

# ? to delete "t" from l1
'''
l1[-1].remove('t')
print(l1)
'''
# ? combine these ["o", "o", 'y'], [8,'t'] lists in l1 to ["p","o",'y',8,'t']
'''
l1=["p","o",'y']
l2=[8,'t']
l1.extend(l2)
print(l1)

['p', 'o', 'y', 8, 't']
'''

# ! -------> Tuple
# * char of tuple

#1.) Tuple have to surrounded by ()
#2.) The elements inside tuple are not changeble
#3.) The element inside4 tuple are indexed$
#4.) The element will execute in order
#5.) It is heterogenous
#6.) It allow duplicate elements

# Eg:
'''
t1 = ( 8,8,9,6,5.78,[9,0],(6,8), "hey", 9+6j)
print(t1)
print(type(t1))

(8, 8, 9, 6, 5.78, [9, 0], (6, 8), 'hey', (9+6j))
<class 'tuple'>
'''
# ? indexing, slicing are all same as list
'''
l1 = [8]
print(type(l1)) #int

<class 'list'>
'''
'''
l1 = [8]
print(type(l1))# tuple


t1 = 8,9
print(type(t1))# tuple

t2 = 8,
print(type(t2))# tuple

<class 'list'>
<class 'tuple'>
<class 'tuple'>

'''

#len(),min(),max(),index(),count()--->all same as list

# to add element inside tuple ---> cannot add
# cannot delete any element from tuple

# * join 2 tuples
'''
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)

(8, 9, 0, 6, 7, 8)

'''

# * To add all element inside list and tuple
#3sum()
'''
l1 =(8,9,7,6)
print(sum(l1))

30
'''
# * sort tuple
'''
t1 = (8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=true)))
'''

# ? Iterate list and tuples 

# * Iterate based on elements
'''
l1 = [9,8,0,6,5]
for i in l1:
    print(i)

9
8
0
6
5
'''

# * Iterate based on index value
'''
l1 = [9,8,0,6,5,8,56]
for i in range (0,len(l1)):
    print(l1[i])
    
9
8
0
6
5
8
56
'''

# ! ----> strings
'''
s1 = 'o'
print(type(s1))
<class 'str'>
'''
'''
s1 = 'u'
print(type(s1))
<class 'str'>
'''

s1 = "hello world"
# * To access string
'''
print(s1)
hello world
'''
# indexing and slicing ---> same as list and tuple
'''
print(s1[0:5])
hello
'''

# ---> common functions
#len(), min(), max(), index(), count()
'''
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))

11
w
 '''

# ord() ---> used to find the ASCII value of a character
'''
s1 = 'u'
print(ord(s1))

117 
'''
# functions of string
'''
s1 = "hello world"
# ? to convert all characters to upper case
print(s1.upper())

HELLO WORLD
'''

# ? to convert to lower case
'''
s1 = "HEREDGi0ou"
print(s1.lower())

heredgi0ou

'''

# strip() --> to eliminate the space in beginning  and end of string
'''
s1 = " where are  you ?"
print(s1.lstrip()) --> at beginning
print(s1.rstrip()) --> at end
print(s1.strip())

where are  you ?
'''

# split() -->
'''
s1 = "where  are you?"
print(s1.split(" "))
print(s1.split("r"))
print(s1.split("e"))

['where', '', 'are', 'you?']
['whe', 'e  a', 'e you?']
['wh', 'r', '  ar', ' you?']
'''

# * replace () ---> to replace a specific char in the string
'''
s1 = "where are you?"
print(s1.replace('r', '&&'))
whe&&e a&&e you?

'''

# * swapcase() ---> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
hey THERE
'''

# title() --> to erite the string in format of title
'''
s1='never give up'
print(s1.title())

Never Give Up
'''
# jion the strings
'''
s1='hello'
s2='world'
print(s1+s2)

helloworld
'''

s1 = '''
how are you
i am fine
hey there
'''
'''
c = 0
for val in s1:
    if val =='\n':
        c+=1
        print(c)

1
2
3
4
'''

# find() --> to find the index based on a character
'''
s1 = "hello world"
print(s1.find('h'))
print(s1.index('h'))
'''
'''
s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))
'''

# * join() -->
'''
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".join(l1))

hey there
hey$there
'''
'''
s1 = "welcome to all"
print(s1.endswith('l'))
print(s1.startswith('w'))

True
True
'''
'''
s1 = "67"
print(type(s1))
print(s1.isdigit())

<class 'str'>
True     
'''

# * print the string in reverse manner
'''
s1 = "welcome to all"
print(s1[::-1])

lla ot emoclew
'''

# ! ----> Eg:1
# wap to find the number of lower case letters
'''
s1 = "HEY there you aRE"
count=0
for i in s1:
    print(i)
for i in s1:
    if i.islower():
        count+=1
        print("The total num of lower case letters: ",count)

The total num of lower case letters:  9
'''


# ! -----> Eg":2 r--> "$"
'''
s1 = 'restarter'
print(s1[0] + s1[1:].replace('r','$'))
resta$te$
'''

s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop p"
'''
character = len(s1)
print(character)
500
'''
'''
words = s1.split(" ")
print(words)

['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry.', 'Lorem', 'Ipsum', 'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s,', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book.', 'It', 'has', 'survived', 'not', 'only', 'five', 'centuries,', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting,', 'remaining', 'essentially', 'unchanged.', 'It', 'was', 'popularised', 'in', 'the', '1960s', 'with', 'the', 'release', 'of', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages,', 'and', 'more', 'recently', 'with', 'desktop', 'p']
'''
'''
words = s1.split(" ")
print(len(words))
82
'''
'''
sentenses = s1.split('.')
for val in sentenses:
    if val ==' ':
        index = sentenses.index(' ')
        sentenses.pop(index)
print(len(sentenses))

4
'''
'''
space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)

'''

# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]











