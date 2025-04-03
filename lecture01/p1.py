class Student:
    student_id = ''
    name = ''
    age = ''
    def display_info(self):
        print('ID:',self.student_id,'번 / 이름:', self.name,'/ 나이:', self.age,'살')

class StudentManager:
    students = []
    def add_student(self, student):
        self.students.append(student)
    def display_all_students(self):
        for i in self.students:
            i.display_info()

a = Student()
b = Student()
c = Student()
stuM = StudentManager()


a.student_id = '1'
a.name = '김철수'
a.age = '20'


b.student_id = '2'
b.name = '이영희'
b.age = '21'


c.student_id = '3'
c.name = '박지민'
c.age = '19'

stuM.add_student(a)
stuM.add_student(b)
stuM.add_student(c)

print('현재 등록된 학생 목록:')
stuM.display_all_students()

d = Student()

d.student_id = '4'
d.name = '한지수'
d.age = '22'

stuM.add_student(d)

print()
print('학번 4번 학생 추가 후:')
stuM.display_all_students()
