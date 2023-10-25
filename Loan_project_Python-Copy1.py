#!/usr/bin/env python
# coding: utf-8

# In[8]:


## The purpose of the project
## 1. Explore data with SQL.
## 2. Visualization using python based on searched data.
## 3. Additionally, Exploring, visualization data with only Python(Pandas, Plotly)


# In[9]:


import pandas as pd
import plotly.express as px


# In[10]:


#load age_loan data that explore from SQL, and do visualization.
age_loan = pd.read_csv('C:/Users/jaeki/OneDrive/바탕 화면/data/project/age_loan.csv')
age_loan


# In[11]:


fig = px.bar(age_loan, x = 'Age_group', y = 'Average_loan',
             title = 'Average loan by age group', color = 'Average_loan')
fig.show()


# In[12]:


# Load data and visualization.
gender_loan = pd.read_csv('C:/Users/jaeki/OneDrive/바탕 화면/data/project/gender_loan.csv')
gender_loan


# In[13]:


fig = px.pie(gender_loan, values = 'Gender_loan', names = 'Gender')
fig.show()


# In[14]:


income_loan = pd.read_csv('C:/Users/jaeki/OneDrive/바탕 화면/data/project/income_loan.csv')
income_loan


# In[15]:


fig  = px.bar(income_loan, x = 'Income_group', y = 'Income_loan', color = 'Income_loan')
fig.show()


# In[16]:


occupation_loan = pd.read_csv('C:/Users/jaeki/OneDrive/바탕 화면/data/project/occupation_loan.csv')
occupation_loan


# In[17]:


fig = px.bar(occupation_loan, x = 'Occupation', y = 'Occupation_loan')
fig.show()


# In[18]:


occupation_overdue = pd.read_csv('C:/Users/jaeki/OneDrive/바탕 화면/data/project/occupation_overdue.csv')
occupation_overdue


# In[19]:


fig = px.bar(occupation_overdue, x = 'Occupation',  y = 'Occupation_overdue')
fig.show()


# In[20]:


# merge data and visualize to find correlatiion between of Loan and overdue by occupation.
merged_data = pd.merge(occupation_loan, occupation_overdue, on = 'Occupation')
merged_data


# In[21]:


fig = px.scatter(merged_data, x = 'Occupation', y = 'Occupation_loan', color = 'Occupation_overdue')
fig.show()


# In[22]:


# Additionaly explore and do visualization with only Python(Plotly, Pandas)
df = pd.read_csv('C:/Users/jaeki/OneDrive/바탕 화면/data/loan.csv')
df


# In[23]:


# Remove Nan value.
df = df.dropna()
df


# In[24]:


#gender_loan
#The reason why I put '1' in df's name, because I used 'gender_loan' at the beginning.

gender_loan1 = df.groupby('Gender')['Loan'].mean().reset_index()
gender_loan1


# In[25]:


fig = px.bar(gender_loan1, x = 'Gender', y = 'Loan')
fig.show()


# In[26]:


#Age_loan
# use lambda x funtcion to make age group.

def create_age_group(age):
    if 21 <= age <= 30:
        return '21-30'
    elif 31 <= age <= 40:
        return '31-40'
    elif 41 <= age <= 50:
        return '41-50'
    elif 51 <= age <= 60:
        return '51-60'
    else:
        return '60+'

df_copy = df.copy()

df_copy['Age_group'] = df_copy['Age'].apply(lambda x: create_age_group(x))

age_loan1 = df_copy.groupby('Age_group')['Loan'].mean().reset_index()

age_loan1


# In[27]:


fig = px.bar(age_loan1, x = 'Age_group', y = 'Loan')
fig.show()


# In[28]:


def create_income_group(income):
    if income < 30000:
        return 'Low'
    elif 30000 <= income < 60000:
        return 'Medium'
    else:
        return 'High'
    
df_copy = df.copy()


df_copy['Income_group'] = df_copy['Income'].apply(lambda x: create_income_group(x))

income_loan1 = df_copy.groupby('Income_group')['Loan'].mean().reset_index()

income_loan1


# In[29]:


#Income_loan group
income_loan1 = income_loan1.sort_values( by = 'Loan', ascending = False)

fig = px.bar(income_loan1, x = 'Income_group', y = 'Loan')
fig.show()


# In[30]:


#Occupation and loan group
occupation_loan1 = df.groupby('Occupation')['Loan'].mean().reset_index()
occupation_loan1 = occupation_loan1.sort_values(by = 'Loan', ascending= False)
occupation_loan1


# In[31]:


fig = px.bar(occupation_loan1, x = 'Occupation', y = 'Loan')
fig.show()


# In[32]:


occupation_overdue1 = df.groupby('Occupation')['Overdue'].mean().reset_index()
occupation_overdue1 = occupation_overdue1.sort_values(by = 'Overdue', ascending= False)
occupation_overdue1


# In[33]:


fig = px.bar(occupation_overdue1, x = 'Occupation', y = 'Overdue')
fig.show()


# In[34]:


# Merge Occupation_loan1 and Occupation_overdue1 data and visualization

merged_data1 = pd.merge(occupation_loan1, occupation_overdue1, on = 'Occupation')
merged_data1


# In[35]:


# visualize data, use 'Overdue' Column as a color
fig = px.bar(merged_data1, x = 'Occupation', y = 'Loan', color = 'Overdue')
fig.show()


# In[ ]:




