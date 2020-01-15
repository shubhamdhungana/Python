from matplotlib import pyplot as plt




dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [4000, 45000, 50000, 55000, 60000,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y, label='All Devs')
#dev_x and dev_y are respectively x-axis and y-axis





# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(dev_x, py_dev_y, label='Python')





plt.xlabel('Ages')

plt.ylabel('Median Salary')

plt.title('Median Salary (USD) by Age')
#Shows the title above the figure

plt.legend()
#This shows indexing of the chart or figure

plt.show()
