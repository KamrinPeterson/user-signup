from flask import Flask, request, redirect, render_template
import cgi
import string

app = Flask(__name__)

app.config['DEBUG'] = True # displays runtime errors in the browser, too

def ValidateUserName(username):
    if username == '':
        return 'Invalid username'
    elif len(username) < 3:
        return 'Username must be longer than 3 characters'
    elif len(username) > 20: 
        return 'Username must be less than of equal to 20 characters'
    elif not str.isalpha(username):
        return "This is not a valid username, please use only letters"

    return ''

def ValidatePassword(password):
    if password == '':
        return 'Invalid password'
    elif len(password) < 3:
        return 'Password must be longer than 3 characters'
    elif len(password) > 20: 
        return 'Password must be less than of equal to 20 characters'
    elif not str.isalpha(password):
        return "This is not a valid password, please use only letters"
    return ''

def ValidateVerify(password, verify):
    if verify == '' or password != verify:
        return 'Password and verify do not match'
    return ''

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')

@app.route("/", methods=['POST'])
def postback():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    usernameMessage = ValidateUserName(username)
    passwordMessage = ValidatePassword(password)
    verifyMessage = ValidateVerify(password, verify)
    
    if usernameMessage != '' or passwordMessage != '' or verifyMessage != '':
        return render_template('index.html',username=username, email=email, usernameMessage = usernameMessage, passwordMessage=passwordMessage, verifyMessage=verifyMessage)
    return redirect('/welcome')
    #return render_template('index.html')
#The user leaves any of the following fields empty: username, password, verify password.
#The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
#The user's password and password-confirmation do not match.
#The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.



    #if ValidateUserName(username):
        # the user tried to enter a user name that was not valid
    #    error = "'{0}' is not a valid user name, please try again.".format(user_signup)
        # redirect to homepage, and include error as a query parameter in the URL
    #    return redirect("/?error=" + error)
    #elif password not in Password():
        # the user tried to enter a user name that was not valid
    #    error = "'{0}' is not a valid user name, please try again.".format(user_signup)
        # redirect to homepage, and include error as a query parameter in the URL
    #    return redirect("/?error=" + error)
    #elif verify != password:
        # the user tried to enter a user name that was not valid
    #    error = "'{0}' is not a valid user name, please try again.".format(user_signup)
        # redirect to homepage, and include error as a query parameter in the URL
    #    return redirect("/?error=" + error)
    

    # if we didn't redirect by now, then all is well
    #return render_template('welcome.html', user_signup=user_signup)



#@app.route("/")
#def index():
#    encoded_error = request.args.get("error")
#    return render_template('index.html', usersignup=user_signup, error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
