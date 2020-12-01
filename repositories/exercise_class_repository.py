from db.run_sql import run_sql

from models.exercise_class import ExerciseClass
import repositories.trainer_repository as trainer_repository

# CREATE 
def save(exercise_class):
    sql = "INSERT INTO exercise_classes (name, type, duration, trainer_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [exercise_class.name, exercise_class.type, exercise_class.duration, exercise_class.trainer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise_class.id = id
    return exercise_class
  
# #   READ -- SELECT ALL
def select_all():  
    exercise_classes = [] 
    sql = "SELECT * FROM exercise_classes"
    results = run_sql(sql)
    for result in results:
        trainer = trainer_repository.select(result["trainer_id"])
        exercise_class = ExerciseClass(result['name'], result['type'], result['duration'], trainer, result['id'] )
        exercise_classes.append(exercise_class)
        # print(vars(exercise_class))
    return exercise_classes 

# #   READ -- SELECT ONE 
def select(id):  
    sql = "SELECT * FROM exercise_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    trainer = trainer_repository.select(result["trainer_id"])
    exercise_class = ExerciseClass(result['name'], result['type'], result['duration'], trainer, result['id'] )
    return exercise_class

# #   DELETE -- DELETE ALL
def delete_all():
    sql = "DELETE FROM exercise_classes" 
    run_sql(sql)

# #   DELETE -- DELETE ONE
def delete(id):
    sql = "DELETE FROM exercise_classes WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

# #   UPDATE 
def update(exercise_class):
    sql = "UPDATE exercise_classes SET (name, type, duration, trainer_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [exercise_class.name, exercise_class.type, exercise_class.duration, exercise_class.trainer.id, exercise_class.id]
    run_sql(sql, values) 


    