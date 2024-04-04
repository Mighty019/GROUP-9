#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #used for array
import pandas as pd #used for tables
import matplotlib.pyplot as plt # helps in to viusalize the charts
import seaborn as sns # perform the same fuction as metplotlib


# In[2]:


ipl=pd.read_csv("C:\\Users\\Lenovo\\Desktop\\matches.csv")


# In[3]:


ipl.head()


# In[4]:


ipl.head(10
        )


# In[5]:


ipl.info()


# In[ ]:





# In[6]:


ipl.columns


# In[7]:


#no need to drop any row as all here contains the some values


# In[8]:


ipl.shape #gives the info about rows and column


# In[9]:


pd.isnull(ipl) #provide the info about missing values 


# In[10]:


pd.isnull(ipl).sum() #used to calculate the total null values


# In[11]:


#we need to clean the data as there is lots of missing values are present


# In[12]:


#ipl.dropna(inplace=True) # drop null values


# In[13]:


ipl['city']=ipl['city'].fillna('Not Found')


# In[14]:


ipl['winner']=ipl['winner'].fillna('Not Found')


# In[15]:


ipl['player_of_match']=ipl['player_of_match'].fillna('Not Found')


# In[16]:


ipl['umpire1']=ipl['umpire1'].fillna('Not required')


# In[17]:


ipl['umpire2']=ipl['umpire2'].fillna('Not required')


# In[18]:


ipl['umpire3']=ipl['umpire3'].fillna('Not required')


# In[19]:


ipl.info()


# In[20]:


ipl.isnull().sum()


# In[21]:


ipl.describe()


# In[22]:


# plotting a bar chart for winner and it's count

ax = sns.countplot(x = 'winner',data = ipl, )
ax.xaxis.set_tick_params(labelsize=8)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


# dir(plt)


# In[24]:


types=ipl['toss_decision'].value_counts()


# In[25]:


plt.pie(types,labels=types.index,labeldistance=1)
plt.show()


# In[26]:


types=ipl['toss_winner'].value_counts()
plt.pie(types,labels=types.index,labeldistance=1)
plt.show()


# In[27]:


# ipl = ipl.astype(int)
# print(ipl.dtypes)
# correlation_matrix = ipl.corr()
# plt.figure(figsize=(20,8))
# sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True, fmt=".2f")
# plt.title('Correlation Heatmap')
# plt.show()


# In[28]:


# player of match wins by run

Data = ipl.groupby(['player_of_match'], as_index=False)['win_by_runs'].sum().sort_values(by='win_by_runs', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = Data, x = 'player_of_match',y= 'win_by_runs')


# In[29]:


# player of match wins by wicket

Data1 = ipl.groupby(['player_of_match'], as_index=False)['win_by_wickets'].sum().sort_values(by='win_by_wickets',  ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = Data1, x = 'player_of_match',y= 'win_by_wickets')


# In[30]:


ipl['teams'] = list(zip(ipl.team1, ipl.team2))


# In[31]:


ipl.teams


# In[33]:


#plotting a bar graph with win by runs 0 included in it
x=ipl['team1']
y=ipl['win_by_runs']
plt.bar(x,y,color="r")
plt.xlabel("team1",fontsize=10)
plt.ylabel("win by runs",fontsize=10)
plt.title("bar graph of team 1 won the match by runs",fontsize=15)
plt.xticks(rotation=90)
plt.show()


# In[34]:


#Now checking for win by wickets by teams
w=ipl['win_by_wickets']
plt.barh(x,w,color="r")
plt.xlabel("team1",fontsize=10)
plt.ylabel("win by wickets",fontsize=10)
plt.title("bar graph of team 1 won the match by wicktes",fontsize=15)
plt.show()


# In[36]:


winner_team=ipl['winner']
s=ipl['win_by_runs']
colors=np.arange(756)
plt.scatter(s,winner_team,c=colors,alpha=0.5,cmap='rainbow')
plt.xlabel('win by runs')
plt.ylabel('winner teams')
o=plt.colorbar()
o.set_label("colorbar",fontsize=15)
plt.show()


# In[37]:


plt.boxplot(ipl['win_by_wickets'])
plt.xlabel('wickets')
plt.show()


# In[38]:


plt.boxplot(ipl['win_by_runs'])
plt.xlabel("win by runs")
plt.show()


# In[39]:


u=ipl['umpire3']
plt.bar(u,s)
plt.xticks(rotation=90,ha='right')
plt.xlabel('umpire3')
plt.ylabel('win by runs')
plt.show()


# In[ ]:




