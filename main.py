from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/usersignup", methods=['POST'])
def user_signup():
    user_signup = request.form['index.html']

    if username not in UserName():
        # the user tried to enter a user name that was not valid
        error = "'{0}' is not a valid user name, please try again.".format(user_signup)
        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)
    elif password not in Password():
        # the user tried to enter a user name that was not valid
        error = "'{0}' is not a valid user name, please try again.".format(user_signup)
        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)
    elif verify != password:
        # the user tried to enter a user name that was not valid
        error = "'{0}' is not a valid user name, please try again.".format(user_signup)
        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)
    

    # if we didn't redirect by now, then all is well
    return render_template('welcome.html', user_signup=user_signup)



@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', usersignup=user_signup(), error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
