from flask import Blueprint,render_template, redirect, flash, url_for
from website.models import DoubanMovie, User
from website.forms import LoginForm, RegisterForm
from flask_login import login_user,logout_user, login_required

index=Blueprint('index',__name__)

@index.route('/')
def front_index():
    return render_template('index.html')

@index.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录','success')
    return redirect(url_for('.front_index'))

@index.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.front_index'))
    return render_template('login.html',form=form)

@index.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录','success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)
