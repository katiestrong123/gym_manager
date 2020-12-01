from flask import Flask, render_template

from controllers.exercise_classes_controller import exercise_classes_blueprint
from controllers.trainers_controller import trainers_blueprint

app = Flask(__name__)

app.register_blueprint(exercise_classes_blueprint)
app.register_blueprint(trainers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()