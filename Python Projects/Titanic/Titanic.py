from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Titanic Dataset
#Assignment 01: Exploratory Data Analysis with the Titanic Dataset (100 points)

# **Name:** Landry Ratliff
# **Date:** March 25, 2026
# **Total Points:** 100

#In this assignment you will perform a full exploratory data analysis (EDA) on the **Titanic dataset**
#The Titanic dataset records information about passengers aboard the RMS Titanic, which sank on April 15, 1912. It is one of the most widely used datasets in data science education.

# | Feature | Description |
# |---------|-------------|
# | 'name' | Passenger name |
# | 'sex' | Sex ('male' / 'female') |
# | 'age' | Age in years |
# | 'pclass' | Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd) |
# | 'home.dest' | Home / destination |
# | 'parch' | Number of parents/children aboard |
# | 'sibsp' | Number of siblings/spouses aboard |
# | 'embarked' | Boarding Port (C = Cherbourg, Q = Queenstown, S = Southampton) |
# | 'ticket' | Ticket number |
# | 'fare' | Passenger fare (in British pounds) |
# | 'cabin' | Cabin number |
# | 'boat' | Lifeboat number (if survived) |
# | 'survived' | **Target: 0 = did not survive, 1 = survived** |
# | 'body' | Body identification number |

# | Feature | Description |
# |---------|-------------|
# | 'passenger_name' | Passenger name |
# | 'first_name' | First name |
# | 'last_name' | Last name |
# | 'passenger_sex' | Sex ('male' / 'female') |
# | 'passenger_age' | Age in years |
# | 'passenger_class' | Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd) |
# | 'home_location' | Home / destination |
# | 'parents_children' | Number of parents/children aboard |
# | 'siblings_spouses' | Number of siblings/spouses aboard |
# | 'starting_point' | Boarding Port (C = Cherbourg, Q = Queenstown, S = Southampton) |
# | 'ticket_number' | Ticket number |
# | 'ticket_price' | Passenger Price (in British pounds) |
# | 'cabin_number' | Cabin number |
# | 'lifeboat_number' | Lifeboat number (if survived) |
# | 'survival_status' | **Target: 0 = did not survive, 1 = survived** |
# | 'body_id' | Body identification number |

#RMS Titanic was a British ocean liner that sank in
#the early hours of 15 April 1912 as a result
#of striking an iceberg on her maiden voyage from Southampton,
#England, to New York City, United States. Of the estimated
#2,224 passengers and crew aboard, approximately 1,500 died (estimates vary),
#making the incident one of the deadliest peacetime sinkings of a single ship.

#Titanic Dataset
print("Titanic Dataset")
Titanic = Table.read_table('Titanic_Dataset.csv')
print(Titanic)

#Relabeling column names
Titanic = (
    Titanic
    .relabel('name', 'passenger_name')
    .relabel('sex', 'passenger_sex')
    .relabel('age', 'passenger_age')
    .relabel('pclass', 'passenger_class')
    .relabel('home.dest', 'home_location')
    .relabel('parch', 'parents_children')
    .relabel('sibsp', 'siblings_spouses')
    .relabel('embarked', 'starting_point')
    .relabel('ticket', 'ticket_number')
    .relabel('fare', 'ticket_price')
    .relabel('cabin', 'cabin_number')
    .relabel('boat', 'lifeboat_number')
    .relabel('survived', 'survival_status')
    .relabel('body', 'body_id')
)
Titanic = Titanic.select('passenger_name', 'passenger_sex', 'passenger_age', 'passenger_class', 'home_location', 'parents_children', 'siblings_spouses', 'starting_point', 'ticket_number', 'ticket_price', 'cabin_number', 'lifeboat_number', 'survival_status', 'body_id')

#Passenger_name converting Andrews, Mr. Thomas Jr ---> Thomas Andrews
passenger_name = make_array()
title = make_array()
first_name = make_array()
last_name = make_array()

for i in range(0, Titanic.num_rows):

    name = Titanic.column('passenger_name')[i]
    first_name = np.append(first_name, name.split(',')[1].split('.')[1].strip().split(' ')[0].replace('(', '').replace(')', '')) #FirstName
    last_name = np.append(last_name, name.split(',')[0]) #LastName
    passenger_name = np.append(passenger_name, name.split(',')[1].split('.')[1].strip().split(' ')[0].replace('(', '').replace(')', '') + ' ' + name.split(',')[0]) #PassengerName

Titanic = Titanic.drop('passenger_name').with_column('passenger_name', passenger_name).with_column('first_name', first_name).with_column('last_name', last_name).select('passenger_name', 'first_name', 'last_name', 'passenger_sex', 'passenger_age', 'passenger_class', 'home_location', 'parents_children', 'siblings_spouses', 'starting_point', 'ticket_number', 'ticket_price', 'cabin_number', 'lifeboat_number', 'survival_status', 'body_id')
print(Titanic)

print("\n")

#Random Forest --- Predicting Titanic Survival
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def encode(x):
    l = LabelEncoder()
    return l.fit_transform(x)

X = np.column_stack([
    encode(Titanic.column('passenger_sex')),
    Titanic.column('passenger_age'),
    Titanic.column('passenger_class'),
    encode(Titanic.column('home_location')),
    Titanic.column('parents_children'),
    Titanic.column('siblings_spouses'),
    encode(Titanic.column('starting_point'))
])

Y = encode(Titanic.column('survival_status'))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 50, stratify = Y)

model = RandomForestClassifier(
    n_estimators = 300,
    max_depth = 25,
    min_samples_leaf = 2,
    random_state = 50,
    class_weight = "balanced"
)

model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)

print(f"Random Forest Prediction (Sample Passenger): {model.predict([X_test[0]])[0]}")
print("Random Forest Accuracy:", round(accuracy_score(Y_test, Y_predict), 4))

estimator = model.estimators_[0]

plt.figure(figsize=(20,10))
plot_tree(estimator, feature_names = ["Sex", "Age", "Class", "Home_Location", "Parents_Children", "Siblings_Spouses", "Starting_Point"], class_names = True, filled = True, rounded = True, max_depth = 3)
plt.show()

#---Summary Statistics---
print("---Summary Statistics---")

#Passengers
print(f"{len(Titanic.column('passenger_name'))} passengers")

print(Titanic.labels) #Passenger features include name, age, sex, class, home

#Passenger Names
print(Titanic.select('first_name', 'passenger_name').group('first_name', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).take(range(0, 10)))
print(Titanic.select('last_name', 'passenger_name').group('last_name', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).take(range(0, 10)))

#Male & Female Passengers
print(Titanic.select('passenger_sex', 'passenger_name').group('passenger_sex', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True))

#Age of Passengers
age = make_array()

for i in range(0, Titanic.num_rows):
    if not np.isnan(Titanic.column('passenger_age')[i]):
        age = np.append(age, Titanic.column('passenger_age')[i])

print(f"{round(np.max(age), 2)} maximum passenger age")
print(f"{round(np.mean(age), 2)} mean passenger age")
print(f"{round(np.median(age), 2)} median passenger age")
print(f"{round(np.min(age), 2)} minimum passenger age")
print(f"{round(np.std(age, ddof = 0), 2)} standard deviation passenger age")
print(f"{round(np.std(age, ddof = 0)/np.mean(age) * 100, 2)}% coefficient of variation passenger age")
print(f"{round(np.max(age) - np.min(age), 2)} range passenger age")

#Passenger Class
print(Titanic.select('passenger_class', 'passenger_name').group('passenger_class', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True))

#Home_location
print(Titanic.select('home_location', 'passenger_name').group('home_location', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).take(range(0, 10)).where('home_location', are.not_equal_to('nan')))

#Parents_children
parents_children = make_array()

for i in range(0, Titanic.num_rows):
    if not np.isnan(Titanic.column('parents_children')[i]):
        parents_children = np.append(parents_children, Titanic.column('parents_children')[i])

print(f"{round(np.max(parents_children), 2)} maximum parents_children")
print(f"{round(np.mean(parents_children), 2)} mean parents_children")
print(f"{round(np.median(parents_children), 2)} median parents_children")
print(f"{round(np.min(parents_children), 2)} minimum parents_children")
print(f"{round(np.std(parents_children, ddof = 0), 2)} standard deviation parents_children")
print(f"{round(np.std(parents_children, ddof = 0)/np.mean(parents_children) * 100, 2)}% coefficient of variation parents_children")
print(f"{round(np.max(parents_children) - np.min(parents_children), 2)} range parents_children")

#Siblings_spouses
siblings_spouses = make_array()

for i in range(0, Titanic.num_rows):
    if not np.isnan(Titanic.column('siblings_spouses')[i]):
        siblings_spouses = np.append(siblings_spouses, Titanic.column('siblings_spouses')[i])

print(f"{round(np.max(siblings_spouses), 2)} maximum siblings_spouses")
print(f"{round(np.mean(siblings_spouses), 2)} mean siblings_spouses")
print(f"{round(np.median(siblings_spouses), 2)} median siblings_spouses")
print(f"{round(np.min(siblings_spouses), 2)} minimum siblings_spouses")
print(f"{round(np.std(siblings_spouses, ddof = 0), 2)} standard deviation siblings_spouses")
print(f"{round(np.std(siblings_spouses, ddof = 0)/np.mean(siblings_spouses) * 100, 2)}% coefficient of variation siblings_spouses")
print(f"{round(np.max(siblings_spouses) - np.min(siblings_spouses), 2)} range siblings_spouses")

#Starting_point
print(Titanic.select('starting_point', 'passenger_name').group('starting_point', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).where('starting_point', are.not_equal_to('nan')))

#Ticket_Price
ticket_price = make_array()

for i in range(0, Titanic.num_rows):
    if not np.isnan(Titanic.column('ticket_price')[i]):
        ticket_price = np.append(ticket_price, Titanic.column('ticket_price')[i])

print(f"${round(np.max(ticket_price), 2)} maximum ticket_price")
print(f"${round(np.mean(ticket_price), 2)} mean ticket_price")
print(f"${round(np.median(ticket_price), 2)} median ticket_price")
print(f"${round(np.min(ticket_price), 2)} minimum ticket_price")
print(f"${round(np.std(ticket_price, ddof = 0), 2)} standard deviation ticket_price")
print(f"{round(np.std(ticket_price, ddof = 0)/np.mean(ticket_price) * 100, 2)}% coefficient of variation ticket_price")
print(f"{round(np.max(ticket_price) - np.min(ticket_price), 2)} range ticket_price")

#Survival Status
print(Titanic.select('survival_status', 'passenger_name').group('survival_status', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True))

#Body_id
print(f"{len(Titanic.select('body_id').where('body_id', are.above(0)).column('body_id'))} bodies found")
print(f"{len(Titanic.select('body_id', 'survival_status').where('body_id', np.isnan).where('survival_status', 0).column('body_id'))} bodies not found")

#--- Marginal Probabilities ---
#Total number of passengers
N = Titanic.num_rows

#Survival
count_survived = Titanic.where('survival_status', are.equal_to(1)).num_rows
count_died = Titanic.where('survival_status', are.equal_to(0)).num_rows
P_survived = count_survived / N
P_died = count_died / N

#Sex
count_male = Titanic.where('passenger_sex', are.equal_to('male')).num_rows
count_female = Titanic.where('passenger_sex', are.equal_to('female')).num_rows
P_male = count_male / N
P_female = count_female / N

#Passenger class
count_class1 = Titanic.where('passenger_class', are.equal_to(1)).num_rows
count_class2 = Titanic.where('passenger_class', are.equal_to(2)).num_rows
count_class3 = Titanic.where('passenger_class', are.equal_to(3)).num_rows
P_class1 = count_class1 / N
P_class2 = count_class2 / N
P_class3 = count_class3 / N

print("--- Marginal Probabilities ---")
print(f"P(Survived = 1) = {round(P_survived, 2)}")
print(f"P(Survived = 0) = {round(P_died, 2)}")
print(f"P(Male) = {round(P_male, 2)}")
print(f"P(Female) = {round(P_female, 2)}")
print(f"P(Class1) = {round(P_class1, 2)}")
print(f"P(Class2) = {round(P_class2, 2)}")
print(f"P(Class3) = {round(P_class3, 2)}")

P_male_and_class1 = P_male * P_class1
print(f"P(MALE AND Class1) = {round(P_male_and_class1, 2)}")

# --- Conditional Probabilities ---
#Survival given sex
P_survived_given_male = Titanic.where('passenger_sex', are.equal_to('male')).where('survival_status', are.equal_to(1)).num_rows / count_male
P_survived_given_female = Titanic.where('passenger_sex', are.equal_to('female')).where('survival_status', are.equal_to(1)).num_rows / count_female

#Survival given class
P_survived_given_class1 = Titanic.where('passenger_class', are.equal_to(1)).where('survival_status', are.equal_to(1)).num_rows / count_class1
P_survived_given_class2 = Titanic.where('passenger_class', are.equal_to(2)).where('survival_status', are.equal_to(1)).num_rows / count_class2
P_survived_given_class3 = Titanic.where('passenger_class', are.equal_to(3)).where('survival_status', are.equal_to(1)).num_rows / count_class3

print("--- Conditional Probabilities ---")
print(f"P(Survived | Male) = {round(P_survived_given_male, 2)}")
print(f"P(Survived | Female) = {round(P_survived_given_female, 2)}")
print(f"P(Survived | Class1) = {round(P_survived_given_class1, 2)}")
print(f"P(Survived | Class2) = {round(P_survived_given_class2, 2)}")
print(f"P(Survived | Class3) = {round(P_survived_given_class3, 2)}")

print("Highest survival by sex: Female")
print("Lowest survival by sex: Male")
print("Difference: 53.65%")

#passenger_name = string
#passenger_sex = string
#passenger_age = float
#passenger_class = integer
#home_location = string
#parents_children = integer
#siblings_spouses = integer
#starting_point = string
#ticket_number = string
#ticket_price = float
#cabin_number = string
#lifeboat_number = string
#survival_status = integer
#body_id = float

#Bar Charts
Titanic.select('first_name', 'passenger_name').group('first_name', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).take(range(0, 10)).barh('first_name', 'count')
plt.title('Top 10 Most Common Passenger First Names')
plt.xlabel('count')
plt.ylabel('first_name')
plt.show()

Titanic.select('last_name', 'passenger_name').group('last_name', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).take(range(0, 10)).barh('last_name', 'count')
plt.title('Top 10 Most Common Passenger Last Names')
plt.xlabel('count')
plt.ylabel('last_name')
plt.show()

Titanic.select('passenger_sex', 'passenger_name').group('passenger_sex', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).barh('passenger_sex', 'count')
plt.title('Passenger Sex Distribution')
plt.xlabel('count')
plt.ylabel('passenger_sex')
plt.show()

Titanic.select('passenger_class', 'passenger_name').group('passenger_class', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).barh('passenger_class', 'count')
plt.title('Passenger Class Distribution')
plt.xlabel('count')
plt.ylabel('passenger_class')
plt.show()

Titanic.select('home_location', 'passenger_name').where('home_location', are.not_equal_to('nan')).group('home_location', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).take(range(0, 10)).barh('home_location', 'count')
plt.title('Top 10 Most Common Passenger Home Locations')
plt.xlabel('count')
plt.ylabel('home_location')
plt.show()

Titanic.select('starting_point', 'passenger_name').where('starting_point', are.not_equal_to('nan')).group('starting_point', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).barh('starting_point', 'count')
plt.title('Starting Point Distribution')
plt.xlabel('count')
plt.ylabel('starting_point')
plt.show()

Titanic.select('survival_status', 'passenger_name').group('survival_status', collect = len).relabel('passenger_name len', 'count').sort('count', descending = True).barh('survival_status', 'count')
plt.title('Survival Status Distribution')
plt.xlabel('count')
plt.ylabel('survival_status')
plt.show()

#Histograms
Titanic.select('passenger_age').where('passenger_age', are.above(-1)).hist('passenger_age', bins = 10)
plt.title('Passenger Age Distribution')
plt.xlabel('passenger_age')
plt.ylabel('count')
plt.show()

Titanic.select('ticket_price').where('ticket_price', are.above(-1)).hist('ticket_price', bins = 25)
plt.title('Ticket Price Distribution')
plt.xlabel('ticket_price')
plt.ylabel('count')
plt.show()

#Box Plot
Titanic.select('passenger_age').where('passenger_age', are.above(-1)).boxplot(vert = False)
plt.title('Passenger Age Distribution')
plt.xlabel('')
plt.ylabel('')
plt.show()

Titanic.select('ticket_price').where('ticket_price', are.above(-1)).boxplot(vert = False)
plt.title('Ticket Price Distribution')
plt.xlabel('')
plt.ylabel('')
plt.show()

#Normality Testing Q-Q Plots
import scipy.stats as stats

#age array
age = make_array()

for i in range(0, Titanic.num_rows):
    if not np.isnan(Titanic.column('passenger_age')[i]):
        age = np.append(age, Titanic.column('passenger_age')[i])

#ticket_price array
ticket_price = make_array()

for i in range(0, Titanic.num_rows):
    if not np.isnan(Titanic.column('ticket_price')[i]):
        ticket_price = np.append(ticket_price, Titanic.column('ticket_price')[i])

#Q-Q Plot for Age
plt.figure()
stats.probplot(age, dist = "norm", plot = plt)
plt.title('Q-Q Plot for Passenger Age')
plt.xlabel('theoretical quantiles')
plt.ylabel('passenger_age')
plt.show()

#Q-Q Plot for Ticket Price
plt.figure()
stats.probplot(ticket_price, dist = "norm", plot = plt)
plt.title('Q-Q Plot for Ticket Price')
plt.xlabel('theoretical quantiles')
plt.ylabel('ticket_price')
plt.show()

