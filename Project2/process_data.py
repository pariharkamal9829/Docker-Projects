import pandas as pd

# Read the CSV file
df = pd.read_csv('data/data.csv')

# Print statistical summary
print(df.describe())
