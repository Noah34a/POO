from flask import Flask, request, jsonify
from Gestion import Student, Course, Enrollment
from data import students, courses

app = Flask(name)  # Créer le site flask pr l'api

@app.route('/students', methods=['POST'])
def create_student():
    """Fonction qui rajoute un nouvau élève"""

    data = request.get_json()  # Récup les info envoyé par l'utilisateur
    student = Student(data['name'], data['studentID'], data['age'])  # Créer un nouvau élève
    students[data['studentID']] = student  # Le met dans la liste des élèves
    return jsonify({"message": "Etudiant créé avec succès "}), 201  # Dit que ça a marché


@app.route('/courses', methods=['POST'])
def create_course():
    """Fonction qui rajoute un nouvau cours"""

    data = request.get_json()  # Récup les info sur le cours
    course = Course(data['courseName'], data['courseCode'], data['creditHours'])  # Créer un nouvau cours
    courses[data['courseCode']] = course  # Ajoute le cour a la liste
    return jsonify({"message": "Cour créé avec succès "}), 201  # Dit que c bon


@app.route('/enrollments', methods=['POST'])
def enroll_student():
    """Fonction qui met un élève dans un cours"""

    data = request.get_json()  # Récup les info
    student = students.get(data['studentID'])  # Cherche l'élève
    course = courses.get(data['courseCode'])  # Cherche le cours
    if student and course:  # Si l'es 2 existe
        course.enrollStudent(student)  # On met l'élève dan le cours
        return jsonify({"message": "Étudiant inscrit avec succès"}), 201  # C bon
    return jsonify({"error": "Etudiant ou cour introuvable"}), 404  # Si ya un pb


@app.route('/students/<studentID>', methods=['GET'])
def get_student(studentID):
    """Fonction qui récup les info d'un élève"""

    student = students.get(studentID)  # Cherche l'élève
    if student:
        return jsonify({
            "name": student.name,  # Donne son nom
            "age": student.age,  # Son age
            "average_grade": student.getAverageGrade()  # Sa moyenne
        })
    return jsonify({"error": "Étudiant introuvable"}), 404  # Si il existe pas


@app.route('/courses/<courseCode>', methods=['GET'])
def get_course(courseCode):
    """Fonction qui récup les info d'un cours"""

    course = courses.get(courseCode)  # Cherche le cours
    if course:
        return jsonify({
            "courseName": course.courseName,  # Nom du cours
            "enrolled_students": course.getEnrolledStudents()  # Liste des élèves qui son dedans
        })
    return jsonify({"error": "Cours introuvable"}), 404  


@app.route('/')
def home():
    """Page d'accueil"""
    return "Bienvenue sur mon API Flask 🚀"  # Message d'accueil


if name == 'main':  # Si on lance le fichier
    app.run(debug=True)  # Démarre l'api en mode debug pr voir les erreurs
