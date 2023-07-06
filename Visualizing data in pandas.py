#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[22]:


df = pd.read_excel("D:\pandas\ice cream ratings.xlsx")
df = df.set_index('Date')
df


# In[50]:


print(plt.style.available)
plt.style.use('seaborn-notebook')


# In[25]:


df.plot(kind = 'line')


# In[26]:


df.plot(kind = 'line', subplots = True)


# In[28]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel='Daily Ratings', ylabel='Scores')


# In[31]:


df['Flavor Rating'].plot(kind = 'bar', stacked = True)


# In[33]:


df.plot(kind = 'bar', stacked = True)


# In[34]:


df.plot.barh(stacked=True)


# In[39]:


df.plot.scatter(x='Texture Rating', y='Overall Rating' ,s =300 , c='green')


# In[43]:


df.plot.hist(bins= 10)#good for showing distribution for variables


# In[44]:


df.boxplot()


# In[46]:


df.plot.area(figsize = (10,4))


# In[48]:


df.plot.pie(y='Flavor Rating', figsize=(10,9))


# In[ ]:




