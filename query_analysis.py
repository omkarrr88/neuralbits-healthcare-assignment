#!/usr/bin/env python3
"""
Neuralbits Technologies - Query Analysis
Executes all 7 analytical queries on the healthcare database
"""

import sqlite3
import pandas as pd
import os

DB_FILE = 'healthcare.db'

if not os.path.exists(DB_FILE):
    print(f"ERROR: {DB_FILE} not found!")
    print("Run 'python create_database.py' first")
    exit(1)

conn = sqlite3.connect(DB_FILE)

print("\n" + "=" * 100)
print(" " * 25 + "NEURALBITS HEALTHCARE ANALYSIS QUERIES")
print("=" * 100)

# ============================================================
# QUERY 1
# ============================================================
print("\n" + "-" * 100)
print("QUERY 1: Average Patients Per Month, Week, and Year")
print("-" * 100)

query1 = """
SELECT 
    h.hospital_id,
    h.hospital_name,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT strftime('%Y-%m', p.admission_datetime)), 2) as avg_patients_per_month,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT strftime('%Y-W%W', p.admission_datetime)), 2) as avg_patients_per_week,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT strftime('%Y', p.admission_datetime)), 2) as avg_patients_per_year
FROM Hospital h
LEFT JOIN Patient p ON h.hospital_id = p.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY h.hospital_id;
"""

result1 = pd.read_sql_query(query1, conn)
print("\nExplanation:")
print("This shows the average number of patients admitted per month, week, and year")
print("for each hospital. Used for capacity planning and resource allocation.\n")
print(result1.to_string(index=False))

# ============================================================
# QUERY 2
# ============================================================
print("\n" + "-" * 100)
print("QUERY 2: Hospital Occupancy Analysis")
print("-" * 100)

query2 = """
SELECT 
    h.hospital_id,
    h.hospital_name,
    ROUND(COUNT(*) * 1.0 / 
          ((julianday(MAX(p.discharge_datetime)) - julianday(MIN(p.admission_datetime))) / 7 + 1), 2) 
    as weekly_occupancy,
    ROUND(COUNT(*) * 1.0 / 
          ((julianday(MAX(p.discharge_datetime)) - julianday(MIN(p.admission_datetime))) / 30 + 1), 2) 
    as monthly_occupancy,
    ROUND(COUNT(*) * 1.0 / 
          ((julianday(MAX(p.discharge_datetime)) - julianday(MIN(p.admission_datetime))) / 365 + 1), 2) 
    as yearly_occupancy
FROM Hospital h
LEFT JOIN Patient p ON h.hospital_id = p.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY h.hospital_id;
"""

result2 = pd.read_sql_query(query2, conn)
print("\nExplanation:")
print("Occupancy rate measures bed utilization. Higher occupancy indicates")
print("good resource usage, but too high means insufficient beds.\n")
print(result2.to_string(index=False))

# ============================================================
# QUERY 3
# ============================================================
print("\n" + "-" * 100)
print("QUERY 3: Age-wise Patient Categorization")
print("-" * 100)

query3 = """
SELECT 
    CASE 
        WHEN CAST((julianday('now') - julianday(p.dob)) / 365.25 AS INTEGER) < 13 THEN 'Child (0-12)'
        WHEN CAST((julianday('now') - julianday(p.dob)) / 365.25 AS INTEGER) BETWEEN 13 AND 19 THEN 'Adolescent (13-19)'
        WHEN CAST((julianday('now') - julianday(p.dob)) / 365.25 AS INTEGER) BETWEEN 20 AND 60 THEN 'Adult (20-60)'
        ELSE 'Senior (60+)'
    END as age_category,
    COUNT(*) as patient_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Patient), 2) as percentage
FROM Patient p
GROUP BY age_category
ORDER BY 
    CASE 
        WHEN age_category = 'Child (0-12)' THEN 1
        WHEN age_category = 'Adolescent (13-19)' THEN 2
        WHEN age_category = 'Adult (20-60)' THEN 3
        ELSE 4
    END;
"""

result3 = pd.read_sql_query(query3, conn)
print("\nExplanation:")
print("Groups patients by age for targeted healthcare services and")
print("resource planning for different age groups.\n")
print(result3.to_string(index=False))

# ============================================================
# QUERY 4
# ============================================================
print("\n" + "-" * 100)
print("QUERY 4: Top 10 Most Consumed Medicines")
print("-" * 100)

query4 = """
SELECT 
    t.medicine_name,
    COUNT(*) as times_prescribed,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Treatment), 2) as percentage_of_all,
    COUNT(DISTINCT t.patient_id) as unique_patients
FROM Treatment t
GROUP BY t.medicine_name
ORDER BY times_prescribed DESC
LIMIT 10;
"""

result4 = pd.read_sql_query(query4, conn)
print("\nExplanation:")
print("Identifies top medicines for inventory management and procurement planning.\n")
print(result4.to_string(index=False))

# ============================================================
# QUERY 5
# ============================================================
print("\n" + "-" * 100)
print("QUERY 5: Top 3 Medicines Per Diagnosis Type")
print("-" * 100)

query5 = """
WITH RankedMedicines AS (
    SELECT 
        d.diagnosis_name,
        t.medicine_name,
        COUNT(*) as prescription_count,
        ROW_NUMBER() OVER (PARTITION BY d.diagnosis_name ORDER BY COUNT(*) DESC) as rank
    FROM Treatment t
    INNER JOIN Patient p ON t.patient_id = p.patient_id
    INNER JOIN Diagnosis d ON p.patient_id = d.patient_id
    GROUP BY d.diagnosis_name, t.medicine_name
)
SELECT 
    diagnosis_name,
    medicine_name,
    prescription_count,
    rank
FROM RankedMedicines
WHERE rank <= 3
ORDER BY diagnosis_name, rank;
"""

result5 = pd.read_sql_query(query5, conn)
print("\nExplanation:")
print("Shows standard treatment protocols for each diagnosis.")
print("Useful for quality control and clinical best practices.\n")
print(result5.head(30).to_string(index=False))
print(f"\n... (Total {len(result5)} results, showing first 30)")

# ============================================================
# QUERY 6
# ============================================================
print("\n" + "-" * 100)
print("QUERY 6: Average Length of Hospital Stay")
print("-" * 100)

query6_avg = """
SELECT 
    h.hospital_id,
    h.hospital_name,
    ROUND(AVG(CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS REAL)), 2) 
        as average_days,
    CAST(MIN(julianday(p.discharge_datetime) - julianday(p.admission_datetime)) AS INTEGER) 
        as min_days,
    CAST(MAX(julianday(p.discharge_datetime) - julianday(p.admission_datetime)) AS INTEGER) 
        as max_days,
    COUNT(*) as total_patients
FROM Hospital h
LEFT JOIN Patient p ON h.hospital_id = p.hospital_id
GROUP BY h.hospital_id, h.hospital_name;
"""

result6_avg = pd.read_sql_query(query6_avg, conn)
print("\nAverage Length of Stay by Hospital:")
print(result6_avg.to_string(index=False))

query6_dist = """
SELECT 
    CASE 
        WHEN CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS INTEGER) <= 3 THEN '1-3 Days'
        WHEN CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS INTEGER) BETWEEN 4 AND 7 THEN '4-7 Days'
        WHEN CAST(julianday(p.discharge_datetime) - julianday(p.admission_datetime) AS INTEGER) BETWEEN 8 AND 14 THEN '8-14 Days'
        ELSE '15+ Days'
    END as los_category,
    COUNT(*) as patient_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Patient), 2) as percentage
FROM Patient p
GROUP BY los_category
ORDER BY 
    CASE 
        WHEN los_category = '1-3 Days' THEN 1
        WHEN los_category = '4-7 Days' THEN 2
        WHEN los_category = '8-14 Days' THEN 3
        ELSE 4
    END;
"""

result6_dist = pd.read_sql_query(query6_dist, conn)
print("\nDistribution of Length of Stay:")
print(result6_dist.to_string(index=False))

print("\nExplanation:")
print("Average LOS affects bed availability and costs. Lower LOS means better efficiency.")

# ============================================================
# QUERY 7
# ============================================================
print("\n" + "-" * 100)
print("QUERY 7: Monthly and Yearly Income Analysis")
print("-" * 100)

query7_yearly = """
SELECT 
    strftime('%Y', p.admission_datetime) as year,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END), 2) 
        as cash_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Credit' THEN b.bill_amount ELSE 0 END), 2) 
        as credit_income,
    ROUND(SUM(b.bill_amount), 2) as total_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END) * 100.0 / SUM(b.bill_amount), 2) 
        as cash_percentage,
    COUNT(*) as transaction_count
FROM Billing b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY strftime('%Y', p.admission_datetime)
ORDER BY year DESC;
"""

result7_yearly = pd.read_sql_query(query7_yearly, conn)
print("\nYearly Income Breakdown:")
print(result7_yearly.to_string(index=False))

query7_monthly = """
SELECT 
    strftime('%Y-%m', p.admission_datetime) as month,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END), 2) 
        as cash_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Credit' THEN b.bill_amount ELSE 0 END), 2) 
        as credit_income,
    ROUND(SUM(b.bill_amount), 2) as total_income,
    ROUND(SUM(CASE WHEN b.payment_mode = 'Cash' THEN b.bill_amount ELSE 0 END) * 100.0 / SUM(b.bill_amount), 2) 
        as cash_percentage
FROM Billing b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY strftime('%Y-%m', p.admission_datetime)
ORDER BY month DESC;
"""

result7_monthly = pd.read_sql_query(query7_monthly, conn)
print("\nMonthly Income Breakdown (Recent 12 months):")
print(result7_monthly.head(12).to_string(index=False))

print("\nExplanation:")
print("Financial analysis helps with cash flow planning and revenue forecasting.")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 100)
print("ANALYSIS COMPLETE")
print("=" * 100)
print("\nAll queries executed successfully!")
print("Check the results above for insights from your healthcare database.")

conn.close()
