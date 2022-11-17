from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length



class LoginForm(FlaskForm):
    password = StringField(label=('Enter Your Password:'),validators=[DataRequired(), Length(min=10)])
    submit = SubmitField(label=('Submit'))


app = Flask(__name__)
app.config['SECRET_KEY']='LongAndRandomSecretKey'



@app.route('/', methods=('GET', 'POST'))
def index():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.password.data)
        with open("top-1000.txt","r") as f:
            content = f.read()
            if form.password.data in content:
                print("known password")
            else:
                return render_template('display.html',value=form.password.data)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)