from flask_wtf import FlaskForm
from wtforms import TextAreaField, FloatField, IntegerField, StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, DataRequired, NumberRange, URL
from website.models import db, User, DoubanMovie

class RegisterForm(FlaskForm):
    username=StringField('用户名', validators=[DataRequired(),Length(3,24)])
    email=StringField('邮箱', validators=[DataRequired(),Email()])
    password=PasswordField('密码', validators=[DataRequired(), Length(6,24)])
    repeat_password=PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('提交')

    def create_user(self):
        user=User()
        user.username=self.username.data
        user.email=self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

class LoginForm(FlaskForm):
    email=StringField('邮箱',validators=[DataRequired(), Email()])
    password=PasswordField('密码', validators=[DataRequired(), Length(6,24)])
    remember_me =BooleanField('记住我')
    submit=SubmitField('提交')

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')

class MovieForm(FlaskForm):
    name=StringField('电影名称', validators=[DataRequired(), Length(0, 64)])
    url=StringField('网址', validators=[DataRequired(),URL()])
    year=IntegerField('年份', validators=[DataRequired(),NumberRange(min=1970,message='无效年份')])
    type=StringField('类型', validators=[DataRequired(), Length(0,64)])
    location=StringField('地区', validators=[DataRequired(), Length(0,64)])
    summary=TextAreaField('简介', validators=[DataRequired(), Length(0,2048)])
    score=FloatField('评分', validators=[DataRequired(), NumberRange(0,10)])
    submit=SubmitField('提交')

    def create_movie(self):
        movie=DoubanMovie()
        self.populate_obj(movie)
        db.session.add(movie)
        db.session.commit()
        return movie

    def update_movie(self, movie):
        self.populate_obj(movie)
        db.session.add(movie)
        db.session.commit()
        return movie
