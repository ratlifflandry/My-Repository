from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Tornado Dataset
Tornado = Table.read_table('Cleaned_US_Tornado_Dataset.csv')
print(Tornado)
print(Tornado.num_rows)
print(Tornado.num_columns)
print(Tornado.labels)

#Summary Statistics of Tornado including max, mean, median, min, standard deviation
print("Summary Statistics:")
print(f"Maximum EF Rating: {round(np.max(Tornado.column('Enhanced Fujita Scale')), 2)}")
print(f"Average EF Rating: {round(np.mean(Tornado.column('Enhanced Fujita Scale')), 2)}")
print(f"Standard Deviation EF Rating: {round(np.std(Tornado.column('Enhanced Fujita Scale'), ddof = 0), 2)}")
print(f"Median EF Rating: {round(np.median(Tornado.column('Enhanced Fujita Scale')), 2)}")
print(f"Minimum EF Rating: {round(np.min(Tornado.column('Enhanced Fujita Scale')), 2)}")
print(f"Coefficient of Variation: {round(np.std(Tornado.column('Enhanced Fujita Scale'))/np.mean(Tornado.column('Enhanced Fujita Scale')) * 100 ,2)}%")

#Average Tornadoes per Year
print("Average Number of Tornadoes per Year:")
print(np.average(Tornado.group('Year').column('count')))

#Average Deaths per Year
print("Average Number of Deaths per Year:")
print(np.average(Tornado.group('Year', collect = np.sum).column('Fatalities sum')))

#Most Powerful Tornados by Date
print("---Most Powerful Tornadoes---")
print(Tornado.where('Enhanced Fujita Scale', are.equal_to(5)).sort('Decimal Date', descending = True))

#Bell Curve of Tornado EF-Rating
mean = np.mean(Tornado.column('Enhanced Fujita Scale'))
std_dev = np.std(Tornado.column('Enhanced Fujita Scale'))

def PDF(x):
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean)/std_dev) ** 2)

x = np.linspace(-5, 5, 1000)
y = PDF(x)

plt.plot(x, y, color='blue', label='Standard Normal PDF')
plt.xlabel('EF Rating')
plt.ylabel('Density')
plt.title('Normal Distribution of Tornado EF-Ratings')
plt.legend()
plt.show()

#Histogram of Distribution of Tornado EF Ratings
Tornado.hist('Enhanced Fujita Scale', bins = 5)
plt.xlabel('Enhanced Fujita Scale')
plt.ylabel('Percent')
plt.title('Distribution of Tornado EF-Ratings')
plt.show()

#Box Plot of Tornado EF Ratings
Tornado.select('Enhanced Fujita Scale').boxplot(vert = False)
plt.title('Tornado EF-Rating Distribution')
plt.xlabel('')
plt.ylabel('')
plt.show()

#Bar Chart of Number of Tornadoes by EF Rating
Tornado.group('Enhanced Fujita Scale').relabel('count', 'Count').barh('Enhanced Fujita Scale', 'Count')
plt.xlabel('Count')
plt.ylabel('Enhanced Fujita Scale')
plt.title('Number of Tornadoes by EF-Rating')
plt.show()

#Pie Chart of Proportion of Tornadoes by EF Rating
EF_num = Tornado.num_rows
EF_0 = Tornado.where('Enhanced Fujita Scale', are.equal_to(0)).num_rows
EF_1 = Tornado.where('Enhanced Fujita Scale', are.equal_to(1)).num_rows
EF_2 = Tornado.where('Enhanced Fujita Scale', are.equal_to(2)).num_rows
EF_3 = Tornado.where('Enhanced Fujita Scale', are.equal_to(3)).num_rows
EF_4 = Tornado.where('Enhanced Fujita Scale', are.equal_to(4)).num_rows
EF_5 = Tornado.where('Enhanced Fujita Scale', are.equal_to(5)).num_rows

EF = Table().with_columns(
    'Enhanced Fujita Scale', make_array('EF-0', 'EF-1', 'EF-2', 'EF-3', 'EF-4', 'EF-5'),
    'Percent', make_array(EF_0/EF_num * 100, EF_1/EF_num * 100, EF_2/EF_num * 100, EF_3/EF_num * 100, EF_4/EF_num * 100, EF_5/EF_num * 100)
)
plt.pie(EF.column('Percent'), labels = EF.column('Enhanced Fujita Scale'))
plt.title('Proportion of Tornadoes by EF-Rating')
plt.show()

#Bar Chart of Most Powerful Tornados
Tornado.where('Enhanced Fujita Scale', are.equal_to(5)).sort('Fatalities', descending = True).take(range(0, 10)).barh('Date State', 'Fatalities')
plt.xlabel('Fatalities')
plt.ylabel('Date State')
plt.title('Top 10 Deadliest EF-5 Tornadoes')
plt.show()

#Line Plot of Average EF-Rating by Year
Tornado.group('Year', collect = np.average).relabel('Enhanced Fujita Scale average', 'Enhanced Fujita Scale').plot('Year', 'Enhanced Fujita Scale')
plt.xlabel('Year')
plt.ylabel('Enhanced Fujita Scale')
plt.title('Tornado EF-Rating by Year')
plt.show()

#Bar Chart of Top 10 Longest-Track Tornadoes
Tornado.sort('Length (km)', descending = True).take(range(0, 10)).barh('Date State', 'Length (km)')
plt.xlabel('Length (km)')
plt.ylabel('Date State')
plt.title('Top 10 Longest-Track Tornadoes')
plt.show()

#Bar Chart of Top 10 Widest Tornadoes
Tornado.sort('Width (m)', descending = True).take(range(0, 10)).barh('Date State', 'Width (m)')
plt.xlabel('Width (m)')
plt.ylabel('Date State')
plt.title('Top 10 Widest Tornadoes')
plt.show()

#Bar Chart of Number of Tornadoes by State
Tornado.group('State').relabel('count', 'Count').sort('Count', descending = True).barh('State', 'Count')
plt.xlabel('Count')
plt.ylabel('State')
plt.title('Number of Tornadoes by State')
plt.show()

#Bar Chart of Top 10 States with the Most Tornado Fatalities
Tornado.group('State', collect = np.sum).relabel('Fatalities sum', 'Fatalities').sort('Fatalities', descending = True).take(range(0, 10)).barh('State', 'Fatalities')
plt.xlabel('Fatalities')
plt.ylabel('State')
plt.title('Top 10 States with the Most Tornado Fatalities')
plt.show()

#Line Plot of Number of Tornadoes by Year
Tornado.group('Year').relabel('count', 'Count').plot('Year', 'Count')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Number of Tornadoes by Year')
plt.show()

#Bar Chart of Top 10 Years with the Most Tornadoes
Tornado.group('Year').relabel('count', 'Count').sort('Count', descending = True).take(range(0, 10)).barh('Year', 'Count')
plt.xlabel('Count')
plt.ylabel('Year')
plt.title('Top 10 Years with the Most Tornadoes')
plt.show()

#Bar Chart of Top 10 Days with the Most Tornadoes
Tornado.group('Date').relabel('count', 'Count').sort('Count', descending = True).take(range(0, 10)).barh('Date', 'Count')
plt.xlabel('Count')
plt.ylabel('Date')
plt.title('Top 10 Days with the Most Tornadoes')
plt.show()

#Bar Chart of Top 10 Years with the Most EF-5 Tornadoes
Tornado.where('Enhanced Fujita Scale', are.equal_to(5)).group('Year').relabel('count', 'Count').sort('Count', descending = True).take(range(0, 10)).barh('Year', 'Count')
plt.xlabel('Count')
plt.ylabel('Year')
plt.title('Top 10 Years with the Most EF-5 Tornadoes')
plt.show()

#Line Plot of Tornado Fatalities Over Time
Tornado.group('Year', collect = np.sum).relabel('Fatalities sum', 'Fatalities').plot('Year', 'Fatalities')
plt.xlabel('Year')
plt.ylabel('Fatalities')
plt.title('Tornado Fatalities Over Time')
plt.show()

#Scatter Plot of Tornado Fatalities Over Time
Tornado.scatter('Decimal Date', 'Fatalities')
plt.xlabel('Decimal Date')
plt.ylabel('Fatalities')
plt.title('Tornado Fatalities Over Time')
plt.show()

#U.S. Map of Tornadoes
from cartopy import crs as ccrs
import cartopy.feature as cfeature

latitude = Tornado.column('Start Latitude')
longitude = Tornado.column('Start Longitude')

fig = plt.figure(figsize = (12, 8))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.scatter(longitude, latitude, color = "blue", s = 0.25, alpha = 0.25, transform = ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linewidth = 1)
ax.add_feature(cfeature.STATES, linewidth = 0.5)
ax.set_title('US Tornadoes')
ax.set_extent([-130, -55, 15, 50]) #West_Longitude, East_Longitude, South_Latitude, North_Latitude
plt.show()

#Linear Regression of Length (km) & Width (m)
#Are length and width correlated?
x = np.array(Tornado.column('Length (km)'))
y = np.array(Tornado.column('Width (m)'))

coefficients = np.polyfit(x, y, 1)
a = coefficients[0] # Slope
b = coefficients[1] # Y-Intercept

x_fit = x
y_fit = a * x + b

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label=f'y = {a:.3f}x + {b:.3f}')
plt.title('Linear Regression')
plt.xlabel('Length (km)')
plt.ylabel('Width (m)')
plt.legend()
plt.grid(True)
plt.show()

r = np.corrcoef(x, y)[0, 1]
print(f"Linear Equation: y = {a:.3f}x + {b:.3f}")
print(f"Correlation R: {r}")

#Polynomial Regression of Length (km) & Width (m)
#Are length and width correlated?
x = np.array(Tornado.column('Length (km)'))
y = np.array(Tornado.column('Width (m)'))

#y = a * x^2 + b * x + c
coefficients = np.polyfit(x, y, 2)
a = coefficients[0]     #Quadratic
b = coefficients[1]     #Slope
c = coefficients[2]     #Y-Intercept

x_fit = np.linspace(min(x), max(x), 65_813) #Starting Point, Ending Point, and Number of Points
y_fit = a * x_fit ** 2 + b * x_fit + c

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, color='blue', label=f'y = {a:.3f}x^2+{b:.3f}x+{c:.3f}')
plt.title('Polynomial Regression')
plt.xlabel('Length (km)')
plt.ylabel('Width (m)')
plt.legend()
plt.grid(True)
plt.show()

r = np.corrcoef(y, y_fit)[0, 1]
print(f"Polynomial Equation: y = {a:.3f}x^2+{b:.3f}x+{c:.3f}")
print(f"Correlation R: {r}")

#Hypothesis Test of Pre-2000s and Post-2000s
#Is there a significant difference in pre-2000s & post-2000s
pre_2000 = Tornado.where('Year', are.below(2000)).column('Enhanced Fujita Scale')
post_2000 = Tornado.where('Year', are.above_or_equal_to(2000)).column('Enhanced Fujita Scale')

X1 = np.mean(pre_2000)
S1 = np.std(pre_2000, ddof = 0)
N1 = len(pre_2000)

X2 = np.mean(post_2000)
S2 = np.std(post_2000, ddof = 0)
N2 = len(post_2000)

print("Summary Statistics:")
print("Pre-2000s")
print(f"Mean: {X1}")
print(f"Standard Deviation: {S1}")
print(f"Count: {N1}")
print("Post-2000s")
print(f"Mean: {X2}")
print(f"Standard Deviation: {S2}")
print(f"Count: {N2}")

#Population Comparison
#Null Hypothesis H₀: μ₁ = μ₂ (Tornadoes did not get stronger)
#Alternative Hypothesis H₁: μ₁ != μ₂ (Tornadoes did get stronger or weaker)
z_score = (X1 - X2) / np.sqrt((S1**2 / N1) + (S2**2 / N2))
print(f"Z-Score: {abs(z_score)}")

x_right = np.linspace(abs(z_score), 100, 1_000_000)
dx = x_right[1] - x_right[0]
y_right = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_right**2)
right = np.sum(y_right * dx)

x_left = np.linspace(-100, -abs(z_score), 1_000_000)
dx = x_left[1] - x_left[0]
y_left = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_left**2)
left = np.sum(y_left * dx)

p_value = left + right
print(f"P-value (Riemann sum): {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis — there is a significant difference in means.")
else:
    print("Conclusion: Fail to reject the null — no significant difference detected.")

#Plot Standard Normal Curve with p-value shaded
def PDF(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

x = np.linspace(-5, 5, 1000)
y = PDF(x)
plt.plot(x, y, color='blue', label='Standard Normal PDF')
plt.fill_between(x, y, where=(x >= abs(z_score)), color='red', alpha=0.5)
plt.fill_between(x, y, where=(x <= -abs(z_score)), color='red', alpha=0.5)
plt.xlabel('Z')
plt.ylabel('Density')
plt.title('Standard Normal Curve with Two-Tailed P-Value Shaded')
plt.legend()
plt.show()

#Neural Network --- Predicting Tornado EF-Rating
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.column_stack([Tornado.column('Start Latitude'), Tornado.column('Start Longitude'), Tornado.column('Year'), Tornado.column('Month'), Tornado.column('Day'), Tornado.column('Length (km)'), Tornado.column('Width (m)'), Tornado.column('Fatalities')])
Y = Tornado.column('Enhanced Fujita Scale')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 50, stratify = Y)

model = MLPClassifier(hidden_layer_sizes = (16, 8), activation = 'relu', solver = 'adam', max_iter = 500, random_state = 50)
model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)                                                                          #Latitude, Longitude, Year, Month, Day, Length, Width, Deaths
print(f"Neural Network Prediction (Dallas, TX @ May 25, 2025 | 10 km traveled, 500 m wide, 25 deaths): EF-{model.predict([[32.776, -96.797, 2025, 5, 25, 10, 500, 25]])[0]}")
print("Neural Network Accuracy:", round(accuracy_score(Y_test, Y_predict), 4))

#Decision Tree --- Predicting Tornado EF-Rating
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.column_stack([Tornado.column('Start Latitude'), Tornado.column('Start Longitude'), Tornado.column('Year'), Tornado.column('Month'), Tornado.column('Day'), Tornado.column('Length (km)'), Tornado.column('Width (m)'), Tornado.column('Fatalities')])
Y = Tornado.column('Enhanced Fujita Scale')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 50, stratify = Y)

model = DecisionTreeClassifier(max_depth = 25, min_samples_leaf = 2, random_state = 50, class_weight = "balanced")
model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)
print(f"Decision Tree Prediction (Dallas, TX @ May 25, 2025 | 10 km traveled, 500 m wide, 25 deaths): EF-{model.predict([[32.776, -96.797, 2025, 5, 25, 10, 500, 25]])[0]}")
print("Decision Tree Accuracy:", round(accuracy_score(Y_test, Y_predict), 4))

plt.figure(figsize=(20,10))
plot_tree(model, feature_names = ["Latitude", "Longitude", "Year", "Month", "Day", "Length", "Width", "Fatalities"], class_names = True, filled = True, rounded = True, max_depth = 3)
plt.show()

#Random Forest --- Predicting Tornado EF-Rating
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = np.column_stack([Tornado.column('Start Latitude'), Tornado.column('Start Longitude'), Tornado.column('Year'), Tornado.column('Month'), Tornado.column('Day'), Tornado.column('Length (km)'), Tornado.column('Width (m)'), Tornado.column('Fatalities')])
Y = Tornado.column('Enhanced Fujita Scale')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 50, stratify = Y)

model = RandomForestClassifier(n_estimators = 300, max_depth = 25, min_samples_leaf = 2, random_state = 50, class_weight = "balanced")
model.fit(X_train, Y_train)

Y_predict = model.predict(X_test)
print(f"Random Forest Prediction (Dallas, TX @ May 25, 2025 | 10 km traveled, 500 m wide, 25 deaths): EF-{model.predict([[32.776, -96.797, 2025, 5, 25, 10, 500, 25]])[0]}")
print("Random Forest Accuracy:", round(accuracy_score(Y_test, Y_predict), 4))

estimator = model.estimators_[0]
plt.figure(figsize=(20,10))
plot_tree(estimator, feature_names = ["Latitude", "Longitude", "Year", "Month", "Day", "Length", "Width", "Fatalities"], class_names = True, filled = True, rounded = True, max_depth = 3)
plt.show()

#K-Means Clustering --- Clustering Tornado EF Ratings
from sklearn.cluster import KMeans

X = np.column_stack([Tornado.column('Enhanced Fujita Scale'), Tornado.column('Fatalities')])

kmeans = KMeans(n_clusters = 5, n_init = 10)
kmeans.fit(X)

labels = kmeans.labels_
centers = kmeans.cluster_centers_

plt.scatter(X[:,0], X[:,1], c = labels)
plt.scatter(centers[:,0], centers[:,1], s = 200, marker = 'X')
plt.title('K-Means Clustering')
plt.xlabel('Enhanced Fujita Scale')
plt.ylabel('Fatalities')
plt.show()
