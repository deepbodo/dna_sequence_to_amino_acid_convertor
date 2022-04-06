#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DNA={}


# In[61]:


str1=input("Enter your DNA sequence: ")    
str2 = str1.replace(' ','')
n = 3
out = [(str2[i:i+n]) for i in range(0, len(str2), n)]

DNA1={
    "TTT":"F","CTT":"L","ATT":"I","GTT":"V","TTC":"F","CTC":"L","ATC":"I","GTC":"V","TTA":"L","CTA":"L","ATA":"I","GTA":"V",
    "TTG":"L","CTG":"L","ATG":"M","GTG":"V","TCT":"S","CCT":"P","ACT":"T","GCT":"A","TCC":"S","CCC":"P","ACC":"T","GCC":"A",
    "TCA":"S","CCA":"P","ACA":"T","GCA":"A","TCG":"S","CCG":"P","ACG":"T","GCG":"A","TAT":"Y","CAT":"H","AAT":"N","GAT":"D",
    "TAC":"Y","CAC":"H","AAC":"N","GAC":"D","CAA":"Q","AAA":"K","GAA":"E","CAG":"Q","AAG":"K","GAG":"E","TGT":"C","CGT":"R",
    "AGT":"S","GGT":"G","TGC":"C","CGC":"R","AGC":"S","GGC":"G","CGA":"R","AGA":"R","GGA":"G","TGG":"W","CGG":"R","AGG":"R",
    "GGG":"G","TAA":"","TGA":""
}
l=[DNA1[x] for x in out]

print(" Amino Acid Sequence is:",''.join(l))


# In[ ]:





# In[15]:



def remove_spaces(str1):
    str1 = str1.replace(' ','')
    return str1
str1=input()    
print(remove_spaces(str1))


# In[33]:


s=input()
print(s)


# In[35]:


s=input()
b=len(s)
print(b)


# In[ ]:


p = {}
for k,v in DNA1.items():
    for i in out:
        if i==k:
            p[k] = 

