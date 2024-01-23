import pandas as pd

# Assuming your CSV file is named 'restaurants.csv'
file_path = 'CSV FILENAME'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Check for duplicates based on all columns
duplicates = df[df.duplicated(subset=['Name', 'Address', 'Latitude', 'Longitude'], keep=False)]

# Print the duplicate entries, if any
if not duplicates.empty:
    print("Duplicate entries found:")
    print(duplicates)
else:
    print("No duplicate entries found.")
