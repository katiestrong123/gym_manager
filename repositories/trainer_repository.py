from db.run_sql import run_sql

from models.trainer import Trainer
from models.exercise_class import ExerciseClass
        
# CREATE 
def save(trainer):
    sql = "INSERT INTO trainers (name, email, phone, specialism) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [trainer.name, trainer.email, trainer.phone, trainer.specialism]
    results = run_sql(sql, values)
    id = results[0]['id']
    trainer.id = id
    return trainer
  
#   READ -- SELECT ALL
def select_all():  
    trainers = [] 
    sql = "SELECT * FROM trainers"
    results = run_sql(sql)
    for sql_result in results:
        trainer = Trainer(sql_result['name'], sql_result['email'],sql_result['phone'], sql_result['specialism'], sql_result['id'] )
        trainers.append(trainer)
    return trainers 

#   READ -- SELECT ONE 
def select(id):
    sql = "SELECT * FROM Trainers WHERE id = %s"  
    values = [id] 
    sql_result = run_sql(sql, values)[0]
    trainer = Trainer(sql_result['name'], sql_result['email'],sql_result['phone'], sql_result['specialism'], sql_result['id'] )
    return trainer

#   DELETE -- DELETE ALL
def delete_all():
    sql = "DELETE FROM trainers" 
    run_sql(sql)

#   DELETE -- DELETE ONE
def delete(id):
    sql = "DELETE FROM trainers WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

#   UPDATE 
def update(trainer):
    sql = "UPDATE trainers SET (name, email, phone, specialism) = (%s, %s, %s, %s) WHERE id = %s"
    values = [trainer.name, trainer.email, trainer.phone, trainer.specialism, trainer.id]
    run_sql(sql, values) 

def get_classes(trainer):
    results = []
    sql = "SELECT * FROM exercise_classes WHERE trainer_id = %s"
    values = [trainer.id]
    sql_results = run_sql(sql, values)
    for sql_result in sql_results:
        exercise_class = ExerciseClass(sql_result['name'], sql_result['type'], sql_result['duration'], sql_result['schedule'], trainer, sql_result['id'] )
        results.append(exercise_class)
    return results