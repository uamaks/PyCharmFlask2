from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return '<h1>Hello!</h1>'
    return render_template('template.html', name="Пользователи")


if __name__ == '__main__':
    app.run(debug=True)
