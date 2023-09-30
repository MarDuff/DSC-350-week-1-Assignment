#!/usr/bin/env python
# coding: utf-8

# ## Data Wrangling with Pandas

# In[2]:


#import libraries
import pandas as pd


# ### Point 1

# In[ ]:


#a) Read each file in.
#b)Add a column to each dataframe indicating the ticker it is for.
#c) Append them together into a single dataframe.
#d)Save the result to a CSV file.


# In[13]:


faang = pd.DataFrame()
for ticker in ['fb', 'aapl', 'amzn', 'nflx', 'goog']:
    df = pd.read_csv(f'/Users/maduffaut/Desktop/ch3_files/{ticker}.csv')
    
# make the ticker the first column
    df.insert(0, 'ticker', ticker.upper())
    faang = faang.append(df)

faang.to_csv('faang.csv', index=False)


# In[14]:


faang.head()


# ### Point 2

# In[65]:


#With faang, use type conversion to cast the values of the date column into datetimes 
#and the volume column into integers. Then, sort by date and ticker


# In[19]:


faang = faang.assign(
    date=lambda x: pd.to_datetime(x.date),
    volume=lambda x: x.volume.astype(int)).sort_values(['date', 'ticker'])

faang.head()


# ### Point 3

# In[16]:


#Find the seven rows in faang with the lowest value for volume

faang.nsmallest(7, 'volume')


# ### Point 4

# In[18]:


#the data is somewhere between long and wide format. 
#Use melt()to make it completely long format

melted_faang = faang.melt(id_vars=['ticker', 'date'], 
    value_vars=['open', 'high', 'low', 'close', 'volume'])

melted_faang.head()


# ### Point 4

# In[20]:


#Suppose we found out that on July 26, 2018 there was a glitch in how the data was recorded.
#How should we handle this?


# #### 
# Given that this is a large data set (~ 1 year), 
# we would be tempted to just drop that date and use interpolation (technique in Python used to estimate unknown data points between two known data points. Interpolation is mostly used to impute missing values in the dataframe or series while pre-processing data.) 
# 
# However, some preliminary research on that date 
# for the FAANG stocks reveals that FB took a huge tumble that day. 
# If we had interpolated, we would have missed the magnitude of the drop.
# 
