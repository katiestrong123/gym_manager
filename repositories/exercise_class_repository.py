from db.run_sql import run_sql

from models.exercise_class import ExerciseClass

# CREATE 
def save(exercise_class):
    sql = "INSERT INTO exercise_classes (name, type, duration) VALUES (%s, %s, %s) RETURNING *"
    values = [exercise_class.name, exercise_class.type, exercise_class.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise_class.id = id
    return exercise_class
  
#   READ -- SELECT ALL


#   READ -- SELECT ONE 


#   DELETE -- DELETE ALL


#   DELETE -- DELETE ONE


#   UPDATE 
