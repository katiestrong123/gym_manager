from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise_class import ExerciseClass
import repositories.exercise_class_repository as exercise_class_repository

exercise_classes_blueprint = Blueprint("exercise_classes", __name__)


@exercise_classes_blueprint.route("/exercise_classes")
def exercise_classes():
    exercise_classes = exercise_class_repository.select_all() # NEW
    return render_template("exercise_classes/index.html", exercise_classes = exercise_classes)

@exercise_classes_blueprint.route("/exercise_classes/<id>")
def show(id):
    exercise_class = exercise_class_repository.select(id)
    return render_template("exercise_classes/show.html", exercise_class=exercise_class)

# NEW
@exercise_classes_blueprint.route("/exercise_classes/new")
def new_class():
    return render_template("exercise_classes/new.html")