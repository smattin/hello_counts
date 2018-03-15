
# coding: utf-8

# In[ ]:

# function that counts the number of occurences of each character in a string
# 'hello' -> 'h' - 1; 'e' - 1; 'l' - 2; 'o' - 1


# In[5]:

def counts(s):
    answer = {}
    for c in s:
        if c in answer.keys():
            answer[c] = answer[c]+1
        else:
            answer[c] = 1
    ret = '{} -> '.format(s)
    for c in answer:
        ret = ret +"'{}' - {}; ".format(c,answer[c])
    return ret


# In[6]:

print(counts('hello'))


# In[ ]:



