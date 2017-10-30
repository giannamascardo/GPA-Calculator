'''
GPA Calculator
'''

'''
Grading Scale
'''


all_grades = {"A_PLUS": 4.0, "A": 4.0, "A_MINUS": 3.7, "B_PLUS": 3.3, "B": 3.0, "B_MINUS": 2.7,
              "C_PLUS": 2.3, "C": 2.0, "C_MINUS": 1.7, "D_PLUS": 1.3, "D": 1.0, "D_MINUS": 0.7, "F": 0}

class Calculator:
    def __init__(self, course_dict):
        '''Takes the inputted dictionary and credit and initializes the course dictionary'''
        self.course_dict = course_dict
        
    def get_course_info(self, course):
        '''Takes the inputted course and returns the two tuple associated with that course'''
        for course_in_dict in self.course_dict:
            if course == course_in_dict:
                return self.course_dict.get(course)

    def credit_per_class(self, course):
        '''Takes the inputted course and returns the GPA credit earned for that class'''
        course_grade = self.get_course_info(course)[0]
        course_credit = self.get_course_info(course)[1]
        
        for possible_grade in all_grades:
            if possible_grade == course_grade:
                return all_grades.get(course_grade) * course_credit

    def gpa_for_all(self):
        '''Calculates the gpa for all the courses in the given course dictionary'''
        total_units_earned = 0
        total_credit = 0
        for course_in_dict in self.course_dict:
            total_units_earned += self.credit_per_class(course_in_dict)
            total_credit += self.get_course_info(course_in_dict)[1]
            
        return total_units_earned / total_credit
            
