class student:
    def __init__(self, name, password, absence, id):
        self.name = name
        self.password = password
        self.absence = int (absence)
        self.id = id
    def daily_attendance(self, present):
        if present == 1:
            print("present!")
        elif present == 0:
            print("absence")
            self.absence += 1
    def show(self):
        print('Name: ', self.name)
        print('Password: ', self.password)
        print('absence: ', self.absence)
        print('Id: ', self.id)

aluno1 = student("joao", "joaoPassword", 0, "0001")

aluno1.show()

students = []
students.append(aluno1)

while True:
    found = False
    print()
    print('Press 0 for quit')
    print('Press 1 for admin')
    print('Press 2 for student')

    case = input('action: ')
    print()

    if case == '0':
        break

    elif case == '1':
        while True:
            print()
            print('Press 0 for quit')
            print('Press 1 for enroll students')
            print('Press 2 for daily attendance')

            case = input('action: ')
            print()

            if case == '0':
                break
            
            elif case == '1':
                new_name = input('Student name: ')
                new_password = input('Strudent password: ')
                new_id = str(len(students) + 1).zfill(4)

                new_student = student(new_name, new_password, 0, new_id)
                students.append(new_student)
            
            elif case == '2':
                attendance = 0
                while attendance < len(students):
                        print(f"{students[attendance].name} ")
                        check = input('Present? (y/n) ')
                        if check.lower() == 'n':
                            students[attendance].absence += 1
                        attendance += 1


    elif case == '2':
        print('Parent Portal')
        id = input('Please enter the student id: ')
        index = 0
        print()

        while index < len(students):
            if students[index].id == id:
                found = True
                print('Student found.')
                password = input('Please enter your password: ')
                
                if students[index].password == password:
                    students[index].show()
                    break
                else:
                    break
            index += 1
        if not found:
            print("Student not found.")
