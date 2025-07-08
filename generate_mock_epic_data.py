import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)

# Define number of appointments to generate
n = 200

# Set up a date range (simulate 2 weeks of appointments)
start_date = datetime(2025, 6, 17)
end_date = datetime(2025, 7, 1)
date_range = pd.date_range(start=start_date, end=end_date).to_list()

# Simulated values for fields
providers = ["Dr. Smith", "Dr. Johnson", "Dr. Lee", "Dr. Patel"]
departments = ["Cardiology", "Neurology", "Oncology", "Family Medicine"]
appt_types = ["Follow-up", "New Patient", "Procedure", "Routine Check"]

# Create data rows
data = []

for i in range(n):
    appt_date = random.choice(date_range)

    # Appointment scheduled time (8:00 AM to 3:45 PM)
    hour = random.randint(8, 15)
    minute = random.choice([0, 15, 30, 45])
    scheduled_time = datetime.combine(appt_date, datetime.min.time()) + timedelta(hours=hour, minutes=minute)

    # Determine if patient was a no-show
    no_show = random.choices([0, 1], weights=[0.85, 0.15])[0]  # 15% no-show rate

    if no_show == 0:
        wait_offset = random.randint(-10, 30)  # patient arrived early/late
        duration = random.randint(10, 60)  # appointment duration in minutes
        check_in_time = scheduled_time + timedelta(minutes=wait_offset)
        check_out_time = check_in_time + timedelta(minutes=duration)
    else:
        check_in_time = None
        check_out_time = None

    # Add row to dataset
    data.append({
        "patient_id": f"PT{i+1:04d}",
        "provider_name": random.choice(providers),
        "department": random.choice(departments),
        "appointment_date": appt_date.date(),
        "scheduled_time": scheduled_time.time(),
        "check_in_time": check_in_time.time() if check_in_time else None,
        "check_out_time": check_out_time.time() if check_out_time else None,
        "no_show": no_show,
        "appointment_type": random.choice(appt_types)
    })

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("mock_epic_appointment_data.csv", index=False)

print(" Dataset generated: mock_epic_appointment_data.csv")
