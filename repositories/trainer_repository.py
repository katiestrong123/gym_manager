from db.run_sql import run_sql

from models.trainer import Trainer
        
# CREATE 
def save(trainer):
    sql = "INSERT INTO trainers (name, email, phone, specialism) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [trainer.name, trainer.email, trainer.phone, trainer.specialism]
    results = run_sql(sql, values)
    id = results[0]['id']
    trainer.id = id
  
#   READ -- SELECT ALL
def select_all():  
    trainers = [] 
    sql = "SELECT * FROM trainers"
    results = run_sql(sql)
    for result in results:
        trainer = Trainer(result['name'], result['email'], result['phone'], result['specialism'], result['id'] )
        trainers.append(trainer)
    return trainers 

#   READ -- SELECT ONE 
def select(id):
    sql = "SELECT * FROM Trainers WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    trainer = Trainer(result['name'], result['email'], result['phone'], result['specialism'], result['id'] )
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