import pandas as pd
# !wget https://drive.google.com/file/d/1E3bwvYGf1ig32RmcYiWc0IXPN-mD_bI_/view

df = pd.read_csv('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/002/276/original/tips.csv')
print(df.info())

print('*'*50)
print('List of columns')
print('*'*50)
print(df.columns)
print(df.keys())
print('*'*50)

print(df['day'])
print(df[['day', 'time']])

print(df['day'].unique())

print('*'*50)
print('Each day number of rows present')
print('*'*50)
print(df['day'].value_counts())
print('*'*50)

print('Rename column')
print('*'*50)
# print(df.rename({ "day": "Day" }, axis=1, inplace=True))
print(df.rename({ "day": "Day" }, axis=1))

print('*'*50)
print('Delete a column')
print('*'*50)
# print(df.drop('day', axis=1, inplace=True))
print(df.drop('day', axis=1))
# print(df.drop(columns=["day"]))


