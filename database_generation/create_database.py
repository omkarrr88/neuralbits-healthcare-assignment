#!/usr/bin/env python3
"""
Neuralbits Technologies - Healthcare Database Generator
Generates 100,000+ patient records with diagnoses, treatments, and billing
"""

import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Configuration
print("=" * 80)
print("HEALTHCARE DATABASE GENERATOR - CONFIGURATION")
print("=" * 80)

np.random.seed(42)
random.seed(42)

NUM_PATIENTS = 100000
DB_FILE = 'healthcare.db'

# Remove old database if exists
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"Removed old {DB_FILE}")

# Connect to database
print(f"\nCreating database: {DB_FILE}")
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# ============================================================
# PART 1: CREATE TABLES
# ============================================================
print("\n" + "=" * 80)
print("PART 1: CREATING TABLES")
print("=" * 80)

cursor.execute('''
    CREATE TABLE Hospital (
        hospital_id INTEGER PRIMARY KEY,
        hospital_name TEXT NOT NULL
    )
''')
print("✓ Hospital table created")

cursor.execute('''
    CREATE TABLE Patient (
        patient_id INTEGER PRIMARY KEY,
        hospital_id INTEGER NOT NULL,
        patient_name TEXT NOT NULL,
        dob DATE NOT NULL,
        admission_datetime DATETIME NOT NULL,
        discharge_datetime DATETIME NOT NULL,
        FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
    )
''')
print("✓ Patient table created")

cursor.execute('''
    CREATE TABLE Diagnosis (
        diagnosis_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        diagnosis_name TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
    )
''')
print("✓ Diagnosis table created")

cursor.execute('''
    CREATE TABLE Treatment (
        treatment_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        medicine_name TEXT NOT NULL,
        dose_time TEXT NOT NULL,
        duration INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
    )
''')
print("✓ Treatment table created")

cursor.execute('''
    CREATE TABLE Billing (
        bill_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        bill_amount DECIMAL(10, 2) NOT NULL,
        payment_mode TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
    )
''')
print("✓ Billing table created")

conn.commit()

# ============================================================
# PART 2: INSERT DATA
# ============================================================
print("\n" + "=" * 80)
print("PART 2: INSERTING DATA")
print("=" * 80)

# 1. Insert hospitals
hospitals = [
    (1, 'KLES Dr Prabhakar Kore Hospital, Belagavi'),
    (2, 'Parul Sevashram Hospital, Gujarat'),
    (3, 'MGM Institute of Health Sciences, Mumbai'),
    (4, 'Sharda University Hospital, Delhi'),
    (5, 'DY Patil University Hospital, Pune')
]

cursor.executemany('INSERT INTO Hospital VALUES (?, ?)', hospitals)
conn.commit()
print(f"✓ {len(hospitals)} Hospitals inserted")

# 2. Generate patient data
print(f"\nGenerating {NUM_PATIENTS:,} patient records...")

first_names = ['Rajesh', 'Priya', 'Amit', 'Anjali', 'Arjun', 'Deepika', 'Vikram', 'Neha',
               'Rohan', 'Isha', 'Aditya', 'Pooja', 'Sanjay', 'Sneha', 'Varun', 'Ravi',
               'Sunita', 'Nitin', 'Kavya', 'Harish']

last_names = ['Sharma', 'Patel', 'Kumar', 'Singh', 'Gupta', 'Verma', 'Desai', 'Menon',
             'Iyer', 'Bhat', 'Nair', 'Kapoor', 'Malhotra', 'Khanna', 'Sinha', 'Reddy',
             'Joshi', 'Trivedi', 'Mishra', 'Pandey']

patient_data = []
start_date = datetime(2022, 1, 1)

for i in range(1, NUM_PATIENTS + 1):
    hospital_id = (i % 5) + 1
    patient_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    # DOB: between 1945 and 2020 (ages 2-77 years)
    dob = start_date - timedelta(days=random.randint(365*20, 365*77))
    
    # Admission: between 2022 and 2025
    admission_offset = random.randint(0, 365*3)
    admission_datetime = start_date + timedelta(days=admission_offset)
    
    # Discharge: 1-14 days after admission
    discharge_datetime = admission_datetime + timedelta(days=random.randint(1, 14))
    
    patient_data.append((i, hospital_id, patient_name, dob.date(), admission_datetime, discharge_datetime))

# Insert in batches (more efficient)
batch_size = 5000
for i in range(0, len(patient_data), batch_size):
    batch = patient_data[i:i+batch_size]
    cursor.executemany(
        'INSERT INTO Patient VALUES (?, ?, ?, ?, ?, ?)',
        batch
    )
    conn.commit()
    if (i // batch_size + 1) % 2 == 0:
        print(f"  → {i + len(batch):,} patients inserted...")

print(f"✓ Total {len(patient_data):,} patients inserted")

# 3. Generate diagnosis data (2 per patient)
print(f"\nGenerating diagnosis data (2 per patient)...")

diagnoses_list = ['Hypertension', 'Type 2 Diabetes', 'Pneumonia', 'Bronchitis', 'Gastritis',
                  'Urinary Tract Infection', 'Migraine', 'Asthma', 'Arthritis', 'Anemia',
                  'Viral Fever', 'Dengue', 'COVID-19', 'Whooping Cough', 'Malaria',
                  'Cholecystitis', 'Appendicitis', 'Pyelonephritis', 'Dyslipidemia', 'Obesity']

diagnosis_data = []
diagnosis_id = 1

for patient_id in range(1, NUM_PATIENTS + 1):
    for diagnosis_name in random.sample(diagnoses_list, 2):
        diagnosis_data.append((diagnosis_id, patient_id, diagnosis_name))
        diagnosis_id += 1

# Insert in batches
for i in range(0, len(diagnosis_data), batch_size):
    batch = diagnosis_data[i:i+batch_size]
    cursor.executemany(
        'INSERT INTO Diagnosis VALUES (?, ?, ?)',
        batch
    )
    conn.commit()
    if (i // batch_size + 1) % 4 == 0:
        print(f"  → {i + len(batch):,} diagnoses inserted...")

print(f"✓ Total {len(diagnosis_data):,} diagnoses inserted")

# 4. Generate treatment data (5-8 medicines per patient)
print(f"\nGenerating treatment data (5-8 medicines per patient)...")

medicines_list = ['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Metformin', 'Lisinopril',
                  'Atorvastatin', 'Aspirin', 'Clopidogrel', 'Metoprolol', 'Amlodipine',
                  'Omeprazole', 'Ranitidine', 'Azithromycin', 'Doxycycline', 'Ciprofloxacin',
                  'Cetirizine', 'Albuterol', 'Fluticasone', 'Levothyroxine', 'Vitamin D',
                  'Cefixime', 'Mefenamic Acid', 'Chloroquine', 'Sulfamethoxazole', 'Insulin']

dose_times = ['Morning', 'Afternoon', 'Evening', 'Night', 'Before Food', 'After Food',
              'Twice Daily', 'Thrice Daily']

treatment_data = []
treatment_id = 1

for patient_id in range(1, NUM_PATIENTS + 1):
    num_medicines = random.randint(5, 8)
    selected_medicines = random.sample(medicines_list, min(num_medicines, len(medicines_list)))
    
    for medicine_name in selected_medicines:
        dose_time = random.choice(dose_times)
        duration = random.randint(3, 30)
        treatment_data.append((treatment_id, patient_id, medicine_name, dose_time, duration))
        treatment_id += 1

# Insert in batches
for i in range(0, len(treatment_data), batch_size):
    batch = treatment_data[i:i+batch_size]
    cursor.executemany(
        'INSERT INTO Treatment VALUES (?, ?, ?, ?, ?)',
        batch
    )
    conn.commit()
    if (i // batch_size + 1) % 10 == 0:
        print(f"  → {i + len(batch):,} treatment records inserted...")

print(f"✓ Total {len(treatment_data):,} treatment records inserted")

# 5. Generate billing data
print(f"\nGenerating billing data...")

billing_data = []
payment_modes_list = ['Cash', 'Credit Card', 'Debit Card', 'Insurance', 'Online Transfer']
bill_id = 1

for patient_id in range(1, NUM_PATIENTS + 1):
    bill_amount = round(random.uniform(5000, 500000), 2)
    payment_mode = random.choice(payment_modes_list)
    
    # Convert to cash or credit for queries
    if payment_mode == 'Cash':
        payment_mode = 'Cash'
    else:
        payment_mode = 'Credit'
    
    billing_data.append((bill_id, patient_id, bill_amount, payment_mode))
    bill_id += 1

# Insert in batches
for i in range(0, len(billing_data), batch_size):
    batch = billing_data[i:i+batch_size]
    cursor.executemany(
        'INSERT INTO Billing VALUES (?, ?, ?, ?)',
        batch
    )
    conn.commit()
    if (i // batch_size + 1) % 2 == 0:
        print(f"  → {i + len(batch):,} billing records inserted...")

print(f"✓ Total {len(billing_data):,} billing records inserted")

# Final commit
conn.commit()

# ============================================================
# PART 3: SUMMARY
# ============================================================
print("\n" + "=" * 80)
print("DATABASE CREATION SUMMARY")
print("=" * 80)
print(f"\n✓ Database file: {DB_FILE}")
print(f"✓ Total records inserted: {5 + NUM_PATIENTS + len(diagnosis_data) + len(treatment_data) + len(billing_data):,}")
print(f"\nBreakdown:")
print(f"  - Hospitals:        {len(hospitals)}")
print(f"  - Patients:         {NUM_PATIENTS:,}")
print(f"  - Diagnoses:        {len(diagnosis_data):,} (2 per patient)")
print(f"  - Treatments:       {len(treatment_data):,} (5-8 per patient)")
print(f"  - Billing records:  {len(billing_data):,}")

# Create index for better query performance
print("\nCreating indexes for better performance...")
cursor.execute('CREATE INDEX idx_patient_hospital ON Patient(hospital_id)')
cursor.execute('CREATE INDEX idx_treatment_patient ON Treatment(patient_id)')
cursor.execute('CREATE INDEX idx_diagnosis_patient ON Diagnosis(patient_id)')
cursor.execute('CREATE INDEX idx_billing_patient ON Billing(patient_id)')
conn.commit()
print("✓ Indexes created")

print("\n" + "=" * 80)
print("✓ DATABASE READY FOR QUERIES")
print("=" * 80)
print(f"\nDatabase location: {os.path.abspath(DB_FILE)}")
print("Next: Run 'python query_analysis.py' to execute all queries")

conn.close()
