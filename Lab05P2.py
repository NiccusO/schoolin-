course_list = []
action = input("Enter 'A' to add a course\nEnter 'D' to drop a course\nEnter 'E' to exit\n Enter choice (A/D/E):")
action = action.upper()
while action == 'A':
    again = 'Y'
    while again == 'Y':
        course_name = input("Which course would you like to add?:")
        if course_name in course_list:
            print("You are already registered in this course.")
            again = input("Would you like to add another course? (Y/N):")
            again = again.upper()
        else:
            course_list.append(course_name)
            again = input("Would you like to add another course? (Y/N):")
            again = again.upper()
            while 'Y' != again != 'N':
                print("Error: enter only Y or N")
                again = input("Would you like to add another course? (Y/N):")
                again = again.upper()
    if again == 'N':
        print("Courses added to course list.")
        course_list.sort()
        print("Your course list:", course_list)
        break
action = input("Enter 'A' to add a course\nEnter 'D' to drop a course\nEnter 'E' to exit\n Enter choice (A/D/E):")
while action == 'D':
    again = 'Y'
    while again == 'Y':
        course_name = input("Which course would you like to drop?:")
        if course_name not in course_list:
            print("You are not registered for this course.")
            again = input("Would you like to drop another course? (Y/N):")
            again = again.upper()
        else:
            course_list.remove(course_name)
            again = input("Would you like to drop another course? (Y/N):")
            again = again.upper()
            while 'Y' != again != 'N':
                print("Error: enter only Y or N")
                again = input("Would you like to drop another course? (Y/N):")
                again = again.upper()
    if again == 'N':
        print("Courses dropped from course list.")
        course_list.sort()
        print("Your course list:", course_list)
        break
action = input("Enter 'A' to add a course\nEnter 'D' to drop a course\nEnter 'E' to exit\n Enter choice (A/D/E):")
