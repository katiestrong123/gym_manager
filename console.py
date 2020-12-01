import pdb
from models.trainer import Trainer
from models.exercise_class import ExerciseClass

import repositories.trainer_repository as trainer_repository
import repositories.exercise_class_repository as exercise_class_repository

exercise_class_repository.delete_all()
trainer_repository.delete_all()

trainer_1 = Trainer('Oli Saunders', 'oli@initializefitness.com', "+447758135514", 'Endurance Training')
trainer_repository.save(trainer_1)

trainer_2 = Trainer('Cassia Briscoe', 'cassia@initializefitness.com', "+447438132414", 'Weight loss')
trainer_repository.save(trainer_2)

trainer_3 = Trainer('Damien Young', 'damo@initializefitness.com', "+447438155514", 'Strength Training')
trainer_repository.save(trainer_3)

class_1 = ExerciseClass('Cycho Spin', 'Cardio', 60, "2nd December", trainer_1)
exercise_class_repository.save(class_1)

class_2 = ExerciseClass('Yoga', 'Flexibility and Core', 45, "4th December", trainer_2)
exercise_class_repository.save(class_2)

class_3 = ExerciseClass('Bodypump', 'Strength Training', 60, "4th December", trainer_2)
exercise_class_repository.save(class_2)

class_4 = ExerciseClass('Kickbox', 'Cardio', 60, "4th December", trainer_3)
exercise_class_repository.save(class_3)

class_5 = ExerciseClass('Soul Cycle', 'Cardio', 45, "6th December", trainer_1)
exercise_class_repository.save(class_1)

class_6 = ExerciseClass('Core init', 'Strength Training', 45, "7th December", trainer_2)
exercise_class_repository.save(class_2)

class_7 = ExerciseClass('Circuits', 'Cardio', 45, "7th December", trainer_3)
exercise_class_repository.save(class_3)

class_8 = ExerciseClass('Bodypump', 'Strength Training', 60, "4th December", trainer_2)
exercise_class_repository.save(class_2)

class_9 = ExerciseClass('Kickbox', 'Cardio', 60, "4th December", trainer_3)
exercise_class_repository.save(class_3)

class_10 = ExerciseClass('Pilates', 'Strength Training', 45, "8th December", trainer_1)
exercise_class_repository.save(class_1)

class_11 = ExerciseClass('Yoga', 'Flexibility and Core', 45, "9th December", trainer_2)
exercise_class_repository.save(class_2)

class_12 = ExerciseClass('Circuits', 'Cardio', 45, "10th December", trainer_3)
exercise_class_repository.save(class_3)

pdb.set_trace()
