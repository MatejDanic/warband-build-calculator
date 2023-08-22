import numpy as np

book_attribute_values =  np.loadtxt('tables/book_attribute_values.csv', skiprows=1, delimiter=',', usecols=range(1,5))
#print(base_attribute_values)
book_skill_values = np.loadtxt('tables/book_skill_values.csv', skiprows=1, delimiter=',', usecols=range(1,25))
#print(base_skill_values)
