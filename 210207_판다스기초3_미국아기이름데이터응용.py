#!/usr/bin/env python
# coding: utf-8

# 러닝스푼즈_ 파이썬데이터분석마스터_by장남수 4주차
# 판다스기초_3

# In[1]:


import pandas as pd


# In[5]:


file = './data/babyNamesUS.csv'
raw = pd.read_csv(file)
# csv comma seperated value   값1, 값2, 값3, ,,,
# tsv tap                     값1     값2      값3 ......
# tsv 파일 읽을 때... raw = pd.read_csv(file, sep='\')


# In[8]:


#데이터 살펴보기
#raw.head()
#raw.tail()
raw.sample(10)


# In[9]:


raw.info()
# RangeIndex: 1048575  개수와 Non-Null Count 숫자 확인


# In[10]:


raw.describe()


# In[ ]:


# 이름별 합계 데이터 만들기
# raw.pivot_table(index = '컬럼', values='컬럼명', aggfunc = 'sum/count/max/min/mean 등')


# In[14]:


df = raw.pivot_table(index = 'Name', values='Number', aggfunc = 'sum')
df


# In[21]:


# 정렬하기
#df.sort_values('Number', ascending = False)
df.sort_values('Number', ascending = False).head(10)
#ascending = False 내림차순


# In[22]:


# 10개에 해당하는 index 확인
df.sort_values('Number', ascending = False).head(10).index 


# #### 남성들이 많이 사용하는 이름인가?
# #### 남자/여자를 분리하여 데이터 정리 해보기

# In[23]:


# 방법1 : 리스로 묶어서 
raw.pivot_table(index=['Name','Sex'], values='Number', aggfunc='sum', )


# In[27]:


# pivot_table()의 기능을 이용하기
name_df = raw.pivot_table(index='Name', values='Number', aggfunc='sum', columns='Sex' )
name_df
# 행 or 컬럼으로 나눌지 --> 행으로 나누는게 좋다. 재가공이 가능하기 때문
# 재가공이 필요하지 않을 경우 컬럼으로 데이터를 쌓는 것도 나쁘지 않음 하지만 재가공이 어려울 수 있다.


# In[28]:


name_df.info()


# 14140개 여자이름의 종류가 더 많다. 

# In[33]:


# 결측값에 값 추가해주기
name_df = name_df.fillna(0)
name_df.info()
# 누락된 값이 다 채워져 있다. 
# 0과 nan의 값은 의미가 다르다


# In[37]:


name_df.sort_values('F', ascending = False).head(10)


# In[38]:


name_df.sort_values('M', ascending = False).head(10)


# In[ ]:


###  []로 묶어서 여러개 조건을 선택할 수 있다.
raw.pivot_table(index='Name', values='Number', aggfunc=['sum','count'])


# In[40]:


# 데이터의 종류를 보는 법
raw['YearOfBirth'].unique()


# In[43]:


# 연도별 얼마나 사용 되었다....
#raw['YearOfBirth'].value_counts() # 시리즈로 보여짐
#raw['YearOfBirth'].value_counts().head(10)
raw['YearOfBirth'].value_counts().head(10).index  


# In[44]:


name_df.head()


# #### 성별 비중 계산하기
# 

# In[46]:


name_df['total'] = name_df['M']+ name_df['F']
name_df.head()


# In[49]:


name_df['F_ratio'] = name_df['F']/ name_df['total']
name_df['M_ratio'] = name_df['M']/ name_df['total']
name_df.head ()


# In[54]:


cond = (name_df['total']>10000)    & (name_df['M_ratio']>0.4)    & (name_df['M_ratio']<0.6)
name_df[cond].sort_values('total', ascending=False)


# In[ ]:





# In[ ]:




