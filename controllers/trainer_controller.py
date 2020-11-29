from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository
import repositories.exercise_class_repository as exercise_classimport 

trainers_blueprint = Blueprint("trainers", __name__)

@trainers_blueprint.route("/trainers")
def trainers():
    trainers = trainer_repository.select_all() # NEW
    return render_template("trainers/index.html", trainers = trainers)

@trainers_blueprint.route("/trainers/<id>")
def show(id):
    trainer = trainer_repository.select(id)
    return render_template("trainers/show.html", trainer=trainer)
