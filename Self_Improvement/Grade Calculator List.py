while True:
    grade_list = input("Please input a list of numerical grades (0-100) separated by spaces, or type 'cancel' to exit: ")
    
    #Check if the input contains the word 'cancel' (case-insensitive)
    if 'cancel' in grade_list.lower().strip():
        print("You canceled the input.")
        break
    
    #Check if the input is not empty
    if grade_list.strip():
        grades = grade_list.split()
        letter_grades = []

        for grade_str in grades:
            try:
                score = float(grade_str)
                if 0 <= score <= 100:
                    if score > 90:
                        letter_grades.append('A')
                    elif score > 80:
                        letter_grades.append('B')
                    elif score > 70:
                        letter_grades.append('C')
                    elif score > 60:
                        letter_grades.append('D')
                    elif score > 50:
                        letter_grades.append('E')
                    else:
                        letter_grades.append('F')
                else:
                    print(f"Invalid input: {grade_str} is not between 0 and 100. Skipping.")
            except ValueError:
                print(f"Invalid input: {grade_str} is not a valid number. Skipping.")

        if letter_grades:
            print("Letter Grades for the input list:")
            for i, letter_grade in enumerate(letter_grades):
                print(f"Grade {i + 1}: {letter_grade}")
        else:
            print("No valid grades were provided in the list.")
    else:
        print("You didn't enter anything.")
