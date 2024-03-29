# -*- coding: utf-8 -*-
"""LVADSUSR90-Jagadeesh-FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b3qdXcniKsxAQ6T-UbQ93y8ajIGXDFu1
"""

#1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
num_rows,num_columns = data.shape
print("number of rows:",num_rows)
print("number of columns:",num_columns)
print()
print("Dta types of columns:")
print(data.dtypes)
print()
print("summary statistics")
print(data.describe())
print()
#missing dara
print("Misiing values")
print(data.isnull().sum())

#2
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
missing_values = data.isnull().sum()
print("Missing values:")
print(missing_values)
print()
data = data.dropna()
duplicate_entries = data.duplicated().sum()
print("number of duplicate entries:",duplicate_entries)
print()
data = data.drop_duplicates()

#3
import pandas as pd
data = pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
numerical_data = data.select_dtypes(include=['int64', 'float64'])
summary_stats = numerical_data.describe()
mode_values = numerical_data.mode().iloc[0]
data_range = numerical_data.max() - numerical_data.min()
summary_stats.loc['mode'] = mode_values
summary_stats.loc['range'] = data_range
variance = numerical_data.var()
std_deviation = numerical_data.std()
summary_stats.loc['variance'] = variance
summary_stats.loc['std_deviation'] = std_deviation
print("Summary statistics for Descriptive Statistics:")
print(summary_stats)

#4
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Histogram to visualize distribution of Profit
plt.figure(figsize=(10, 6))
sns.histplot("Profit", kde=True)
plt.title('Histogram of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Sales')
plt.show()

# Scatter plot to visualize relationship between Profit and Sales
plt.figure(figsize=(10, 6))
#sns.scatterplot (x="Profit", y="Sales", data=df)
plt.title('Scatter Plot of Profit vs Sales')
plt.xlabel('Profit')
plt.ylabel('Sales')
plt.show()

# Box plot to visualize distribution of numerical data and identify outliers
plt.figure(figsize=(10, 6))
sns.boxplot (x="Order Date", y="Sales")
plt.title('Box Plot of Order Date vs Sales')
plt.xlabel('Order Date')
plt.ylabel('Sales')
plt.show()

# Bar plot to visualize distribution of categorical data
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=df)
plt.title('Bar Plot of Categorical Column')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.show()

#5
import pandas as pd
data = pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
variable1 = "Profit"
variable2 = "Sales"
variable3 = "Quantity"
variable4 = "Category"
correlation = data[variable1].corr(data[variable2])
print(f"Correlation between '{variable1}' and '{variable2}': {correlation}")

#6
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")

# Identify and Investigate Outliers or Unusual Data
# Example: Investigating outliers in the 'total day minutes' column

# Visual Inspection (Box Plot)
plt.figure(figsize=(8, 6))
plt.boxplot(data['Profit'])
plt.title('Box Plot of Profit')
plt.ylabel('Total Profit')
plt.show()

# Summary Statistics
summary_stats = data['Profit'].describe()
print("Summary Statistics for Total Profits:")
print(summary_stats)
print()

# Statistical Tests (Z-score)
# Calculate Z-score for each data point
z_scores = (data['Profit'] - data['Profit'].mean()) / data['Profit'].std()
# Threshold for identifying outliers (e.g., z_score > 3 or z_score < -3)
outliers = data[abs(z_scores) > 3]
print("Potential Outliers based on Z-score:")
print(outliers['Profit'])

#7a Trends analysis:
# 1.analyze the scales and profit trends over the year. Are there any noticeable patterns or seasonal variations?
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
yearly_data = data.groupby('Year').agg({
    'Sales': 'sum',
    'Profit': 'sum'}).reset_index()
plt.figure(figsize=(6, 6))
plt.plot(yearly_data['Year'], yearly_data['Sales'], marker='o', label='Total Sales', color='blue')
plt.plot(yearly_data['Year'], yearly_data['Profit'], marker='o', label='Total Profit', color='green')
plt.title('Sales and Profit Trends vs the Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.xticks(yearly_data['Year'])
plt.legend()
plt.show()
category_sales = data.groupby(['Year', 'Category'])['Sales'].sum().unstack()
plt.figure(figsize=(12, 8))
category_sales.plot(kind='line', marker='o')
plt.title('Sales Trend of Each Product Category Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks(yearly_data['Year'])
plt.legend(title='Category')
plt.show()

#7b Customer analysis
customer_group = data.groupby('EmailID')
orders_per_customer = customer_group.size()
total_sales_per_customer = customer_group['Sales'].sum()
customer_stats = pd.DataFrame({
    'Number of Orders': orders_per_customer,
    'Total Sales': total_sales_per_customer
})
sorted_customers = customer_stats.sort_values(by=['Number of Orders', 'Total Sales'], ascending=False)
top_5_customers = sorted_customers.head(5)
print("Top 5 Customers:")
print(top_5_customers)

"""#7

**Trend Analysis**
The dataset consists of Walmart_Dataset with several features including Order ID, Order Date, ship Date, Email ID,Geography,Category,Sales,Quantity and Profit
The dataset contains 3203 rows and 10 columns.
There are no missing values in the dataset.
Most columns contain String values, while some are Float.
Categorical features such as Profit, Sales, and Qauntity were explored.
Frequency distributions and proportions were examined to understand the distribution of Profit vs Sales
Correlation analysis was conducted between profit and sales to identify relationships.
Strong positive correlations were observed between profit and sales as 0.6474771769464481
Visualizations such as histograms, box plots, and scatter plots were used to gain insights into the data distribution and relationships.
Visual inspection helped identify patterns and anomalies in the data.

**Customer Analysis :**
Findings and Insights:
Profits and Sales showed a wide range of values, with some outliers suggesting potential anomalies or high Sales
Most of the orders were delivered within or less than 3 - 4 days
All the orders are from United States of different states
espicially most of the orders were recorded from the los angels california and also
top profits were recorded from the  order ID of CA-2014-140151 worth 6719.9808 USD
top quantities were placed by 11 people with order quantity of 14
top sales were recorded by the order ID of CA-2014-140151 of worth 13999.96 USD

 **Comprenhensive Analytics**:
Insights from the analysis could inform targeted marketing strategies over sales vs profit, customer retention efforts, and service improvements.
Further analysis, such as predictive modeling or segmentation, could be conducted based on the insights gained from EDA.
Walmart has to increase the discounts on the product categories which are showing less sales comparetely other category products and also increase the delivery of the speed for few states.
Few state like texas esp austin location sales were very less it has to be improved by providing additional discounts and also prices should not be very aggresive they should be less compared to the local stores and the other compitetors
Overall, the EDA provided valuable insights into the Walmart_Dataset, highlighting patterns, relationships, and potential areas for further investigation and action.All the orders are from United States of different states espicially most of the orders were recorded from the los angels california and also top profits were recorded from the order ID of CA-2014-140151 worth 6719.9808 USD top quantities were placed by 11 people with order quantity of 14 top sales were recorded by the order ID of CA-2014-140151 of worth 13999.96 USD
"""