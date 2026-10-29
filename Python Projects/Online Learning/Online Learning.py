from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Online Learning Dataset
Learning = Table.read_table('Online_Learning_Behavior_Dataset_Worldwide.csv')
print(Learning)

#Summary Statistics
print("Summary Statistics of Online Learning Satisfaction Score")
print(f"Number of Students in the Study: {len(Learning.column('Satisfaction_Score(1-5)'))}")
print(f"Maximum Satisfaction Score(1-5): {np.round(np.max(Learning.column('Satisfaction_Score(1-5)')), 2)}")
print(f"Average Satisfaction Score(1-5): {np.round(np.mean(Learning.column('Satisfaction_Score(1-5)')), 2)}")
print(f"Standard Deviation Satisfaction Score(1-5): {np.round(np.std(Learning.column('Satisfaction_Score(1-5)'), ddof = 0), 2)}")
print(f"Median Satisfaction Score(1-5): {np.round(np.median(Learning.column('Satisfaction_Score(1-5)')), 2)}")
print(f"Minimum Satisfaction Score(1-5): {np.round(np.min(Learning.column('Satisfaction_Score(1-5)')), 2)}")
print(f"Coefficient of Variation Satisfaction Score(1-5): {np.round(np.std(Learning.column('Satisfaction_Score(1-5)'), ddof = 0)/np.mean(Learning.column('Satisfaction_Score(1-5)')) * 100, 2)}%")

#Line Plot
Decimal_Date = make_array()
year = 0
month = 0
day = 0

for i in range(0, Learning.num_rows):

    #Year
    year = int(Learning.column('Enrollment_Date')[i].split('-')[0])

    #Month
    month = int(Learning.column('Enrollment_Date')[i].split('-')[1])

    if month == 1:
        month = 0
    elif month == 2:
        month = 31
    elif month == 3:
        month = 59
    elif month == 4:
        month = 90
    elif month == 5:
        month = 120
    elif month == 6:
        month = 151
    elif month == 7:
        month = 181
    elif month == 8:
        month = 212
    elif month == 9:
        month = 243
    elif month == 10:
        month = 273
    elif month == 11:
        month = 304
    elif month == 12:
        month = 334

    #Day
    day = int(Learning.column('Enrollment_Date')[i].split('-')[2])

    #Decimal Date
    Decimal_Date = np.append(Decimal_Date, year + (day + month)/365)


Learning = Learning.with_column('Enrollment_Decimal_Date', Decimal_Date)

Learning.plot('Enrollment_Decimal_Date', 'Daily_Learning_Hours')
plt.xlabel('Enrollment Date')
plt.ylabel('Daily Learning Hours')
plt.title('Daily Learning Hours by Enrollment Date')
plt.show()

#Country
Learning.group('Country').relabel('count', 'Count').sort('Count', descending = True).barh('Country', 'Count')
plt.xlabel('Count')
plt.ylabel('Country')
plt.title('Number of Students by Country')
plt.show()

#Age
Learning.hist('Age', bins = 10)
plt.xlabel('Age')
plt.ylabel('Percent')
plt.title('Histogram of Student Age')
plt.show()

#Gender
Learning.group('Gender').relabel('count', 'Count').where('Gender', are.not_equal_to('Other')).sort('Count', descending = True).barh('Gender', 'Count')
plt.xlabel('Count')
plt.ylabel('Sex')
plt.title('Number of Students by Sex')
plt.show()

#Education Level
Learning.group('Education_Level').relabel('count', 'Count').sort('Count', descending = True).barh('Education_Level', 'Count')
plt.xlabel('Count')
plt.ylabel('Education Level')
plt.title('Number of Students by Education Level')
plt.show()

#Field of Study
Learning.group('Field_of_Study').relabel('count', 'Count').sort('Count', descending = True).barh('Field_of_Study', 'Count')
plt.xlabel('Count')
plt.ylabel('Field of Study')
plt.title('Number of Students by Field of Study')
plt.show()

Learning_num = Learning.num_rows

Data_Science = Learning.where('Field_of_Study', are.equal_to('Data Science')).num_rows
Computer_Science = Learning.where('Field_of_Study', are.equal_to('Computer Science')).num_rows
Business = Learning.where('Field_of_Study', are.equal_to('Business')).num_rows
Engineering = Learning.where('Field_of_Study', are.equal_to('Engineering')).num_rows
Arts = Learning.where('Field_of_Study', are.equal_to('Arts')).num_rows

Online_Learning = Table().with_columns(
    'Field_of_Study', make_array('Data Science', 'Computer Science', 'Business', 'Engineering', 'Arts'),
    'Percent', make_array(Data_Science / Learning_num * 100, Computer_Science / Learning_num * 100, Business / Learning_num * 100, Engineering / Learning_num * 100, Arts / Learning_num * 100))

plt.pie(Online_Learning.column('Percent'), labels = Online_Learning.column('Field_of_Study'))
plt.title('Proportion by Field of Study')
plt.show()

#Platform Used
Learning.group('Platform_Used').relabel('count', 'Count').sort('Count', descending = True).barh('Platform_Used', 'Count')
plt.xlabel('Count')
plt.ylabel('Learning Platform')
plt.title('Number of Students by Learning Platform')
plt.show()

#Device Used
Learning.group('Device_Used').relabel('count', 'Count').sort('Count', descending = True).barh('Device_Used', 'Count')
plt.xlabel('Count')
plt.ylabel('Device')
plt.title('Number of Students by Device')
plt.show()

#Learning
Learning.group('Learning_Mode').relabel('count', 'Count').sort('Count', descending = True).barh('Learning_Mode', 'Count')
plt.xlabel('Count')
plt.ylabel('Learning Mode')
plt.title('Number of Students by Learning Mode')
plt.show()

#Daily Learning Hours
Learning.hist('Daily_Learning_Hours', bins = 10)
plt.xlabel('Daily Learning Hours')
plt.ylabel('Percent')
plt.title('Histogram of Daily Learning Hours')
plt.show()

#Linear Regression
#Are Daily Learning Hours and Course Completion Rate correlated?
x = np.array(Learning.column('Daily_Learning_Hours'))
y = np.array(Learning.column('Course_Completion_Rate(%)'))

coefficients = np.polyfit(x, y, 1)
a = coefficients[0] # Slope
b = coefficients[1] # Y-Intercept

x_fit = x
y_fit = a * x + b

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label=f'y = {a:.3f}x + {b:.3f}')
plt.title('Linear Regression')
plt.xlabel('Daily Learning Hours')
plt.ylabel('Course Completion Rate(%)')
plt.legend()
plt.grid(True)
plt.show()

r = np.corrcoef(x, y)[0, 1]
print(f"Linear Equation: y = {a:.3f}x + {b:.3f}")
print(f"Correlation R: {r}")

#Random Forest --- Predicting Satisfaction Score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.column_stack([Learning.column('Daily_Learning_Hours'), Learning.column('Course_Completion_Rate(%)')])
Y = Learning.column('Satisfaction_Score(1-5)')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 50, stratify = Y)

model = RandomForestClassifier(n_estimators = 300, max_depth = 25, min_samples_leaf = 2, random_state = 50, class_weight = "balanced")
model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)
print(f"Random Forest Prediction (5 hours daily and 50% completion rate): {model.predict([[5, 50]])[0]} Satisfaction Score")
print("Random Forest Accuracy:", round(accuracy_score(Y_test, Y_predict), 4))

estimator = model.estimators_[0]
plt.figure(figsize=(20,10))
plot_tree(estimator, feature_names = ["Daily_Learning_Hours", "Course_Completion_Rate(%)"], class_names = True, filled = True, rounded = True, max_depth = 3)
plt.show()
