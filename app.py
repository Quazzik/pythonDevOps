from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# Инициализация Flask-приложения
app = Flask(__name__)

# Получение строки подключения из переменной окружения DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем отслеживание изменений

# Инициализация базы данных
db = SQLAlchemy(app)

# Модель для таблицы студентов
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    patronymic = db.Column(db.String(80), nullable=False)
    group = db.Column(db.String(20), nullable=False)
    course = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Student {self.surname} {self.name}>"


# Главная страница с формой
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        patronymic = request.form['patronymic']
        group = request.form['group']

        # Определение курса по первой цифре номера группы
        try:
            course = int(group.split('-')[1][0])
        except (IndexError, ValueError):
            course = "Не удалось определить курс"

        # Создание нового объекта Student и добавление в базу данных
        new_student = Student(surname=surname, name=name, patronymic=patronymic, group=group, course=course)
        db.session.add(new_student)
        db.session.commit()  # Сохраняем изменения в базе данных

        result = f"{surname} {name} {patronymic}, Группа: {group}, Курс: {course}"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6007, debug=True)
