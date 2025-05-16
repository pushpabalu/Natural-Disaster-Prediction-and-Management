import random

# List of disasters and areas
disasters = ["Earthquake", "Flood", "Tsunami", "Hurricane", "Wildfire"]
areas = ["City A", "City B", "City C", "City D", "City E"]

# Management plans
plans = {
    "Earthquake": "Stay under sturdy furniture, evacuate if needed.",
    "Flood": "Move to higher ground, avoid water.",
    "Tsunami": "Evacuate coastal areas, go to high ground.",
    "Hurricane": "Stay indoors, keep emergency kit ready.",
    "Wildfire": "Evacuate early, avoid smoke, stay low."
}

# Predict disaster
def predict_disaster():
    disaster = random.choice(disasters)
    area = random.choice(areas)
    print("Predicted Disaster:", disaster)
    print("Location:", area)
    print("Management Plan:", plans[disaster])

# Run
predict_disaster()
