from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise_class import ExerciseClass
import repositories.trainer_repository as trainer_repository
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
    trainers = trainer_repository.select_all()
    return render_template("exercise_classes/new.html",  trainers=trainers)

# CREATE 
@exercise_classes_blueprint.route("/exercise_classes", methods=["POST"])
def create_exercise_class():
    name = request.form["name"]
    type = request.form["type"]
    duration = request.form["duration"]
    trainer_id = request.form["trainer_id"]
    trainer = trainer_repository.select(trainer_id)
    new_exercise_class = ExerciseClass(name, type, duration, trainer)
    exercise_class_repository.save(new_exercise_class)
    return redirect("/exercise_classes")

# DELETE 
@exercise_classes_blueprint.route("/exercise_classes/<id>/delete", methods=["POST"])
def delete_exercise_class(id):
    exercise_class_repository.delete(id)
    return redirect("/exercise_classes")

 # EDIT 
@exercise_classes_blueprint.route("/exercise_classes/<id>/edit", methods=["GET"])
def edit_exercise_classes(id):
    exercise_class = exercise_class_repository.select(id)
    return render_template("exercise_classes/edit.html", exercise_class=exercise_class)

# UPDATE
@exercise_classes_blueprint.route("/exercise_classes/<id>", methods=["POST"])
def update_exercise_class(id):
    name = request.form["name"]
    type = request.form["type"]
    duration = request.form["duration"]
    trainer_id = request.form["trainer_id"]
    trainer = trainer_repository.select(id)
    updated_class = ExerciseClass(name, type, duration, trainer, id)
    exercise_class_repository.update(updated_class)
    return redirect("/exercise_classes")