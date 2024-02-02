import os


def see_all_courses1():
    with open("course.txt", "r", encoding="utf-8") as file:
        print("--------------------------------------------------------------")
        for lines in file:
            list_1 = lines.split(";")
            print(list_1[0], ">>>>", list_1[1], ">>>>", list_1[2])
            print("--------------------------------------------------------------")

    menu_message(" ")
    menu()


def at_least_one_student2():
    with open("course.txt", "r", encoding="utf-8") as file:
        print("-------------------------------")
        for lines in file:
            list_2 = lines.split(";")

            if int(list_2[3]) > 0:
                print(">>>" + list_2[1])
                print("-------------------------------")
                continue

    menu_message(" ")
    menu()


def add_new_course3():
    global courses_codes

    while True:
        try:
            courses_codes = input("Course Code:\n(Please enter only digits!) ")

        except:
            print("You must use just digits!")
            continue

        if len(courses_codes) == 4:
            print("Course code is valid ✓")
            break
        else:
            print("Course code must contain 4 digits!!!")
            continue

    with open("course.txt", "r+", encoding="utf-8") as file_course:
        lines_list = file_course.readlines()

        if "CENG" + courses_codes not in str(lines_list):
            course_name = input("Enter course name: ")
            instructor_name = input("Enter instructor name:")
            file_course.write(
                "CENG" + courses_codes + ';' + course_name.title() + ';' + instructor_name.title() + ';' + "0" + '\n')

        else:
            print("The course with this course code already exists!!!")
            add_new_course3()

    menu_message(" ")
    menu()


def search_code4():
    with open("course.txt", "r", encoding="utf-8") as file:
        x = "CENG" + input("Search the course code: ")

        for lines in file:
            list_4 = lines.split(";")
            if x == list_4[0]:
                print("-------------------------------")
                print("~" + list_4[0], ">>>", list_4[1])
                print("-------------------------------")

    menu_message(" ")
    menu()


def search_name5():
    with open("course.txt", "r", encoding="utf-8") as file:
        x = input("Search the course name: ")

        print("-------------------------------")

        for lines in file:
            list_5 = lines.split(";")
            if x.capitalize() in list_5[1]:
                print(">>>" + list_5[1])
                print("-------------------------------")

    menu_message(" ")
    menu()


def register_student6():
    global student_id

    while True:
        try:
            student_id = input("Student ID: ")

        except:
            print("You must use just digits!")
            continue

        if len(student_id) == 6:
            print("Student ID is valid ✓")
            break
        else:
            print("Student ID must contain 6 digits!!!")
            continue

    course_code = input("Course Code:\n(Please enter only digits!) ")

    fh2_r = open("student.txt", "r", encoding="utf-8")
    fh2_w = open("temp2.txt", "w", encoding="utf-8")

    x = ' '

    while x:
        x = fh2_r.readline()
        y = x.split(";")

        if len(x) > 0:
            if student_id in y[0]:
                fh2_w.write(x.replace(y[2], "CENG" + course_code + "," + y[2]))

            else:
                fh2_w.write(x)

    fh2_w.close()
    fh2_r.close()
    os.remove("student.txt")
    os.rename("temp2.txt", "student.txt")

    fh_r = open("course.txt", "r", encoding="utf-8")
    fh_w = open("temp.txt", "w", encoding="utf-8")

    s = ' '

    while s:
        s = fh_r.readline()
        a = s.split(";")

        if len(s) > 0:
            if "CENG" + course_code == a[0]:

                my_str = str(int(a[3]) + 1)
                fh_w.write(a[0] + ";" + a[1] + ";" + a[2] + ";" + my_str + '\n')

            else:
                fh_w.write(s)

    fh_w.close()
    fh_r.close()
    os.remove("course.txt")
    os.rename("temp.txt", "course.txt")
    print("-------------------------------")
    print("Course added successfully!!!")
    print("-------------------------------")

    menu_message(" ")
    menu()


def students_courses7():
    with open("student.txt", "r", encoding="utf-8") as file:
        print("-----------------------------------")
        for students in file:
            list_7 = students.split(";")
            under_list = list_7[2].split(",")

            print(list_7[1] + ":")

            with open("course.txt", "r", encoding="utf-8") as f:
                for lines in f:
                    list_7_2 = lines.split(";")
                    if list_7_2[0] in str(under_list):
                        print("~~~" + list_7_2[1])
            print("-----------------------------------")
    menu_message(" ")
    menu()


def top_3courses8():
    course_names = []
    course_numbers = []

    with open("course.txt", "r", encoding="utf-8") as file:
        for line in file:
            list_8 = line.split(";")
            course_names.append(list_8[1])
            course_numbers.append(int(list_8[3]))

        top3 = []

        for i in range(3):
            value = max(course_numbers)
            index_value = course_numbers.index(value)
            top3.append(course_names[index_value])
            course_numbers[index_value] = 0

    record = 1
    print("------------------------------")
    for i in top3:
        print(record, "~~", i)
        print("------------------------------")
        record += 1

    menu_message(" ")
    menu()


def top_3_student9():
    with open("student.txt", "r", encoding="utf-8") as file:
        student_list = []
        lesson_number = []
        for linet in file:
            category = linet.split(";")
            lessons = category[2].split(",")
            student_list.append(category[1])
            lesson_number.append(len(lessons))

        top3 = []

        for i in range(3):
            value = max(lesson_number)
            index_value = lesson_number.index(value)
            top3.append(student_list[index_value])
            lesson_number[index_value] = 0

        print("------------------")
    for i in top3:
        print("~~" + i)
        print("------------------")

    menu_message(" ")
    menu()


def menu_message(message):
    while True:
        print()
        press = input("PRESS M TO RETURN TO THE MENU: ").lower() if message != None else input(
            "Press M for menu: ").lower()
        if press == 'm':
            menu()
            break


def menu():
    while True:
        os.system("cls")
        islem = input("____________________________________________________________________\n"
                      "|                 STUDENT REGISTRATION APP MENU                    |\n"
                      "| 1- See all the courses                                           |\n"
                      "| 2- List all the course that have at least one student registered |\n"
                      "| 3- Add a new course                                              |\n"
                      "| 4- Search a course by course code                                |\n"
                      "| 5- Search a course by name                                       |\n"
                      "| 6- Register a student to a course                                |\n"
                      "| 7- See all the students their registered courses                 |\n"
                      "| 8- See top 3 most crowded courses                                |\n"
                      "| 9- See top 3 students with the most course registrations         |\n"
                      "| e- Exit                                                          |\n"
                      "____________________________________________________________________\n"
                      "PLEASE CHOOSE AN OPTION:")

        if islem == "1":
            see_all_courses1()
        elif islem == "2":
            at_least_one_student2()
        elif islem == "3":
            add_new_course3()
        elif islem == "4":
            search_code4()
        elif islem == "5":
            search_name5()
        elif islem == "6":
            register_student6()
        elif islem == "7":
            students_courses7()
        elif islem == "8":
            top_3courses8()
        elif islem == "9":
            top_3_student9()
        elif islem == "e":
            break


menu()
