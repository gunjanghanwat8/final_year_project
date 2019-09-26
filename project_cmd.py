import classifier as classifier
import pandas as pd
import numpy as np
import csv
from sklearn.preprocessing import LabelBinarizer

print("------------------------------------------------------------")
print(" ")
print("BODY TYPE RECOGNIZATION")
row=[]
print(" ")
print("-------------------------------------------------------------")

height=int((input("enter the height in cm\n")))
gender=input("enter the gender M--->male or F---->Female\n")
weight=int((input("enter the weight in kgs\n")))
age=int((input("enter the age in whole year\n")))
print("--------------------------------------------------------------")
bmi=int((weight*10000)/(height*height))
if(gender=='M'):
    gender=0
else:
    gender=1
if(gender==0):
    fat=int(1.20*bmi+0.23*age-16.2)
    bmr=int(66.4730+(13.7516*weight)+(5.0033*weight)-(6.7550*age))
elif(gender==1):
    fat=int(1.20*bmi+0.23*age-5.4)
    bmr=int(655.0955+(9.5634*weight)+(1.8496*height)-(4.6756*age))

row.append(gender)
row.append(height)
row.append(weight)
row.append(age)
row.append(bmi)
row.append(fat)
row.append(bmr)

with open('test_data1.csv','a') as csvFile:
    writer=csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()

dataset=pd.read_csv('numerical_data_hw1.csv')
x=dataset.iloc[:,[1,2,3,4,5,6,7]].values
y=dataset.iloc[:,8].values





# from sklearn.preprocessing import LabelEncoder,OneHotEncoder
# labelencoder_x=LabelEncoder()
# x[:,0]=labelencoder_x.fit_transform(x[:,0])
# onehotencoder=OneHotEncoder(categorical_features=[0])
# x=onehotencoder.fit_transform(x).toarray()
#
# labelencoder_y=LabelEncoder()
# y=labelencoder_y.fit_transform(y)
# # onehotencoder=onehot(categorical_feature=[0])
# # y=onehotencoder.fit_transform(y).toarray()
#
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state =0)

# onehotencoder=OneHotEncoder()
# y=onehotencoder.fit_transform(y).toarray()




from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)

l=pd.read_csv('test_data1.csv')
l=l.iloc[:,[0,1,2,3,4,5,6]].values

y_pred=classifier.predict(l)
size=(len(y_pred)-1)
l=0
while(l!=size):
     l=l+1
value=y_pred[l]

if(value==0):
    print("------body type is UNDERWEIGHT------")
    print("the required calories are",bmr)
    # print("the fat percentage is ",fat,"%")
elif(value==1):
    print("----body type is NORMAL------------")
    print("the required calories are",bmr)
    # print("the fat percentage is ",fat,"%")

elif(value==2):
    print("-------body type is OBASE-------")
    print("the required calories are",bmr)
    # print("the fat percentage is ",fat,"%")

else:
    print("---------OVER-WEIGHT------------")
    print("the required calories are",bmr)
    # print("the fat percentage is ",fat,"%")
