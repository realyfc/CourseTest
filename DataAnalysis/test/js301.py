# coding: utf-8

# * Write a function 'what_sign' which returns 'Positive' 'Zero' or 'Negative' when given a number.

# In[11]:

def what_sign(n):
    if n > 0:
        return 'Positive'
    elif n < 0:
        retur
        'Negative'
    else:
        return 'Zero'


what_sign(3)
what_sign(0)
what_sign(-3)


# * Write a function 'fizzbuzz' that returns the integers from 1 to n. 
#  - But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#  - For numbers which are multiples of both three and five print "FizzBuzz".

# In[1]:

def fizzbuzz(n):
    msg = []
    for num in range(1, n + 1):
        if num % 3 == 0:
            msg.append('Fizz')
        if num % 5 == 0:
            msg.append('Buzz')
        else:
            msg.append(num)
    return msg


fizzbuzz(100)


# * Write a function 'remove_indices' which removes one or more indicies from a list.
#  - For example given the list:
# ["John", "Bob", "Charles", "Trev"]
# and the indices:
# [1, 2]
# the resulting list will be:
# ["John", "Trev"]

# In[ ]:

def remove_indices(mylist, idxs):
    result = []
    for i, l in enumerate(mylist):
        if i not in idxs:
            result.append(l)
    return result


# In[ ]:

remove_indices(["John", "Bob", "Charles", "Trev"], [0])

# In[ ]:

remove_indices(["John", "Bob", "Charles", "Trev"], [1, 2])
