from datetime import datetime
from flask import Flask, render_template, request, flash #request handles data sent by the client.
from flask_sqlalchemy import SQLAlchemy #SQLAlchemy is a Flask extension to interact with databases

#If you run the file directly, __name__ will be "__main__".
#If you import this file as a module into another script, __name__ will be the module’s name.
app = Flask(__name__) #Using __name__ helps Flask know where to find your HTML and other files, so your app can display web pages properly.
app.config["SECRET_KEY"] = "myapplication123" #Helps with security. Hackers will need this key to hack. It is kept private.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #Configures the app to use a SQLite database stored in a file called data.db.
db = SQLAlchemy(app) #Links the Flask app to the SQLAlchemy database

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(20))


#@app.route("/") is a decorator, it modifies the behavior of the function it wraps by associating that function with a specific URL route in a Flask web application.
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date = request.form['date']
        date_obj = datetime.strptime(date,"%Y-%m-%d")
        occupation = request.form['occupation']

        form = Form(first_name=first_name, last_name=last_name, email=email, occupation=occupation, date=date_obj) #date accepts date type so we need conversion
        db.session.add(form)
        db.session.commit()
        flash(f"{first_name}, your form was submitted successfully", "success")


    return render_template("index.html")

if __name__ == "__main__": #This means the script will only run the code inside this block if the script is being run directly (not imported as a module).
    #When you write with app.app_context(): before any operation, you're telling Flask:
    #"Hey Flask, get everything ready (like the app's configuration, database connections,
    # and other important parts), because I'm about to do something that needs them in the next lines of code."
    with app.app_context():
        db.create_all() #Sees if the database already exists if not creates the database
        app.run(debug=True, port=5001)
