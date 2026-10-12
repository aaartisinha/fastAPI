from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)]
    email: EmailStr
    linkedin:AnyUrl
    age: Annotated[int, Field(gt=0)]
    weight: Annotated[float, Field(gt=0)]
    married: Annotated[bool, Field(default=False)]
    allergies: Optional[List[str]] = None
    contact_details: Optional[dict[EmailStr, str]] = None

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Invalid domain')
        return value

    @field_validator('name',mode='before')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age',mode='before')
    @classmethod
    def transform_age(cls, value):
        if 0< value < 18:
            return value 
        else:
            raise ValueError('Age must be greater than 18')

    @model_validator(mode='after')
    def validate_married(self):
        if self.married and self.age < 18:
            raise ValueError('Age must be greater than 18 if married')
        return self 

    @computed_field
    @property
    def display_name(self) -> str:
        return f"{self.name} ({self.age} years old)"

def insert_patient_data(patient: Patient):  
    """
    Insert patient data into database
    """
    print(patient.display_name)
    print('inserted into database')
  
patient_info = {"name": "John", "email": "john@gmail.com", "linkedin": "https://linkedin.com/in/john", "age": 30, "weight": 70.5, "married": True, "allergies": ["penicillin", "shellfish"], "contact_details": {"phone": "1234567890", "email": "john@gmail.com"}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)

def update_patient_data(patient: Patient):  

    print(patient.display_name)
    print('updated in database')
  
patient_info = {"name": "John", "email": "john@gmail.com", "linkedin": "https://linkedin.com/in/john", "age": 31, "weight": 71.5, "married": False, "allergies": ["penicillin", "shellfish"], "contact_details": {"phone": "1234567890", "email": "john@gmail.com"}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)


