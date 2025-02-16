class student:
    def __init__(self, name, password, absence, id, classe, installment):
        self.name = name
        self.password = password
        self.absence = int (absence)
        self.id = id
        self.classe = classe
        self.installment = int (installment)
    def login(self, userpassword):
        if userpassword == self.password:
            return 1
        else:
            print("Incorrect password!")
            return 0
    def daily_attendance(self, present):
        if present == 1:
            print("present!")
        elif present == 0:
            print("absence")
            self.absence += 1
    def edit_password(self, new_password):
        self.password = new_password
        print('your new password is', self.password)
    def show(self):
        print()
        print('Name:', self.name)
        print('Password:', self.password)
        print('absence:', self.absence)
        print('Id:', self.id)
        print('Class:', self.classe)
        print('Remaining installments:', 12 - self.installment)

class tutor:
    def __init__(self, user, access):
        self.user = user
        self.access = access
    def login(self, useraccess):
        if useraccess == self.access:
            return 1
        else:
            print("Incorrect access!")
            return 0
        
class timetable:
    def __init__(self, classe, first, second, third, fourth, fifth):
        self.classe = classe
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
    def edit(self, time):
        if time == 'first':
            print()
            print(f'current: {self.first}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.first = new_matter
            elif case == '1':
                return 0
        elif time == 'second':
            print()
            print(f'current: {self.second}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.second = new_matter
            elif case == '1':
                return 0
        elif time == 'third':
            print()
            print(f'current: {self.third}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.third = new_matter
            elif case == '1':
                return 0
        elif time == 'fourth':
            print()
            print(f'current: {self.fourth}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.fourth = new_matter
            elif case == '1':
                return 0
        elif time == 'fifth':
            print()
            print(f'current: {self.fifth}')
            print('Press 0 for edit')
            print('Press 1 for keep')
            case = input('action: ')
            
            if case == '0':
                print()
                new_matter = input('New matter: ')
                self.fifth = new_matter
            elif case == '1':
                return 0
    def show(self):
        print()
        print(f'class: {self.classe}')
        print(f'First: {self.first}')
        print(f'Second: {self.second}')
        print(f'Third: {self.third}')
        print(f'Fourth: {self.fourth}')
        print(f'Fifth: {self.fifth}')

class examination: 
    def __init__(self, classe, matter, date):
        self.classe = classe
        self.matter = matter
        self.date = date

gradebook = [
    {'matricula': '0001', 'math': {'ab1': 8, 'ab2': 0}, 'science': {'ab1': 2, 'ab2': 0}},
]

badu = tutor('badu', 'admin_badu')
aluno1 = student('joao', 'joaoPassword', 0, '0001', '1A', 3)
timetable1 = timetable('1A', 'vague', 'vague', 'vague', 'vague', 'vague')
exam = examination('1A','math', '27/02/2025')

timetables = []
timetables.append(timetable1)
tutors = []
tutors.append(badu)
students = []
students.append(aluno1)
exams = []
exams.append(exam)

while True:
    found = False
    print()
    print('Press 0 for quit')
    print('Press 1 for tutor')
    print('Press 2 for student')

    case = input('action: ')
    print()

    if case == '0':
        break

    elif case == '1':
        print()
        print('tutor Portal')
        user = input('Please enter the tutor user: ')
        index = 0
        print()

        while index < len(tutors):
            if tutors[index].user == user:
                found = True
                print(f'Hello {tutors[index].user}.')
                print()
                access = input('Please enter your acces: ')
                
                while tutors[index].login(access) == 1:
                    print()
                    print('Press 0 for quit')
                    print('Press 1 for enroll students')
                    print('Press 2 for daily attendance')
                    print('Press 3 for create a class')
                    print('Press 4 for timetable manage')
                    print('Press 5 for add exam')
                    print('Press 6 for edit gradebook')

                    case = input('action: ')
                    print()

                    if case == '0':
                        break
                    
                    elif case == '1':
                        new_name = input('Student name: ')
                        new_classe = input('Class: ')
                        new_installments = input('installments paid: ')
                        new_id = str(len(students) + 1).zfill(4)
                        new_password = new_id

                        new_installments = int(new_installments)
                        new_student = student(new_name, new_password, 0, new_id, new_classe, 12 - new_installments)
                        students.append(new_student)
                        new_student.show()

                        new_grade = {'matricula': new_id, 'math': {'ab1': 0, 'ab2': 0}, 'science': {'ab1': 0, 'ab2': 0}}
                        gradebook.append(new_grade)
                    
                    elif case == '2':
                        attendance = 0
                        while attendance < len(students):
                                print(f"{students[attendance].name} ")
                                check = input('Present? (y/n) ')
                                if check.lower() == 'n':
                                    students[attendance].absence += 1
                                attendance += 1
                    
                    elif case == '3':
                        new_classe = input('New class: ')
                        new_timetables = timetable(new_classe, 'vague', 'vague', 'vague', 'vague', 'vague')
                        new_timetables.show()
                        timetables.append(new_timetables)

                    elif case == '4':
                        classe = input('clas: ')
                        index = 0
                        
                        while index < len(timetables):
                            if timetables[index].classe == classe:
                                found = True

                                while True:
                                    print('-First')
                                    print('-Second')
                                    print('-Third')
                                    print('-Fourth')
                                    print('-Fifth')
                                    print()
                                    time = input('Enter the time(Or 0 for quit)')
                                    
                                    if time == '0':
                                        timetables[index].show
                                        break
                                    else:
                                        timetables[index].edit(time.lower())
                                break
                            index += 1
                        if not found:
                            print("Class not found.")

                    elif case == '5':
                        classe = input('Clas: ')
                        matter = input('Matter: ')
                        date = input('Date: ')
                        new_exam = examination(classe, matter, date)

                    elif case == '6':
                        matricula = input('id aluno: ')
                        subject = input('subject: ')
                        assessment = input('assessment (ex: ab1, ab2): ')
                        new_grade = input('new grade: ')

                        for aluno in gradebook:
                            if aluno['matricula'] == matricula:  
                                if subject in aluno:  
                                    if assessment in aluno[subject]:  
                                        aluno[subject][assessment] = new_grade 
                                        print(f"Changed {assessment.upper()} grade in {subject.capitalize()} to {new_grade}.")
                                    else:
                                        print(f"assessment '{assessment}' not found.")
                                else:
                                    print(f"subject '{subject}' not found.")
                                break 
                        else:
                            print("Matrícula não encontrada.")

            index += 1
        if not found:
            print('Student not found.')


    elif case == '2':
        print()
        print('Parent Portal')
        id = input('Please enter the student id: ')
        index = 0
        print()

        while index < len(students):
            if students[index].id == id:
                found = True
                print('Student found.')
                print()
                userpassword = input('Please enter your password: ')
                
                while students[index].login(userpassword) == 1:
                    print()
                    print('Press 0 for quit')
                    print('Press 1 for see informations')
                    print('Press 2 for see gradebook')
                    print('Press 3 for edit password')

                    case = input('action: ')
                    
                    if case == '0':
                        break

                    if case == '1':
                        students[index].show()
                    
                    if case == '2':
                        for x in gradebook:
                            if x['matricula'] == students[index].id:
                                print(f"\nGrades for {students[index].name}:")
                                for subject, grades in x.items():
                                    if subject != 'matricula':  
                                        print(f"  {subject.capitalize()}:")
                                        for evaluation, grade in grades.items():
                                            print(f"    {evaluation.upper()}: {grade}")
                                print("-" * 30)
                    
                    if case == '3':
                        userpassword = input('new password: ')
                        students[index].edit_password(userpassword)
                break
            index += 1
        if not found:
            print("Student not found.")
