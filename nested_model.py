from pydantic import BaseModel
class address(BaseModel):
    house_no: str
    street: str
    city: str
    state: str
    pincode: str

class patient(BaseModel):
    name: str
    age: int
    email: str
    address: address

address_dict ={'city':'gurgaon','state':'haryana','pincode':'122002'}

address1 =Address(**address_dict)
patient1 =patient(name='John',age=30,email='john@gmail.com',address=address1)

patient_dict = {'name':'John','age':30,'email':'john@gmail.com','address':address1}
patient1 = patient(**patient_dict)
print(patient1)