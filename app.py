from flask import Flask, render_template

from controllers.exercise_classes_controller import exercise_classes_blueprint
from controllers.trainers_controller import trainers_blueprint

import datetime


app = Flask(__name__)

app.register_blueprint(exercise_classes_blueprint)
app.register_blueprint(trainers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

def new_year_countdown():
    new_years = datetime.date(2021, 1, 1) - datetime.date.today()
    new_years = str(new_years)
    days_remaining = new_years.strip("0:,") 
    days_remaining = days_remaining.replace(',', '')
    return days_remaining

app.jinja_env.globals.update(new_year_countdown=new_year_countdown)

if __name__ == '__main__':
    app.run()
