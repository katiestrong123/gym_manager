from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

trainers_blueprint = Blueprint("trainers", __name__)

@trainers_blueprint.route("/trainers")
def trainers():
    trainers = trainer_repository.select_all() # NEW
    return render_template("trainers/index.html", trainers = trainers)

@trainers_blueprint.route("/trainers/<id>")
def show(id):
    trainer = trainer_repository.select(id)
    classes = trainer_repository.get_classes(trainer)
    return render_template("trainers/show.html", trainer=trainer, classes=classes)

# NEW
@trainers_blueprint.route("/trainers/new")
def new_trainer():
    return render_template("trainers/new.html")

# CREATE 
@trainers_blueprint.route("/trainers", methods=["POST"])
def create_trainer():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    specialism = request.form["specialism"]
    new_trainer = Trainer(name, email, phone, specialism)
    trainer_repository.save(new_trainer)
    return redirect("/trainers")

# DELETE 
@trainers_blueprint.route("/trainers/<id>/delete", methods=["POST"])
def delete_trainer(id):
    trainer_repository.delete(id)
    return redirect("/trainers")

# EDIT 
@trainers_blueprint.route("/trainers/<id>/edit", methods=["GET"])
def edit_trainer(id):
    trainer = trainer_repository.select(id)
    return render_template("trainers/edit.html", trainer=trainer)

# UPDATE 
@trainers_blueprint.route("/trainers/<id>", methods=["POST"])
def update_trainer(id):
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    specialism = request.form["specialism"]
    updated_trainer = Trainer(name, email, phone, specialism, id)
    trainer_repository.update(updated_trainer)
    return redirect("/trainers")