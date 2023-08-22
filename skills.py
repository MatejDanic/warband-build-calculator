import numpy as np

skills = ['Ironflesh', 'Power Strike', 'Power Throw', 'Power Draw', 
          'Shield', 'Weapon Master', 'Riding', 'Horse Archery', 'Athletics', 'Looting', 
          'Trainer', 'Tracking', 'Spotting', 'Path-finding', 'Tactics', 'Wound Treatment', 'Surgery', 'First Aid', 'Engineer', 'Inventory Management', 
          'Leadership', 'Prisoner Management', 'Persuasion', 'Trade']

skill_base_attributes = np.loadtxt('tables/skill_base_attributes.csv', skiprows=1, delimiter=',', usecols=range(1,25))

def get_skill_base_attribute(skill):
    skill_mask = [1 if i == skill else 0 for i in range(len(skills))]
    skill_mask[skill] = 1
    result = np.matmul(skill_base_attributes, skill_mask)
    index = np.where(result == 1)[0][0]
    return index
