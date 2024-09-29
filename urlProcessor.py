# Install necessary packages
# pip install pandas openpyxl

import pandas as pd
from openpyxl import load_workbook

# File paths
file_path = 'C:/Users/HR/Desktop/medica links.xlsx'  # Path to the Excel file you want to modify
new_sheet_name = 'sortedLinks'  # The name for the new sheet to be created

# Load the existing workbook
workbook = load_workbook(file_path)
print("workbook loaded")
# Load the data from the first sheet or specify the sheet name
df = pd.read_excel(file_path, sheet_name='Sheet1', engine='openpyxl')

# Process the DataFrame (e.g., remove alternating rows)
df = df.iloc[::2, :].reset_index(drop=True)  # This keeps every second row (removing odd-indexed rows)

# Save the modified DataFrame to a new sheet in the same workbook
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    # Add the new sheet
    df.to_excel(writer, sheet_name=new_sheet_name, index=False)

print("task completed")
