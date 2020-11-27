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
def select_all():  
    exercise_classes = [] 

    sql = "SELECT * FROM exercise_classes"
    results = run_sql(sql)

    for row in results:
        exercise_class = ExerciseClass(row['name'], row['type'], row['duration'], row['id'] )
        exercise_classes.append(exercise_class)
    return exercise_classes 

#   READ -- SELECT ONE 
def select_all():  
    exercise_classes = None 

    sql = "SELECT * FROM exercise_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        exercise_class = ExerciseClass(row['name'], row['type'], row['duration'], result['id'] )
        exercise_classes.append(exercise_class)
    return exercise_class






def select(id):
    trainer = None
    sql = "SELECT * FROM Trainers WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        trainer = Trainer(result['name'], result['email'], result['phone'], result['specialism'], result['id'] )
    return trainer





#   DELETE -- DELETE ALL


#   DELETE -- DELETE ONE


#   UPDATE 
