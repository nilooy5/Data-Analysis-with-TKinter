import pandas as pd

df = pd.read_csv('Files_Assignment3/mycsv.csv')

df = df.iloc[:, [2, 4, 5, 6]]

# print(df.keys())
# print(df.values)

"""
• Change SIS User ID to ID
• Change Submit Assignment 1 (57584) to A1
• Change Submit Assignment 2 (57585) to A2, and
• Change Submit Assignment 3 (57473) to Exam.
"""
df_new = df.rename(columns={'SIS User ID': 'ID',
                            'Submit Assignment 1 (57584)': 'A1',
                            'Submit Assignment 2 (57585)': 'A2',
                            'Submit Assignment 3 (57473)': 'Exam'})


"""select all rows from df_new['ID'] which start with 'u' or 's'"""
df_new = df_new[df_new['ID'].str.startswith('u') | df_new['ID'].str.startswith('s')]

print(df_new)

"""
separate df_new to 2 separate groups where first group has df_new['ID'] starts with u and
the second group has df_new['ID'] starts with s
"""
df_new_u = df_new[df_new['ID'].str.startswith('u')]
print("starts with U:")
print(df_new_u)
df_new_s = df_new[df_new['ID'].str.startswith('s')]
print("starts with S:")
print(df_new_s)

"""parse values of df_new_s['A1'] to numeric"""
df_new_s['A1'] = pd.to_numeric(df_new_s['A1'], errors='coerce')
df_new_s['A2'] = pd.to_numeric(df_new_s['A2'], errors='coerce')
df_new_s['Exam'] = pd.to_numeric(df_new_s['Exam'], errors='coerce')

"""sort data of df_new_s by A1"""
df_new_s = df_new_s.sort_values(by='A1')
print("SORTED starts with S:")
print(df_new_s)

"""parse values of df_new_u['A1'] to numeric"""
df_new_u['A1'] = pd.to_numeric(df_new_u['A1'], errors='coerce')
df_new_u['A2'] = pd.to_numeric(df_new_u['A2'], errors='coerce')
df_new_u['Exam'] = pd.to_numeric(df_new_u['Exam'], errors='coerce')

"""sort data of df_new_u by A1"""
df_new_u = df_new_u.sort_values(by='A1')
print("SORTED starts with U:")
print(df_new_u)

writer = pd.ExcelWriter('Files_Assignment3/myexcel.xls', engine='xlsxwriter')

df_new_s.to_excel(writer, sheet_name='SID')
df_new_u.to_excel(writer, sheet_name='UID')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

