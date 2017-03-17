# coding: utf-8

# * Write a function 'what_sign' which returns 'Positive' 'Zero' or 'Negative' when given a number.

# In[ ]:

def what_sign(n):
    if n > 0:
        return 'Positive'
    elif n < 0:
        return 'Negative'
    else:
        return 'Zero'


what_sign(3)
what_sign(0)
what_sign(-3)


# * Write a function 'fizzbuzz' that prints the integers from 1 to 100. 
#  - But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#  - For numbers which are multiples of both three and five print "FizzBuzz".

# In[ ]:

def fizzbuzz():
    for num in range(1, 101):
        msg = ''
        if num % 3 == 0:
            msg += 'Fizz'
        if num % 5 == 0:
            msg += 'Buzz'
        else:
            msg = str(num)
        print(msg)


fizzbuzz()


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
