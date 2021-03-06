from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST", "GET"])
def login():

    if request.method=="POST":
        pass
        '''
        if user pressed Login:
        check user's info and login
        ''' 
    else:
        '''
        if user opened login page with get method
        '''
        return render_template("login.html")


@auth.route("/logout")
def logout():
    return "Logout "



@auth.route("/signup", methods = ["POST", "GET"])
def signup():
    
    if request.method=="POST":
        #get data
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        # check validation of data

        if len(email)<4:
            #invalid
            #flash("Email must be greater then 4 characters" , category="error")
            return render_template("signup.html", massage = "Email must be greater then 4 characters")        
        
        elif password1 != password2:
            #passwords are not the same
            #flash("Passwords didn't match." , category="error")
            return render_template("signup.html", massage = "Passwords didn't match.")
        
        elif len(password1)< 8 or len(password2)<8:
            #passwords are too short
            #flash("Passwords are too short." , category="error")
            return render_template("signup.html", massage = "Passwords are too short.")
        
        elif len(username) < 3:
            #username has no value
            #flash("Username must be greater than 3 characters." , category="error")
            return render_template("signup.html", massage = "Username must be greater than 3 characters.")
        
        
        else:
            #add user to database
            #flash("Account created.", category="success")
            return "success!"
    else:
        return render_template("signup.html")

