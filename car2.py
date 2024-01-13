
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
car_data = pd.read_csv(url)


# Sidebar for region selection
region = st.sidebar.selectbox('Select Region', car_data['continent'].unique())

# Filter data based on the selected region
if region != 'All':
    car_data = car_data[car_data['continent'] == region]

# Display the filtered dataset
st.subheader('Filtered Dataset')
st.write(car_data)

# Correlation matrix for numeric columns
st.subheader('Correlation Matrix (Numeric Columns Only)')
numeric_columns = car_data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_columns.corr()

# Plotting the correlation matrix heatmap using Seaborn
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot()

st.subheader('Correlation Matrix (Numeric Columns Only)')
numeric_columns = car_data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_columns.corr()

st.subheader('Distribution Analysis')
for column in numeric_columns.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(data=car_data, x=column, kde=True)
    plt.title(f'Distribution of {column}')
    st.pyplot()

# Clear the Matplotlib plot cache to avoid unexpected behavior
plt.close('all')