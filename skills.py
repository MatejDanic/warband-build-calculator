import numpy as np
from attributes import attributes

skills = ['Ironflesh', 'Power Strike', 'Power Throw', 'Power Draw', 
          'Shield', 'Weapon Master', 'Riding', 'Horse Archery', 'Athletics', 'Looting', 
          'Trainer', 'Tracking', 'Spotting', 'Path-finding', 'Tactics', 'Wound Treatment', 'Surgery', 'First Aid', 'Engineer', 'Inventory Management', 
          'Leadership', 'Prisoner Management', 'Persuasion', 'Trade']

skill_base_attributes = np.loadtxt('tables/skill_base_attributes.csv', skiprows=1, delimiter=',', usecols=range(1,25))
#print(skill_base_attributes)

def get_skill_base_attribute_index(skill_index):
    skill_mask = [1 if i == skill_index else 0 for i in range(len(skills))]
    skill_mask[skill_index] = 1
    result = np.matmul(skill_base_attributes, skill_mask)
    index = np.where(result == 1)[0][0]
    return index


#for i, skill in enumerate(skills):
    #print(str(i) + '. ' + skill + ' -> ' + attributes[get_skill_base_attribute_index(i)])
