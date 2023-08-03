import numpy as np

base_attribute_values =  np.loadtxt('tables/base_attribute_values.csv', skiprows=1, delimiter=',', usecols=range(1,5))
print(base_attribute_values)
base_skill_values = np.loadtxt('tables/base_skill_values.csv', skiprows=1, delimiter=',', usecols=range(1,25))
print(base_skill_values)
