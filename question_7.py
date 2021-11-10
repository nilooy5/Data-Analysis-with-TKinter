import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sid = pd.read_excel('Files_Assignment3/myexcel.xls', sheet_name='SID')
uid = pd.read_excel('Files_Assignment3/myexcel.xls', sheet_name='UID')


print(sid)
print(uid)

plt.hist(sid['Exam'])
plt.show()
