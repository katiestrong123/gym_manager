from db.run_sql import run_sql

from models.trainer import Trainer


# class Trainer:
#     def __init__(self, name, email, phone, specialism, id=None):
#         self.name = name 
#         self.email = email
#         self.phone = phone
#         self.specialism = specialism
#         self.id = id

        
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

    for row in results:
        trainer = Trainer(row['name'], row['email'], row['phone'], row['specialism'], row['id'] )
        trainers.append(trainer)
    return trainers 

#   READ -- SELECT ONE 

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