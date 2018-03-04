
# coding: utf-8

# In[8]:


from __future__ import print_function, division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
palette = sns.color_palette('deep', 5)
palette[1], palette[2] = palette[2], palette[1]
get_ipython().magic(u'matplotlib inline')
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score

train = pd.read_csv('train.csv')
val = pd.read_csv('val.csv')
test = pd.read_csv('solution_no_answer.csv')


# In[20]:


tr_action = pd.get_dummies(train['ACTION_TYPE'])
val_action = pd.get_dummies(val['ACTION_TYPE'])
test_action = pd.get_dummies(test['ACTION_TYPE'])


# In[21]:


train = train.drop(['EVENTTIME', 'EVENT_TYPE', 'GAME_DATE', 'GAME_EVENT_ID', 'GAME_ID', '' 'HTM', 'LOC_X', 'LOC_Y', 'MINUTES_REMAINING', 'PERIOD', 'PLAYER_NAME', 'QUARTER', 'SECONDS_REMAINING', 'SHOT_ATTEMPTED_FLAG', 'SHOT_TIME', 'SHOT_ZONE_AREA', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_RANGE', 'TEAM_ID', 'TEAM_NAME', 'VTM'], axis=1)


# In[11]:


test = test.drop(['EVENTTIME', 'EVENT_TYPE', 'GAME_DATE', 'GAME_EVENT_ID', 'GAME_ID', '' 'HTM', 'LOC_X', 'LOC_Y', 'MINUTES_REMAINING', 'PERIOD', 'PLAYER_NAME', 'QUARTER', 'SECONDS_REMAINING', 'SHOT_ATTEMPTED_FLAG', 'SHOT_TIME', 'SHOT_ZONE_AREA', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_RANGE', 'TEAM_ID', 'TEAM_NAME', 'VTM'], axis=1)
val = val.drop(['EVENTTIME', 'EVENT_TYPE', 'GAME_DATE', 'GAME_EVENT_ID', 'GAME_ID', '' 'HTM', 'LOC_X', 'LOC_Y', 'MINUTES_REMAINING', 'PERIOD', 'PLAYER_NAME', 'QUARTER', 'SECONDS_REMAINING', 'SHOT_ATTEMPTED_FLAG', 'SHOT_TIME', 'SHOT_ZONE_AREA', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_RANGE', 'TEAM_ID', 'TEAM_NAME', 'VTM'], axis=1)


# In[27]:


tr_action = tr_action.drop(['Driving Jump shot', 'Running Hook Shot', 'Step Back Bank Jump Shot', 'Driving Reverse Dunk Shot', 'Running Alley Oop Layup Shot', 'Running Reverse Dunk Shot'], axis=1)


# In[28]:


val_action = val_action.drop(['Driving Reverse Dunk Shot', 'Running Alley Oop Layup Shot', 'Running Reverse Dunk Shot'], axis=1)


# In[29]:


test_action = test_action.drop(['Step Back Bank Jump Shot'], axis=1)


# In[32]:


tr_type = pd.get_dummies(train['SHOT_TYPE'], drop_first=True)


# In[33]:


val_type = pd.get_dummies(val['SHOT_TYPE'], drop_first=True)
test_type = pd.get_dummies(test['SHOT_TYPE'], drop_first=True)



# In[35]:


train = train.drop(['ACTION_TYPE', 'SHOT_TYPE'], axis=1)
val = val.drop(['ACTION_TYPE', 'SHOT_TYPE'], axis=1)
test = test.drop(['ACTION_TYPE', 'SHOT_TYPE'], axis=1)


# In[36]:


train = pd.concat([train, tr_type, tr_action], axis = 1)
val = pd.concat([val, val_type, val_action], axis = 1)
test = pd.concat([test, test_type, test_action], axis=1)


# In[39]:


X_tr = train.drop('SHOT_MADE_FLAG', axis=1)
Y_tr = train['SHOT_MADE_FLAG']


# In[40]:


X_val = val.drop('SHOT_MADE_FLAG', axis=1)
Y_val = val['SHOT_MADE_FLAG']


# In[46]:


scaler = StandardScaler()
X_tr_scaled = scaler.fit_transform(X_tr)
svmmodel = SVC()
svmmodel.fit(X_tr_scaled, Y_tr)


# In[47]:


X_val_scaled = scaler.transform(X_val)
predictions = svmmodel.predict(X_val_scaled)
print(classification_report(Y_val, predictions))
print("Accuracy: {}".format(accuracy_score(Y_val, predictions)))


# In[49]:


test_scaled = scaler.transform(test)
predictions = svmmodel.predict(test_scaled)


# In[53]:


test_game_id = pd.read_csv('solution_no_answer.csv')


# In[54]:


test_game_id = test_game_id['GAME_EVENT_ID']



# In[61]:


out_file = open("submission.csv", "a")


# In[62]:


out_file.write("GAME_EVENT_ID,SHOT_MADE_FLAG\n")


# In[63]:


for x in range(0, len(predictions)):
    out_file.write("%s,%s\n" % (str(test_game_id[x]), str(predictions[x])))


# In[64]:


out_file.close()
