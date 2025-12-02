# Neuralbits Technologies - Healthcare Database Challenge

## 📋 Assignment Overview

This repository contains my complete solution to the Neuralbits Technologies 
Python Query Challenge for the Internship position.

### Submission Contents:

1. **Healthcare Database System**
2. **7 Analytical SQL Queries**
3. **Live Project Demonstrations**

---

## 🗂️ Directory Structure

### 1. Database Generation (`database_generation/`)

**File**: `create_database.py`

**What It Does**:
- Creates 5 hospital records
- Generates 100,000 patient records with realistic data
- Creates 2 diagnoses per patient (200,000 total)
- Assigns 5-8 medicines per patient (649,455 treatment records)
- Generates billing records with cash/credit payment modes

**Key Features**:
- Batch processing (5,000 records per batch) for efficiency
- Data validation and error handling
- Execution time: ~3-4 minutes
- Database size: ~50MB

**How to Run**:
```

cd database_generation

```

```

python create_database.py

```

## Technologies Used:

SQLite3

Python 3.8+

Pandas, NumPy

### 2. SQL Queries (queries/)
All 7 queries are documented separately with:

Query purpose and business value

SQL code

Expected output format

Key SQL concepts used


### 3. Analysis & Results (analysis/)
File: query_analysis.py

Executes all 7 queries sequentially with:

Result formatting as Pandas DataFrames

Summary statistics

Run All Queries:

```

python query_analysis.py

```


Installation:
```

pip install -r requirements.txt

```

Generate Database:
```

python database_generation/create_database.py

```

Run All Queries:
```

python analysis/query_analysis.py

```

## 📊 Results Summary
Database Statistics:
Total Records: 1,049,460

Hospitals: 5

Patients: 100,000

Diagnoses: 200,000

Treatments: 649,455

Billing Records: 100,000


## 📸 Execution Proof
Screenshots of database generation and query results included in
screenshots/ folder.

## 🙋 Questions or Clarifications?
Feel free to contact me at:

Email: omkarkadam181188@gmail.com

LinkedIn: https://www.linkedin.com/in/omkarrrr/

GitHub: https://github.com/omkarrr88

### 📄 License
This project is created for Neuralbits Technologies evaluation purposes.

Submitted: 02/12/2025 by Omkar Kadam