import pandas as pd
import pickle
import csv

df = pd.read_csv("D:/PycharmProject/Forest-Fire/Forest_Fire.csv")


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df[['Oxygen','Temperature','Humidity']],df.Fire_Occurrence,test_size=0.1)



from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
model.predict(X_test)
model.score(X_test,y_test)
model.predict_proba(X_test)



print(model.score(X_test,y_test))

print(model.predict(X_test))

print(model.predict([[12,12,12]]))


pickle.dump(model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))