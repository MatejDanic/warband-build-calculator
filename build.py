from attributes import attributes
from skills import skills, skill_base_attributes, get_skill_base_attribute_index
from defaults import base_attribute_values, base_skill_values

class Build:

    def __init__(self, name, gender, father, early_life, occupation, reason):
        self.name = name
        self.gender = gender
        self.father = father
        self.early_life = early_life
        self.occupation = occupation
        self.reason = reason
        self.free_attribute_points = 0
        self.free_skill_points = 0
        self.given_attribute_values = [0, 0, 0, 0]
        self.given_skill_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get_starting_attribute_values(self):
        return base_attribute_values + self.get_background_attribute_modifiers()

    def get_total_attribute_values(self):
        return self.get_starting_attribute_values() + self.given_attribute_values
    
    def get_starting_skill_values(self):
        return base_skill_values + self.get_background_skill_modifiers() 
    
    def get_total_skill_values(self):
        return self.get_starting_skill_values + self.given_skill_values

    def increase_attribute_value(self, attribute):
        if self.free_attribute_points < 1:
            raise Exception('Not enough attribute points')
        self.given_attribute_values[attributes.index(attribute)] += 1
        self.free_attribute_points -= 1

    def decrease_attribute_value(self, attribute):
        attribute_index = attributes.index(attribute)
        current_attribute_value = self.get_total_attribute_values()[attribute_index]
        if current_attribute_value - 1 < self.get_starting_attribute_values()[attribute_index]:
            raise Exception('Minimum attribute value reached.')
        self.given_attribute_values[attribute_index] -= 1
        self.free_attribute_points += 1

    def set_attribute_value(self, attribute, value):     
        attribute_index = attributes.index(attribute)
        if value < self.get_total_attribute_values()[attribute_index]:
            raise Exception ('Minimum attribute value reached.')
        diff = self.get_total_attribute_values()[attribute_index] - value 
        if diff < 0:
            raise Exception('Not enough attribute points.')        
        self.given_attribute_values[attribute_index] = value
        self.free_attribute_points += diff

    def increase_skill_value(self, skill):
        if self.free_skill_points < 1:
            raise Exception('Not enough attribute points.')
        skill_index = skills.index(skill)
        base_attribute_index = get_skill_base_attribute_index(skill)
        current_skill_value = self.get_total_skill_values()[skill_index]
        if current_skill_value + 1 > self.get_total_attribute_values()[base_attribute_index] / 3:
            raise Exception('Skill limit exceeded.')
        self.given_skill_values[skills.index(skill)] += 1
        self.free_skill_points -= 1

    def decrease_skill_value(self, index):
        skill_index = skills.index(skill)
        current_skill_value = self.get_total_skill_values()[skill_index]
        if current_skill_value - 1 < self.get_starting_skill_values()[skill_index]:
            raise Exception('Minimum skill value reached.')
        self.given_skill_values[index] -= 1
        self.free_skill_points += 1

    def set_skill_value(self, skill, value):
        skill_index = skills.index(skill)
        if value < self.get_total_skill_values()[skill_index]:
            raise Exception ('Minimum skill value reached.')
        base_attribute_index = get_skill_base_attribute_index(skill)
        if value > self.get_total_attribute_values()[base_attribute_index] / 3:
            raise Exception('Skill limit exceeded.')
        diff = self.get_total_skill_values()[skill_index] - value 
        if diff < 0:
            raise Exception('Not enough skill points.')   
        self.given_skill_values[skill_index] = value
        self.free_skill_points += diff

    def __str__(self):
        details = ''
        details += f'Name        : {self.name}\n'
        details += f'Gender      : {self.gender}\n'
        details += f'Father      : {self.father}\n'
        details += f'Early Life  : {self.early_life}\n'
        details += f'Occupation  : {self.occupation}\n'
        details += f'Reason      : {self.reason}\n'
        return details

