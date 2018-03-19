import pandas as pd
import os

# create list of excel file
listOfFiles = os.listdir()
listOfExcelFiles =list( filter(lambda f: f.endswith(('.xlsx')), listOfFiles) )
print(listOfExcelFiles)

excelFile = pd.ExcelFile("excelExample.xlsx")
# Print the sheet names
print(excelFile.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = excelFile.parse('Sheet1')

df1 = pd.read_excel(excelFile, 'Sheet1')
df2 = pd.read_excel(excelFile, 'Sheet2')

#find all column names
columnnames = df1.columns
print(columnnames)

#find column value as a list
col0 = list(df1['col1'])
print('col10=',col0)

#find unique values from column
print(df1.col1.unique())

