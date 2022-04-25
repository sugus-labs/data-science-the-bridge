from the_bridge import Teacher
from companies import Telco, Retail, Insurance
import hobbies
from datetime import date

def calculate_age(born_date):
    today = date.today()
    age = today.year - born_date.year
    return age 

class Person:
    def __init__(name, academic_role, born_date, 
        phone_number, email, experience, hobbies):
        self.name = name
        self.academic_role = academic_role
        self.birth_date = born_date
        self.phone_number = phone_number
        self.email = email
        self.experience = experience
        self.hobbies = hobbies
        age = calculate_age(born_date)

##### THE BELOW CODE IS THE IMPORTANT PART ##### 

academic_roles = {
    "LEAD_INSTRUCTOR": "Lead Instructor @ The Bridge",
    "TEACHER_ASSISTANT": "Teacher Assistant @ The Bridge",
    "STUDENT": "Student @ The Bridge",
}

teacher = Person(
    name = "Gustavo Martín Vela", 
    academic_role = academic_roles.LEAD_INSTRUCTOR, 
    born_date = date(1986, 11, 22), 
    phone_number = "633996124", 
    email = "gustavo.martin@thebridgeschool.es",
    experience = {
        Telco.TELEFONICA: ["Data Scientist", 72],
        Retail.IKEA: ["Data Scientist", 24],
        Insurance.INTERMUNDIAL: ["Data Engineering Manager", 12],
        Telco.MASMOVIL: ["Data Engineer Lead", 24],
        Retail.INDITEX: ["Cloud Data Solutions Lead", 4],
    }, 
    hobbies = [hobbies.mtb, hobbies.electronics, hobbies.iot, 
        hobbies.data_analysis, hobbies.travels],
)

##### THIS IS THE PART YOU HAVE TO FILL IT #####

#student = Person(
#    name = , 
#    academic_role = , 
#    born_date = , 
#    phone_number = , 
#    email = ,
#    experience = {}, 
#    hobbies = [],
#)


from datetime import date

ramp_up = {
    "start_date": date(2022, 4, 18),
    "end_date": date(2022, 5, 14),
    "description": """
        Learn the fundamentals of Python language programming. 
        Learn the basics of Git to manage code versions.
        Learn the basics of Markdown to comment the notebooks code.
        """,
    "subjects": ["Python", "Data Science toolkit", "Git", "Markdown"],
    "roles": ["Python Programmer"]
}
    
data_analysis = {
    "start_date": date(2022, 5, 18),
    "end_date": date(2022, 7, 16),
    "description": """
        Learn the Python libraries to analyze and visualize the data. 
        Learn the basics of data analysis and exploratory analysis.
        Learn about SQL and NoSQL databases. 
        """,
   "subjects": ["Data Analysis", "Data Exploration", 
       "Data Visualization", "SQL"],   
    "roles": ["Data Analyst", "Data Engineer"]
}

machine_learning = {
    "start_date": date(2022, 7, 18),
    "end_date": date(2022, 10, 15),
    "description": """
        Learn the basics of statistics. 
        Build your own models.
        Visualize the effectiveness of your models.
        """,
   "subjects": ["Supervised models", "Unsupervised models", 
       "Time series", "Deep learning"],   
    "roles": ["Data Engineer", "Machine Learning Engineer"]
}



data_science_and_business = {
    "start_date": date(2022, 10, 17),
    "end_date": date(2022, 12, 17),
    "description": """
        Learn how to deploy your models in production.
        Create and deploy Data Science projects end to end.
        Understand the business needs and create data solutions.
        """,
   "subjects": ["Storytelling", "Big Data", "API", "Cloud"],        
    "roles": ["Data Scientist", "Visualization Engineer", 
        "Business Analyst"]
}