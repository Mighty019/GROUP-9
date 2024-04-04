#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #used for array
import pandas as pd #used for tables
import matplotlib.pyplot as plt # helps in to viusalize the charts
import seaborn as sns # perform the same fuction as metplotlib


# In[2]:


dl=pd.read_csv("C:\\Users\\Lenovo\\Desktop\\deliveries.csv")


# In[3]:


dl.head()


# In[4]:


#  dl.loc[dl['penalty_runs']==0].sum()


# In[5]:


dl.info() #provide the info and data type also


# In[6]:


dl.columns #used to check the name of the columns


# In[7]:


dl.shape #shows the number of rows and coulmn


# In[8]:


for col in dl:
    print(dl[col].unique())


# In[9]:


dl.describe() #gives the info about stats calc


# In[10]:


dl["match_id"].unique #fetch the unique values


# In[11]:


dl.isnull() #shows the missing values


# In[12]:


dl.isnull().sum() #sum of missing values


# In[13]:


dl['player_dismissed']=dl['player_dismissed'].fillna('No')


# In[14]:


dl['dismissal_kind']=dl['dismissal_kind'].fillna('Not found')


# In[15]:


dl['fielder']=dl['fielder'].fillna('No')


# In[16]:


dl.isnull().sum()


# In[17]:


print(len(dl['batsman']))
len(dl['batsman'].unique())


# In[18]:


print(len(dl['bowler']))
len(dl['bowler'].unique())


# In[19]:


# plotting a bar chart for batting team and it's count

ax = sns.countplot(x = 'batting_team',data = dl)
ax.xaxis.set_tick_params(labelsize=12)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
plt.title('Batting Team')

for bars in ax.containers:
    ax.bar_label(bars)


# In[20]:


# plotting a bar chart for bowling_team and it's count

ax = sns.countplot(x = 'bowling_team',data = dl, )
ax.xaxis.set_tick_params(labelsize=10)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
plt.title('Bowling Team')

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


# plotting a bar chart for innings and it's count

ax = sns.countplot(x = 'inning',data = dl, )
ax.xaxis.set_tick_params(labelsize=8)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
plt.title('Innings')

for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


# batting team vs wide runs

Data = dl.groupby(['batting_team'], as_index=False)['wide_runs'].sum().sort_values(by='wide_runs', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,10)})
ax = sns.countplot(x = 'batting_team',data = Data, )
ax.xaxis.set_tick_params(labelsize=15)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
sns.barplot(data = Data, x = 'batting_team',y= 'wide_runs')


# In[23]:


# batting team vs by runs

Data = dl.groupby(['batting_team'], as_index=False)['bye_runs'].sum().sort_values(by='bye_runs', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,10)})
ax = sns.countplot(x = 'batting_team',data = Data, )
ax.xaxis.set_tick_params(labelsize=15)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
sns.barplot(data = Data, x = 'batting_team',y= 'bye_runs')


# In[24]:


# bowling team vs wide runs

Data = dl.groupby(['bowling_team'], as_index=False)['wide_runs'].sum().sort_values(by='wide_runs', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,10)})
ax = sns.countplot(x = 'bowling_team',data = Data, )
ax.xaxis.set_tick_params(labelsize=15)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
sns.barplot(data = Data, x = 'bowling_team',y= 'wide_runs')


# In[25]:


# batting team vs penality runs

Data = dl.groupby(['batting_team'], as_index=False)['penalty_runs'].sum().sort_values(by='penalty_runs', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,10)})
ax = sns.countplot(x = 'batting_team',data = Data, )
ax.xaxis.set_tick_params(labelsize=15)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
sns.barplot(data = Data, x = 'batting_team',y= 'penalty_runs')


# In[26]:


# bowling team vs penality runs

Data = dl.groupby(['bowling_team'], as_index=False)['penalty_runs'].sum().sort_values(by='penalty_runs', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,10)})
ax = sns.countplot(x = 'bowling_team',data = Data, )
ax.xaxis.set_tick_params(labelsize=15)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
sns.barplot(data = Data, x = 'bowling_team',y= 'penalty_runs')


# In[27]:


sns.histplot(dl['total_runs'], bins=20, kde=True, color='blue', label='Total Team Runs') 


# In[28]:


# sns.histplot(dl['extra_runs'], bins=10, kde=True, color='black', label='Extra Team Runs')


# In[29]:


# line plot total runs vs penality runs
# sns.lineplot(x='is_super_over',y='non_striker',data=dl,labels="Run score")


# In[30]:


#ine plot over vs balls runs 
# print(df.dtypes)sns.lineplot(x='over', y='ball', data=dl) 


# In[ ]:


#  correlation_matrix = dl.corr()
# plt.figure(figsize=(10,8))
# sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True, fmt=".2f")
# plt.title('Correlation Heatmap')
# plt.show()


# In[32]:


types=dl['batting_team'].value_counts()
plt.pie(types,labels=types.index,labeldistance=1)
plt.show()


# In[33]:


types=dl['bowling_team'].value_counts()
plt.pie(types,labels=types.index,labeldistance=1)
plt.show()


# In[42]:





# In[37]:


dl.head()


# In[41]:


dl.info()


# In[46]:


winner_team=dl['batsman']
s=dl['batsman_runs']
colors=np.arange(179078)
plt.scatter(s,winner_team,c=colors,alpha=0.5,cmap='rainbow')
plt.xlabel('batsman')
plt.ylabel('runs')
o=plt.colorbar()
o.set_label("colorbar",fontsize=15)
plt.show()


# In[ ]:




