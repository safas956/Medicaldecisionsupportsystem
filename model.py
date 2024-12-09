import warnings
warnings.filterwarnings('ignore')


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('dataset.xlsx')
df.tail

df.shape
df.info()
df.describe()
df.isnull().sum()
df.nunique()

df = df.dropna()


#df['SEX'] = df['SEX'].map({'M': 0 ,'F': 1})

from sklearn.preprocessing import LabelEncoder

l1 = LabelEncoder()
l1.fit(df['SEX'])
df.SEX = l1.transform(df.SEX)
print(df)

corr = df.corr()
 
plt.figure(dpi=130)
sns.heatmap(df.corr(), annot=True, fmt= '.2f')
plt.show()


plt.pie(df.SOURCE.value_counts(), 
        labels= ['0', '1'], 
        autopct='%.f', shadow=True)
plt.title('SOURCE')
plt.show()


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(df)

# check outlier in column
sns.boxplot(df['HAEMATOCRIT'])
sns.boxplot(df['HAEMOGLOBINS'])
sns.boxplot(df['ERYTHROCYTE'])
sns.boxplot(df['LEUCOCYTE'])
sns.boxplot(df['THROMBOCYTE'])
sns.boxplot(df['MCH'])
sns.boxplot(df['MCHC'])
sns.boxplot(df['MCV'])
sns.boxplot(df['AGE'])




x = df.iloc[:, :10]
y = df.iloc[:, -1]		

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.70, random_state=42)

from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression(random_state = 42)
lg_model.fit(x_train, y_train)


lg_train, lg_test = lg_model.score(x_train , y_train), lg_model.score(x_test , y_test)

print(f"Training Score: {lg_train}")
print(f"Test Score: {lg_test}")




from sklearn.ensemble import RandomForestRegressor

modelr = RandomForestRegressor()
modelr.fit(x, y)
predictionsr = modelr.predict(x_test)
accr = modelr.score(x_train,y_train)
rf_acc = accr*100



from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(random_state=42)
model.fit(x, y)
dtacc=round(model.score(x, y), 4)

from sklearn.svm import SVR
SVM = SVR()
SVM.fit(x, y)
svmacc=round(SVM.score(x, y), 4)


data = {'RandomForestClassifier':rf_acc,'LogisticRegression':lg_train*100,'DecisionTreeRegressor':dtacc*100}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color =['black', 'red', 'green'], 
        width = 0.4)
 
plt.xlabel("Algorithm")
plt.ylabel("Accuracy")
plt.title("Accuracy of Algorithms")
plt.show()

import pickle
file=open('my_model.pkl','wb')
pickle.dump(model,file,protocol=3)
