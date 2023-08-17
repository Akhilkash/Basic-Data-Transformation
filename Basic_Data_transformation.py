import pandas as pd

# Reading CSV file
input_file = "Input.csv"
data=pd.read_csv(input_file)

# Applying transformations
data['Age'] = data['Age'] + 1
data['Location'] = data['Location'].str.upper()
data['Name'] = data['Name'].str.upper()

# Saving the transformed data to a new file
output_file = 'output.csv'
data.to_csv(output_file, index=False)

print("Data transformation complete. Transformed data is saved to 'output.csv'.")