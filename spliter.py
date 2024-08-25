# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:04:21 2020

@author: toranj
"""
def splitter(ip_string):
    from itertools import product
    length=len(ip_string)
    all_comb=list(product([0,1],repeat=length-1))
    for comb in all_comb:
        string_ =[ip_string]
        for i in range(length-2,-1,-1):
            if comb[i]==1:
                save=string_[0]
                del string_[0]
                string_ .insert(0,save[i+1:])
                string_ .insert(0,save[:i+1])
        yield string_
def check_ip(ip_string):
    if len(ip_string)>3:
        return False
    if not int(ip_string[0]) and len(ip_string)>1:
        return False
    if int(ip_string)>=255:
        return False
    return True
def noghte_shomar(ip_string):
    m=0
    for i in ip_string:
        if i=='.':
            m+=1
    return m
a=input('')
m=[]
for i in splitter(a):
    l=[]
    for j in i:
        if check_ip(j):
            l.append(j)
    m.append(l)
for i in range(len(m)):
    for j in range(len(m[i])-1):
        m[i][j]+='.'
for i in range(len(m)):
    m[i]=''.join(m[i])
ip=[]
for i in range (len(m)):
    if len(m[i])==len(a)+3:
        if noghte_shomar(m[i])==3:
            ip.append(m[i])
ip.sort()
for i in ip:
    print(i)

