from models.base_model import BaseModel
from models import storage

the_objects = storage.all()
print("-- Reloaded objects --")
for o_id in the_objects.keys():
    obj = the_objects[o_id]
    amr = obj
    print(amr)

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print("-- Create a new object --")
print(my_model)
