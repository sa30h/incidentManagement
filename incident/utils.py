# import random
# import datetime
# from .models import Incident 

# def check_incident_id_exists(incident_id):
#     return Incident.objects.filter(incident_id=incident_id).exists()

# def generate_unique_incident_id():
#     while True:
#         # Generate the Incident ID
#         prefix = "RMG"
#         random_number = random.randint(10000, 99999)
#         current_year = datetime.datetime.now().year
#         incident_id = f"{prefix}{random_number}{current_year}"
        
#         # Check if the Incident ID already exists
#         if not check_incident_id_exists(incident_id):
#             return incident_id
