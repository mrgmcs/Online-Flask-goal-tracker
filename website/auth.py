from flask import Blueprint, render_template, request

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
    
    if request.method="POST":
        pass
        '''
        chek username and email and passwords , if they chould be valid, make 
        account
        '''
    else:
        return render_template("signup.html")

