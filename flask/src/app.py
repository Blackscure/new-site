from models.user import User


from flask import Flask, render_template, request,session

app = Flask(__name__) # '__main__'
app.secret_key = "blacks"


@app.route('/') # www.mysite.com/api/
def hello_method():
    return render_template('login.html')

@app.before_first_request
def hello_method():
     Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if user.login_valid(email, password):
        user.login(email)

    return render_template("profile.html"  )

if __name__ == '__main__': 
    app.run(port=4995) 