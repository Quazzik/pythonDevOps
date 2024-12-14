from flask import Flask, render_template, request

app = Flask(__name__)


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

        result = f"{surname} {name} {patronymic}, Группа: {group}, Курс: {course}"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6007, debug=True)
