#tp5 "Structure data types and functions as objects"
def convert_grades_in_place(s):
    """Funciton that converst number grade into percentage grade"""
    for i in range(len(s)):
        name, grade = s[i]
        percentage = grade / 20 * 100
        s[i] = (name, percentage)
    return s

#should return [('student1', 50.0), ('student2', 45.0), ('student3', 90.0)]
print(convert_grades_in_place([('student1', 10.0), ('student2', 9.0), ('student3', 18.0)]))

def convert_grades_new(s):
    """Does the same thing as before but without modifiying the parameter s"""
    return [(name, grade / 20 * 100) for name, grade in s]

#should return [('student1', 50.0), ('student2', 45.0), ('student3', 90.0)]
print(convert_grades_new([('student1', 10.0), ('student2', 9.0), ('student3', 18.0)]))

def grade(grades):
    """Function that retruns true if average of grades is equal to or bigger than 10"""
    #check if student has any grades
    if not grades:
        return False
    
    #calculate average
    average = sum(grades) / len(grades)

    #return true if average bigger than or equal to 10
    return average >= 10

print(grade([5.0, 15.0])) #should return True
print(grade([])) #should return False

def filter_students_by_grade(d, grading_function):
    """Function that deletes students with insufficient grades from the list"""
    #check for each student in list
    for student in list(d):
        #assigne grade for each student
        grades = d[student]

        #apply grading_function 
        sufficient_grade = grading_function(grades)

        #if grade not sufficient delete student from list
        if not sufficient_grade:
            del d[student]
    return d

#should return {'student2': [12.0, 17.5]}
print(filter_students_by_grade({'student1': [5.0, 10.0], 'student2': [12.0, 17.5]}, grade))
#should return {'student2': [20.0]}
print(filter_students_by_grade({'student1': [], 'student2': [20.0]}, grade))