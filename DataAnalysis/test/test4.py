# coding: utf-8

# 1.creating lists.
# 
# ```python
# a='A'
# b='B'
# c='C'
# x = list()
# ```
# add a, b, c into x and print the length of x.

# In[2]:

def create_list():
    """Create a list."""
    a = 'A'
    b = 'B'
    c = 'C'
    x = list()
    x.append(a)
    x.append(b)
    x.append(c)
    return x


# In[3]:

create_list()


# 2.selecting from lists. Given the list x
#  - return the first item.
#  - return the last item.
#  - return the x reversed using indexing.

# In[ ]:

def select_first_item(x):
    """Return first item."""
    return x[0]


def select_last_item(x):
    """Return first item."""
    return x[-1]


def select_reversed(x):
    """Return list reversed."""
    return x[::-1]


# In[13]:

x = ['A', 'B', 'C']
select_first_item(x)

# In[14]:

select_last_item(x)

# In[15]:

select_reversed(x)


# 3.selecting first items. Given the following:
# ```python
# x = [('A','x'), ('B','y'), ('C','z')]
# ```
# return
# ```python
# ['A','B','C'].
# ```

# In[19]:

def select_first_items(x):
    """Select first item on each list."""
    return [v[0] for v in x]


# In[18]:

x = [('A', 'x'), ('B', 'y'), ('C', 'z')]
select_first_items(x)


# 4.add 5 to values. Given the following:
# ```python
# x = [1, 10, 20]
# ```
# return a list with 5 added to the numbers i.e. 
# ```python
# [6, 15, 25].
# ```

# In[23]:

def add_5_to_values(x):
    """Return the list with 5 added to each value."""
    return [v + 5 for v in x]


# In[24]:

x = [1, 10, 20]
add_5_to_values(x)


# 5.divisible by 5. Given the following:
# ```python
# x = [1, 10,  15, 3, 12, 15, 25, 50]
# ```
# return a list with only numbers divisible by 5 (% modulo operator)

# In[25]:

def get_divisble_by_5(x):
    """Return elements that are divisble by 5."""
    return [v for v in x if v % 5 == 0]


# In[26]:

x = [1, 10, 15, 3, 12, 15, 25, 50]
get_divisble_by_5(x)


# 6.merge_lists. Given the lists:
# ```python
# x = ['A', 'B', 'C']
# y = ['x', 'y', 'z']
# ```
# create the following list:
# ```python
# [('A','x'), ('B','y'), ('C','z')].
# ```

# In[27]:

def merge_lists(x, y):
    """Returns pairs from each list."""
    x = ['A', 'B', 'C']
    y = ['x', 'y', 'z']
    return list(zip(x, y))


# In[28]:

x = ['A', 'B', 'C']
y = ['x', 'y', 'z']
merge_lists(x, y)


# 7.transpose(). Create a function that takes a list of lists and returns the transpose. So given:
# ```python
# [
#     [1, 2, 3],
#     ['A', 'B', 'C'],
# ]```
# We would expect:
# ```python
# [
#     [1, 'A'],
#     [2, 'B'],
#     [3, 'C'],
# ]```
# In the case of uneven length lists choose then truncate to the shortest, so given:
# ```python
# [
#     [1, 2, 3],
#     ['A', 'B'],
# ]```
# We would expect:
# ```python
# [
#     [1, 'A'],
#     [2, 'B'],
# ]```
# Hint: There is a builtin function zip that can help you.
# 

# In[30]:

def transpose_easy(list_of_lists):
    """Transpose  a list of lists."""
    # Gotcha: zip returns a list of tuples, we want a list of lists
    return [list(v) for v in zip(*list_of_lists)]


# In[32]:

list_of_lists = [[1, 2, 3], ['A', 'B', 'C'], ]
transpose_easy(list_of_lists)


# 8.list rotation.Rotate a list by taking the value from one end a putting it on the other end.
# Create two functions rotate_left() and rotate_right() that modify a list in place as follows, given the list 
# ```python
# ['A', 'B', 'C']:
# ```
# rotate_left() changes it to 
# ```python
# ['B', 'C', 'A']
# ```
# rotate_right() changes it to 
# ```python
# ['C', 'A', 'B']
# ```

# In[33]:

def rotate_left(alist):
    """Rotates a list to the left so that the first item appears at the end."""
    if len(alist):
        alist.append(alist.pop(0))


def rotate_right(alist):
    """Rotates a list to the right so that the last item appears at the beginning."""
    if len(alist):
        alist.insert(0, alist.pop())


# In[35]:

alist = ['A', 'B', 'C']
rotate_left(alist)
alist

# In[36]:

alist = ['A', 'B', 'C']
rotate_right(alist)
alist
