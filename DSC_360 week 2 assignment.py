#!/usr/bin/env python
# coding: utf-8

# ## Point 1

# In[107]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib as plt
import sys
from datetime import datetime 


# In[10]:


#add 2 vectors using Numpy 
def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c


# In[17]:


#adding two vectors using Python

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c


# In[110]:


size = 250


# In[111]:


start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)


# In[112]:


start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)


# ## Point 2/plot with matplotlib

# In[26]:


from sklearn.datasets import load_iris
from matplotlib import pyplot as plt


# In[23]:


#print infos fron Iris dataset with matplolib
iris = load_iris()
print(iris.DESCR)


# In[31]:


data=iris.data
plt.xlabel("sepal lengh")
plt.ylabel("sepal width")
plt.plot(data[:,0],data[:,1],".")
plt.show()


# ## Point 3

# In[41]:


#import data from library
#from sklearn.datasets import load_boston?NOT WORKING
import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
print(data)


# In[43]:


#plot data with matplotlib
plt.xlabel("% of non-retail business")
plt.ylabel("nitric oxide concentration")
plt.plot(data[:,3],data[:,5],"+")
plt.show()


# ## Point 4

# In[45]:


#Create a multi-dimensional array
m = np.array([np.arange(4), np.arange(4)])
m


# ## Point 5

# In[46]:


#Produce an array of single precision floats
np.arange(5, dtype='f')


# ## Point 6

# In[47]:


#Produce an array of complex numbers
np.arange(5, dtype='D')


# ## Point 7

# In[48]:


#slicing and indexing arrays
#define an array containing the numbers 0, 1, 2, and so on up to and including 8
a = np.arange(9)
a


# In[49]:


# select a part of the array from indexes 3 to 7
a[3:7]


# In[50]:


#choose elements from an index of 0 to 7 with an increment of 2
a[:7:2]


# In[51]:


#use negative indices and reverse the array
a[::-1]


# ## Point 8/ Arrays shapes

# In[63]:


#create an array
a= np.arange(12).reshape(2,3,2)
print(a)


# In[65]:


#Ravel
a
a.ravel()


# In[66]:


#flatten
a.flatten()


# In[70]:


#Setting the shape with a tuple
a.shape=(3,4)
a


# In[71]:


#Transpose
a.transpose()


# In[74]:


#Resize
a.resize(2,6)
a


# ## Point 9/Array Attributes in Numpy

# In[81]:


#crate an array
a= np.arange(9)
a


# In[113]:


#number of dimensions
a.ndim


# In[86]:


a=np.arange(9).reshape(3,3)
a


# In[87]:


a.ndim


# In[89]:


#Count of elements
b=np.arange(10).reshape(2,5)
b


# In[90]:


b.size


# In[94]:


#Count of bytes
b.itemsize


# In[96]:


#Full count of bytes
b.nbytes


# In[97]:


b.nbytes*b.itemsize


# ## Point 10/Converting arrays

# In[100]:


#convert an array to a Python list 
m=np.arange(12).reshape(3,4)
m


# In[101]:


m.tolist()

