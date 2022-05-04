from diagnoses_data import normal_weight, overweight_obese, underweight

class User:
    
    def __init__(self, username = str(), age = int(), current_weight = int(), goal_weight = int(), height = int(), sex = str()): #constructor
        
        self.__username = username
        
        self.__age = age
        
        self.__current_weight = current_weight
        
        self.__goal_weight = goal_weight
        
        self.height = height
        
        self.sex = sex

        
    def set_username(self, username):
        self.__username = username
        
    def set_age(self, age):
        self.__age = age
    
    def set_current_weight(self, current_weight):
        self.__current_weight = current_weight

    def set_goal_weight(self, goal_weight):
        self.__goal_weight = goal_weight
        
    def set_height(self, height):
        self.height = height
        
    def set_sex(self, sex):
        self.sex = sex
    
    def get_username(self):
        return self.__username
    
    def get_age(self):
        return self.__age
    
    def get_current_weight(self):
        return self.__current_weight
        
    def get_goal_weight(self):
        return self.__goal_weight
    
    def get_height(self):
        return self.height
    
    def get_sex(self):
        return self.sex 
        
    def get_current_goal_difference(self): #calculate weight loss
        return (int(self.get_current_weight()) - int(self.get_goal_weight()))
        
    def get_body_mass_index(self):
        return (int(self.get_current_weight()) / int(self.get_height())**2) * 703

    def get_new_bmi(self): #calculate new bmi if goal weight is made by user
        __new_bmi = (float(self.get_goal_weight()) / float(self.get_height())**2) * 703
        return __new_bmi
    
    def weight_status_category(self, bmi):
        if bmi < 18.5:
            return str("Underweight")
            self.weight_status_category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            return str("Normal weight")
            self.weight_status_category = "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return str("Overweight")
            self.weight_status_category = "Overweight"
        else:
            return str("Obese")
            self.weight_status_category = "Obese"
   
    def diagnoses(self):
        bmi = self.get_body_mass_index()
        if self.weight_status_category(bmi) == "Overweight" or self.weight_status_category(bmi) == "Obese":
            if self.get_sex() == "male":
                overweight_obese.extend(['Specific risks for overweight and obese men:', 'erectile dysfunction', 'prostate cancer', 'benign prostatic hyperplasia', 'low testosterone', 'low/no sperm count', 'reduced sperm quality'])
                print(*overweight_obese, sep = "\n")
            else:
                overweight_obese.extend(['Specific risks for overweight and obese women:', 'pregnancy complications', 'breast cancer', 'endometrial cancer', 'irregular menstrual cycles', 'reduced quality of eggs', 'anovulation (no egg is relased by the ovaries)'])
                print(*overweight_obese, sep = "\n")
        elif self.weight_status_category(bmi) == "Normal weight":
            print(*normal_weight, sep = "\n")
        elif self.weight_status_category(bmi) == "Underweight":
            if self.get_sex() == "male":
                underweight.extend(['Specific risks for underweight men:', 'low sperm count', 'reduced sperm quality', 'low testosterone'])
                print(*underweight, sep = "\n")
            else:
                underweight.extend(['Specific risks for underweight women:', 'irregular periods', 'amenorrhea', 'premature births'])
                print(*underweight, sep = "\n")
    
        if int(self.get_age()) < 21 and (self.weight_status_category(bmi) == "Overweight" or self.weight_status_category(bmi) == "Obese"):
            print("Being overweight or obese can stunt growth")
        elif int(self.get_age()) < 21 and (self.weight_status_category(bmi) == "Underweight"):
            print("Being underweight can stunt growth")
        else:
            pass
        

    def __repr__(self):
        return "Basic Stats:(SW: %s, GW: %s, H: %s)" % (self.__current_weight, self.__goal_weight, self.height)
    
    