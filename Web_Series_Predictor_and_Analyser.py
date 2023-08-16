# -*- coding: utf-8 -*-
#19/06/23 Data Pre-processing
import pandas as pd
import numpy as np
df=pd.read_csv("Series_Movies_dataset.csv")
df.head(5)
train_df=df.iloc[:7496] #80%-20% train-test split
test_df=df.iloc[7497:]
print(train_df)

train_df.columns

train_df.isna().sum()

#01/07/23 Preliminary Stages of Building a Model
plat_list=[] #contains names of all unique platforms
for i in df['Streaming Platform']:
  ls=i.split(',')
  for j in ls:
    if j not in plat_list:
      plat_list.append(j)
    else:
      continue
#print(plat_list)

#03/07/23
from sklearn.preprocessing import LabelBinarizer
lb=LabelBinarizer()
lb.fit(plat_list) #assign unique binary values to each streaming platform
lb.classes_
([plat_list])
plat_bin=lb.transform(plat_list)
# for i in plat_bin:
#   print(i)
# print(len(plat_bin))

map_plat=dict() #maintaining the mapping of platform and its binary representation
for i in plat_list:
  for j in plat_bin:
    map_plat.setdefault(i,j)
# for i in map_plat:
#   print(i,map_plat[i])
#print(len(map_plat))

genre_list=[] #contains names of all unique genres
for i in df['Genre']:
  ls=i.split(',')
  for j in ls:
    if j not in genre_list:
      genre_list.append(j)
    else:
      continue
#print(genre_list)

from sklearn.preprocessing import LabelBinarizer
lb=LabelBinarizer()
lb.fit(genre_list) #assign unique binary values to each genre
lb.classes_
([genre_list])
genre_bin=lb.transform(genre_list)
#for i in genre_bin:
  #print(i)
#print(len(genre_bin))

map_genre=dict() #maintaining the mapping of genre and its binary representation
for i in genre_list:
  for j in genre_bin:
    map_genre.setdefault(i,j)
#for i in map_genre:
  #print(i,map_genre[i])
#print(len(map_genre))

#Creating column of binary OR operated Genres
gen_or_ls=[]
for i in df['Genre']:
  ls = i.split(",");
  ans=0
  for j in range (0,len(ls)):
    ans=ans | genre_bin[j]
  gen_or_ls.append(ans)
df['ORed_Binary_Genres']=gen_or_ls
lg = df['ORed_Binary_Genres'].tolist()
cp1 = pd.DataFrame(lg,dtype=int).to_numpy()
df['ORed_Binary_Genres'] = cp1

#Creating column of binary OR operated Streaming Platforms
streamplat_or_ls=[]
for i in df['Streaming Platform']:
  ls = i.split(",");
  ans=0
  for j in range (0,len(ls)):
    ans= ans | plat_bin[j]
  streamplat_or_ls.append(ans)
df['ORed_Binary_Streaming_Platforms']=streamplat_or_ls
bg = df['ORed_Binary_Streaming_Platforms'].tolist()
cp2 = pd.DataFrame(bg,dtype=int).to_numpy()
df['ORed_Binary_Streaming_Platforms'] = cp2

train_df=train_df.drop(['Series Title'],axis=1)
train_df=train_df.drop(['Genre'],axis=1)
train_df=train_df.drop(['Description'],axis=1)
train_df=train_df.drop(['Streaming Platform'],axis=1)

#07/08/23 Kmeans Model Creation
from sklearn.cluster import KMeans
import numpy as np
kmeans=KMeans(n_clusters=3, random_state=0, n_init="auto").fit(train_df)

#08/08/23 Testing Model
test_df=test_df.drop(['Series Title'],axis=1)
test_df=test_df.drop(['Genre'],axis=1)
test_df=test_df.drop(['Description'],axis=1)
test_df=test_df.drop(['Streaming Platform'],axis=1)

predicted_values=kmeans.fit_predict(test_df)
# for i in predicted_values:
#   print(i)

# Calculating the quality of clustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.metrics import accuracy_score

# Calculate Silhouette Score
silhouette_avg = silhouette_score(test_df,predicted_values)
# Calculate Calinski-Harabasz Index
ch_score = calinski_harabasz_score(test_df,predicted_values)
print(silhouette_avg)
print(ch_score)
