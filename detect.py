# detect.py

import random

def detect_objects(image_path):
    # Simulate detection logic
    print(f"Processing image: {image_path}")
    
    # Simulated results
    helmet_detected = random.choice([True, False])
    license_plate_number = "AP31BZ" + str(random.randint(1000, 9999))

    return {
        "helmet": helmet_detected,
        "license_plate": license_plate_number
    }
