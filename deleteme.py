import pandas as pd

# Create a pandas Series
series_data = pd.Series([10, 20, 30, 40, 50], name='Numbers')

# Create a pandas DataFrame
df_data = pd.DataFrame({'Numbers': [10, 20, 30, 40, 50]})

# Accessing values
print("Pandas Series:")
print(series_data)
print("\nFirst value in Series:", series_data[0])

print("\nPandas DataFrame:")
print(df_data)
print("\nFirst value in DataFrame:")
print(df_data['Numbers'][0])