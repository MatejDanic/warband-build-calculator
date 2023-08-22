import json
from attributes import attributes
from skills import skills, get_skill_base_attribute
from defaults import base_attribute_values, base_skill_values
from books import book_attribute_values, book_skill_values
from modifiers import *
from backgrounds import *

class Build:

    def __init__(self, dict=None):
        if dict:
            vars(self).update(dict)
        else:
            self.name = 'John Doe'
            self.gender = 0
            self.father = 0
            self.early_life = 0
            self.occupation = 0
            self.reason = 0
            self.level = 1
            self.given_attribute_values = [0 for i in range(len(attributes))]
            self.given_skill_values = [0 for i in range(len(skills))]
            
    def __str__(self):
        return json.dumps(self.__dict__)
    
    def set_attribute_values(self, attribute_values):
        diff = 0
        for i, attribute_value in enumerate(attribute_values):
            if attribute_value < self.get_starting_attribute_values()[i]:
                raise Exception ('Minimum attribute value reached.')
            diff += self.get_total_attribute_values()[i] - attribute_value
        if diff + self.get_free_attribute_points() < 0:
            raise Exception('Not enough attribute points.')   
        self.given_attribute_values = (attribute_values - self.get_starting_attribute_values()).astype(int).tolist()

    def get_total_attribute_values(self):
        return (self.get_starting_attribute_values() + self.given_attribute_values).astype(int)

    def get_starting_attribute_values(self):
        return (base_attribute_values + book_attribute_values + self.get_background_attribute_values()).astype(int)
    
    def get_background_attribute_values(self):
        return (self.get_gender_attribute_values() + self.get_father_attribute_values() + self.get_early_life_attribute_values() + self.get_occupation_attribute_values() + self.get_reason_attribute_values()).astype(int)
    
    def get_gender_attribute_values(self):
        gender_mask = [1 if i == self.gender else 0 for i in range(len(genders))]
        return np.matmul(gender_mask, gender_attribute_modifiers)
    
    def get_father_attribute_values(self):
        father_mask = [1 if i == self.father else 0 for i in range(len(fathers))]
        return np.matmul(father_mask, father_attribute_modifiers)
    
    def get_early_life_attribute_values(self):
        early_life_mask = [1 if i == self.early_life else 0 for i in range(len(early_lives))]
        return np.matmul(early_life_mask, early_life_attribute_modifiers)
    
    def get_occupation_attribute_values(self):
        occupation_mask = [1 if i == self.occupation else 0 for i in range(len(occupations))]
        return np.matmul(occupation_mask, occupation_attribute_modifiers)
    
    def get_reason_attribute_values(self):
        reason_mask = [1 if i == self.reason else 0 for i in range(len(reasons))]
        return np.matmul(reason_mask, reason_attribute_modifiers)
    
    def set_skill_values(self, skill_values):
        diff = 0
        for i, skill_value in enumerate(skill_values):
            if skill_value < self.get_starting_skill_values()[i]:
                raise Exception ('Minimum skill value reached.')
            base_attribute = get_skill_base_attribute(i)
            if skill_value > self.get_starting_skill_values()[i] and skill_value > self.get_total_attribute_values()[base_attribute] / 3:
                raise Exception('Skill limit exceeded.')
            diff += self.get_total_skill_values()[i] - skill_value
        if diff + self.get_free_skill_points() < 0:
            raise Exception('Not enough skill points.')   
        self.given_skill_values = (skill_values - self.get_starting_skill_values()).astype(int).tolist()

    def get_total_skill_values(self):
        return (self.get_starting_skill_values() + self.given_skill_values).astype(int)

    def get_starting_skill_values(self):
        return (base_skill_values + book_skill_values + self.get_background_skill_values()).astype(int)
    
    def get_background_skill_values(self):
        return (self.get_father_skill_values() + self.get_early_life_skill_values() + self.get_occupation_skill_values() + self.get_reason_skill_values()).astype(int)

    def get_father_skill_values(self):
        father_mask = [1 if i == self.father else 0 for i in range(len(fathers))]
        return np.matmul(father_mask, father_skill_modifiers)
    
    def get_early_life_skill_values(self):
        early_life_mask = [1 if i == self.early_life else 0 for i in range(len(early_lives))]
        return np.matmul(early_life_mask, early_life_skill_modifiers)
    
    def get_occupation_skill_values(self):
        occupation_mask = [1 if i == self.occupation else 0 for i in range(len(occupations))]
        return np.matmul(occupation_mask, occupation_skill_modifiers)
    
    def get_reason_skill_values(self):
        reason_mask = [1 if i == self.reason else 0 for i in range(len(reasons))]
        return np.matmul(reason_mask, reason_skill_modifiers)
    
    def get_free_attribute_points(self):
        return int(3 + self.level - np.sum(self.given_attribute_values))

    def get_free_skill_points(self):
        return int(self.level + self.get_total_attribute_values()[attributes.index('Intelligence')] - np.sum(self.given_skill_values)) - 1
