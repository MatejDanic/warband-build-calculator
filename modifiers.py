import numpy as np

gender_attribute_modifiers = np.loadtxt('tables/gender_attribute_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,5))
print(gender_attribute_modifiers)

father_attribute_modifiers = np.loadtxt('tables/father_attribute_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,5))
print(father_attribute_modifiers)
father_skill_modifiers = np.loadtxt('tables/father_skill_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,25))
print(father_skill_modifiers)

early_life_attribute_modifiers = np.loadtxt('tables/early_life_attribute_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,5))
print(early_life_attribute_modifiers)
early_life_skill_modifiers = np.loadtxt('tables/early_life_skill_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,25))
print(early_life_skill_modifiers)

occupation_attribute_modifiers = np.loadtxt('tables/occupation_attribute_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,5))
print(occupation_attribute_modifiers)
occupation_skill_modifiers = np.loadtxt('tables/occupation_skill_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,25))
print(occupation_skill_modifiers)

reason_attribute_modifiers = np.loadtxt('tables/reason_attribute_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,5))
print(reason_attribute_modifiers)
reason_skill_modifiers = np.loadtxt('tables/reason_skill_modifiers.csv', skiprows=1, delimiter=',', usecols=range(1,25))
print(reason_skill_modifiers)