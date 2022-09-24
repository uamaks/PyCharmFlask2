from app import app, db
from flask import render_template, flash, request, redirect, url_for
from app.forms import LoginForm, RegForm


@app.route('/')
@app.route('/index/')
@app.route('/main/')
def index():
    return render_template('main.html')


@app.route('/userlist')
def userlist():
    rows = db.select_user()
    return render_template('userlist.html', rows=rows)


@app.route('/userpage')
def userpage():
    alias, name, email = 'klava', 'Клавдия', 'klava92@meil.net'
    userdata = dict(alias=alias, name=name, email=email)
    return render_template('userpage.html', **userdata)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegForm()
    if form.validate_on_submit():
        if db.check_login(form):
            db.add_user(form)
            flash(f'Пользователь {form.login.data} успешно зарегистрирован')
            return redirect('/index')
        else:
            flash(f"Пользователь {form.login.data} уже зарегистрирован. \
            Если это Вы - воспользуйтесь формой авторизации. Если нет - используйте другой логин")

    return render_template('registration.html', title='Регистрация пользователя', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == '123':
            flash("Логин введен для пользователя {}".format(form.login.data))
            return redirect('/index')
        else:
            flash("Для пользователя {} введен неверный пароль...".format(form.login.data))
            return render_template('login.html', title='Авторизация пользователя', form=form, mss='alert-warning')
    return render_template('login.html', title='Авторизация пользователя', form=form)


@app.route('/base')
def base():
    # return render_template('base.html', title='Заголовок страницы')
    return render_template('base.html')


@app.route('/template')
def template():
    # return render_template('base.html', title='Заголовок страницы')
    return render_template('template.html', title='шаблон страницы')


@app.route('/basebs')
def basebs():
    # return render_template('base.html', title='Заголовок страницы')
    return render_template('basebs.html')
