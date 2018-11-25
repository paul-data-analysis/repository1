
# coding: utf-8

# Import pandas and numpy libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# Import 'changes' file - some 'comment' columns have not been cleansed correctly and extend over addditional columns. Actual comments made do not appear to be important or rather their 'interestingness' is deemed low. So I have only imported columns A-F from 'changes.csv' 
# 

# In[60]:


df = pd.read_csv('changes.csv', usecols=[0,1,2,3,4,5])


# In[61]:


df.head()


# Author appears to have some unuseful data included in the data frame.

# In[62]:


df.describe()


# Create a new variable for plotting authors and number of revisions.

# In[63]:


auth_rev = df.groupby(["author"]).count()["revision"]
auth_rev


# Author with name "/OU=Domain Control Validated/CN=svn.company.net" is not useful for insightfulness so I am going to remove it from auth_rev

# In[64]:


auth_rev = auth_rev.drop(labels = ['/OU=Domain Control Validated/CN=svn.company.net'])


# In[65]:


auth_rev.plot(kind = 'bar', title = 'Number of Revisions by Author', rot = 45, ).set(xlabel = 'Authors', ylabel = 'No. of Revisions')


# INTERESTINGNESS 1:
# This is interesting as it shows us that 2 staff members - Thomas and Jimmy - are highly active in making revisions. We can also see that Vincent has just over 25 commits while everyone else has less than 10 entries.

# In[66]:


# new data frame with split value columns 
newtime = df["time"].str.split(":", n = 3, expand = True) 
 
# making seperate column for hours 
df["hour"]= newtime[0] 
 
# making seperate column for minutes
df["minute"]= newtime[1] 
 
# making seperate column for seconds 
df["seconds"]= newtime[2]

df = df.sort_values(by=['hour','minute'])
# df display 
df


# In[70]:


# new data frame with split value columns 
newdate = df["date"].str.split("/", n = 3, expand = True) 
 
# making seperate column for days 
df["day"]= newdate[0] 
 
# making seperate column for months
df["month"]= newdate[1] 
 
# making seperate column for years 
df["year"]= newdate[2]

df = df.sort_values(by=['year','month', 'day', 'hour', 'minute'])
# df display 
df


# Replace author with user domain name to 'Unknown_Employee'

# In[71]:


df['author'] = df['author'].replace('/OU=Domain Control Validated/CN=svn.company.net' ,'Unknown_Employee')


# In[72]:


df[['hour', 'minute', 'seconds']] = df[['hour', 'minute', 'seconds']].apply(pd.to_numeric)
df[['day', 'month', 'year']] = df[['day', 'month', 'year']].apply(pd.to_numeric)

df.dtypes


# In[149]:


rev_time = df.groupby(['month']).count()["revision"]
rev_time.head()


# In[131]:


rev_time.plot(kind = 'bar', x='month', rot = 1, y='revision',figsize = (10,5), title = 'Count of Revisions per Month')


# In[178]:


auth_date = df.groupby(['author']).agg({'month': [min, max]})
auth_date.head(12)


# In[196]:


#f, ax = plt.subplots
auth_date.plot(kind = 'barh', legend = False,figsize = (10,5),title = 'Employees present over the period', xticks = ([7,8,9,10,11,12]), xlim = (6,11))


# Interestingness #2:
# We can see from the above analysis, the number of of commits was very low in September in comparison to the other months. From the above graph we can see authors who were present from July to November - blue bar representing the month the employee logged the first commit and the orange representing the month they logged their last commit.
# 
# Thomas and Jimmy were present in the organisation for the entire period under review so it is not surprising they have the most commits logged. Dave was also present in the organisation for the entire review period. Records show he has only logged 2 commits during the period of review. His productivity may be something that needs attention.

# In[238]:


hours = sns.catplot(kind = 'boxen', x = 'hour', y = 'author', data = df, hue = 'author', legend = False, ci=None, height = 7, aspect = 1.5)
hours.set_axis_labels("Hours of Day", "Author")


# Interestingness #3:
# From the above analysis of concentration of commits throughout the workday, we can see:
# > Vincent is appears to be logging the longest days, with commits occurring from early morning through to late evening.
# 
# > Thomas and Jimmy while having logged the most commits over the period, are doing so during the standard working day of 8am - 6pm.
# 
# > Dave's work day tends to start after 10am and finishes around 7pm which is not unusal in itself however we know from previous analysis he has only 2 commits logged for the review period so we cannot perform a full analysis of his daily productivity yet. Dave may have some issues with his time management or might not be involved in logging commits as part of his normal job. Further information on Dave would be required to arrive at any conclusion.
