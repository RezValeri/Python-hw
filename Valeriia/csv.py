#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
def csv_py(file,d):
    if file not in os.listdir(path="."):
        print("Error. File with this name doesn't exist")
    else:
        with open(file,'r') as f:
            l1=[]
            for i in f:
                l2=[]
                s=0
                for n in i:
                    if n==d:
                        if s: 
                            l2.append(d)
                        else:
                            l2.append(' ')
                    elif n=='"':
                        s=(s+1)%2
                    else:
                        l2.append(n)
                l1.append(''.join(l2).split())
        return l1


def py_tsv(file,frame,d):
    with open(file,'w') as f:
        for i in frame:
            f.write(d.join(i)+"\n")
            
res=csv_py("book2.csv", ',')
print(res)
res2=py_tsv('book2.csv',res,',')

