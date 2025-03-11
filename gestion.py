class Student:
    """C la class qui représente un élève avec son nom, son ID et son âge"""
    
    def __init__(self, name, studentID, age):
        self.name = name  # Stock le nom de l'élève
        self.studentID = studentID  # Stock l'ID unique de l'élève
        self.age = age  # Stock l'age de l'élève
        self.grades = []  # Liste pour enregistrer les notes de l'éléve

    def add_grade(self, grade):
        """Rajoute une note a la liste des notes de l'élève"""
        self.grades.append(grade)

    def get_average_grade(self):
        """Fait la moyenne des notes, ou met 0 si ya pas de note"""
        return sum(self.grades) / len(self.grades) if self.grades else 0


class Course:
    """C la class ki représente un cour avec un nom, un code et des crédits"""

    def __init__(self, course_name, course_code, credit_hours):
        self.course_name = course_name  # Stock le nom du cour
        self.course_code = course_code  # Stock le code du cour
        self.credit_hours = credit_hours  # Stock le nb d'heure de credit
        self.students = []  # Liste des élèves qui sont inscrit dans le cour

    def enroll_student(self, student):
        """Ajoute un élève dans la liste des élèves inscrit au cour"""
        self.students.append(student)

    def get_enrolled_students(self):
        """Donne la liste des noms des élèves ki sont dan ce cour"""
        return [s.name for s in self.students]


class Enrollment:
    """Class ki gère kan un élève s'inscrit a un cour"""

    def __init__(self, student, course):
        self.student = student  # Stock l'élève qui s inscrit
        self.course = course  # Stock le cour ou il s inscrit

    def register(self):
        """Ajoute l'élève au cour en apellant la foncion enroll_student"""
        self.course.enroll_student(self.student)

