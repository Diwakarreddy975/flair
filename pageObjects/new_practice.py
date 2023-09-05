# generate an infinite fibnocci series using generator
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# f=fib()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
import collections
import string

# sort a list without using sort keyword
# l=[22,1,32,47,87,6,46,6,52]
# n=len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
#
# print(l)

# sort a dictionary by using dict comprehension
# d={200:"apple",899:"pineapple",500:"dragon fruit",50:"banana",1000:"cashew"}
# way-1
# a=sorted(d.keys())
# print(a)
# s={}
# for i in a:
#     s[i]= d[i]
# print(s)

# way-2
# a=sorted(d.items())
# print(a)

# way-3
# d={key:value for key,value in sorted(d.items())}
# print(d)


# # print all pairs which are equal to given sum
# l=[2,4,3,1,5,8,6,7,9]
# k=13
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#             if (l[i]+l[j]==k):
#                 print(l[i],l[j])


#fib series using recursion function

# def fun(n):
#     if n <=1:
#         return 1
#     else:
#         return fun(n-1)+fun(n-2)
#
# for i in range(10):
#     print(fun(i))



# result="blue is sky the"
# S=""

# for i in s:
#     if i.isalpha():
#          S +=i
#     else:
#         l.append(S)
#         S=""
# l.append(S)
# a=" ".join(reversed(l))
# print(a)
#
# with split//
# a=s.split()
# print(" ".join(a[::-1]))



# remove punctuations
# s="@hlo hyd, how are you.. // if this ha&*(ns."
# a=""
# for i in s:
#     if ((i>='A' and i<='Z') | (i>='a' and i<='z')|(i==" ")):
#         a +=i
# print(a)

# s="@hlo hyd, how are you.. // if this ha&*(ns."
# a=collections.defaultdict(int)
# for i in s:
#   a[i] +=1
# print(dict(a))



# find max min values in a given list
# l=[2,4,3,1,5,8,6,7,9]
# max=0
# min=0
# for i in range(len(l)):
#   for j in range(i+1,len(l)):
#     if l[i]>l[j]:
#       l[i],l[j]=l[j],l[i]
#     max=l[-1]
#     min=l[0]
# print(max,min)


# raise exception if u found 1 in list
# l=[2,4,3,1,5,8,6,7,9]
# for i in l:
#   if i==1:
#     raise Exception("1 found in the list")


#find common characters within two strings
#
# s1="sdfgrfvbn"
# s2="wscftyh"
# way-1
# S1=set(s1)
# S2=set(s2)
# a=S1.intersection(S2)
# print(a)

# way -2
# a=[]
# for i in s1:
#     if i in s2:
#         if i not in a:
#             a.append(i)
#
# print(a)

# s="how are you i am fine how about you were are you staying"
#
# l=s.split(" ")
# d=collections.defaultdict(int)
# for i in l:
#
#         d[i] +=1
# print(dict(d))

# convert two lists into dict
# l=[2,5,4,1,7]
# l1=["B","E","D","A","G"]
# d={key:value for key,value in zip(l,l1)}
# print(d)
# way-2
# d={}
# for i in range(len(l)):
#      d[l[i]]=l1[i]
# print(d)

# count total vowels in given string
# s="how are you i am fine how about you were are you staying"
# count=0
# for i in s:
#     if i  in "aeiouAEIOU" :
#         count += 1
# print(count)

# count occurence ov each vowel:
# d=collections.defaultdict(int)
# for i in s:
#     if i in "AEIOUaeiou":
#         d[i]+=1
# print(sorted(dict(d).items()))

# count unique characters
# a=collections.Counter(s)
# print(dict(a))

#
# return words starts with uppercase
# s="Hello  welcomes to USA , Kilo kilkim Jios "
#
# l=s.split()
# a=[]
# for i in l:
#   if i[0].isupper():
#       a.append(i)
# print(a)

# print first letter of each word
# s="Hello  welcomes to USA , Kilo kilkim Jios "
#
# l=s.split()
# for i in l:
#     print(i[0],end=" ")

# fetch first and last character of each word
# s="Hello welcomes to USA,Kilo kilkim Jios "
# l=s.split()
# for i in l:
#     print("first char",i[0],"last char",i[-1])

# s="hai jai shree ram jai shree ram raja ram"
# l=s.split()
# a=" "
# for i in l:
#     a+=i[0].upper()+i[1:].lower()+" "
# print(a)

# d={200:"apple",899:"pineapple",500:"dragon fruit",50:"banana",1000:"cashew"}
# a={key:value for value,key in d.items()}
# print(a)

# l=[3,5,4,2,1,12,78]
# l=[x*x for x in l if x%2==0]
# print(l)


# reverse the items in a string
# d={200:"apple",899:"pineapple",500:"dragon fruit",50:"banana",1000:"cashew"}
# l=list(d.items())
# print(l)
# l.reverse()
# q={}
# for k,v in l:
#     q[k]=v
# print(q)

# data = {
#
#    "key1": {"key11": {"key111": {"key1111": 1}}},
#
#    "key2": {"key22": {"key222": 2}},
#
#    "key3": {"key33": 3},
#
#    "key4": 4
#
# }
#
# def foo(data):
#     a = []
#     for key,value in data.items():
#         if isinstance(value,dict):
#             a.extend(foo(value))
#         else:
#             a.append(value)
#     return a
#
# print(foo(data))

# q='kmjn vicujikce voireos vndow fewsdfv njk,mn,mkjhgfd'

import os

# print(os.rename(r"C:\Users\91789\PycharmProjects\flair\pageObjects\practice.py",r"C:\Users\91789\PycharmProjects\flair\pageObjects\new_practice.py"))

# edfggtrdxde

















































































