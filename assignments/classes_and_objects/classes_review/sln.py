class Course:

    def __init__(self, title, classroom, description, students=None):
        self.title = title
        self.classroom = classroom
        self.description = description
        if students is None:
            self.students = []
        else:
            self.students = students


    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        return 'Title: {} \nRoom: {} \nDesc: {} \nStudents: {}'.format(self.title, self.classroom, self.description, self.students)


cs = Course('HSCS 2019-2020', 'Computer Lab', 'High School Computer Science')
cs.add_student('Chris Tung')
print(cs)
        

    
