import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sid = pd.read_excel('Files_Assignment3/myexcel.xls', sheet_name='SID')
uid = pd.read_excel('Files_Assignment3/myexcel.xls', sheet_name='UID')

print(sid)
print(uid)

fig, axs = plt.subplots(2, 3)
axs[0, 0].hist(uid['A1'])
axs[0, 0].set_title('UID A1')
axs[0, 0].set_xlabel('Mark')
axs[0, 0].set_ylabel('Number of Students')

axs[0, 1].hist(uid['A2'])
axs[0, 1].set_title('UID A2')
axs[0, 1].set_xlabel('Mark')
axs[0, 1].set_ylabel('Number of Students')

axs[0, 2].hist(uid['Exam'])
axs[0, 2].set_title('UID Exam')
axs[0, 2].set_xlabel('Mark')
axs[0, 2].set_ylabel('Number of Students')

axs[1, 0].hist(sid['A1'])
axs[1, 0].set_title('SID A1')
axs[1, 0].set_xlabel('Mark')
axs[1, 0].set_ylabel('Number of Students')

axs[1, 1].hist(sid['A2'])
axs[1, 1].set_title('SID A2')
axs[1, 1].set_xlabel('Mark')
axs[1, 1].set_ylabel('Number of Students')

axs[1, 2].hist(sid['Exam'])
axs[1, 2].set_title('SID Exam')
axs[1, 2].set_xlabel('Mark')
axs[1, 2].set_ylabel('Number of Students')

# plt.hist(sid['Exam'])
plt.show()
