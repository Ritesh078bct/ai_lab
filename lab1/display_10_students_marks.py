def students_mark(student_number):
    student = 1
    marks = []
    while student<=student_number:
        print(f"enter the marks of student{student}")
        mark = int(input())
        marks.append(mark)
        student+=1

    print(marks)

    for index,value in enumerate(marks):
        print(f"student{index+1} got {value} marks")

student_number=int(input("enter student number"))
students_mark(student_number)
