# Neuralbits Technologies – Healthcare Database & Analytics Challenge  
**Complete Solution • 1,049,460 Records • 7 Advanced Analytical Queries**

*A high-performance synthetic healthcare database system built from scratch in Python & SQLite – submitted for Neuralbits Technologies Internship Assessment*

---

### Live Execution Proof
All screenshots from real execution included in `/screenshots`

---

## Features & Highlights
- **1,049,460 total realistic records** across 5 major Indian hospitals  
- 100,000 patients | 200,000 diagnoses | **649,455 treatment records** | 100,000 billing entries  
- Fully automated generation + instant analytical reporting  
- 7 production-grade SQL queries with business explanations  
- Optimized batch insertion (5k–10k rows/sec)  
- Clean, readable, and well-commented Python code  
- Zero external dependencies beyond standard library + pandas/numpy  

---

## Tech Stack
| Technology      | Purpose                                      |
|-----------------|----------------------------------------------|
| Python 3.9+     | Full backend logic & data generation         |
| SQLite3         | Lightweight, embedded, zero-config DB        |
| pandas + NumPy  | Realistic random data synthesis              |
| DB Browser (SQLite) | Visual validation & manual query testing |
| Windows CMD     | One-click execution                          |

---

## Project Structure
```
neuralbits-healthcare-challenge/
├── database_generation/
│   ├── output.txt                      # Full console log
│   └── create_database.py          # Generates entire 1M+ record DB (~3 mins)
├── analysis/
│   ├── results_summary.txt             # Clean formatted results
│   └── query_analysis.py           # Executes all 7 analytical queries with explanations
├── sql_queries/                    # Individual .sql files for reuse
│   ├── query_1_avg_patients.sql
│   ├── query_2_occupancy.sql
│   ├── query_3_age_category.sql
│   ├── query_4_top_medicines.sql
│   ├── query_5_medicines_diagnosis.sql
│   ├── query_6_avg_stay.sql
│   └── query_7_income_analysis.sql
├── healthcare.db                   # Final database (auto-generated)
├── screenshots/                    # Proof of execution
├── requirements.txt
└── README.md                       # This file
```

---

## How to Run (One-Command Experience)

```bash
# 1. Clone the repo
git clone https://github.com/omkarrr88/neuralbits-healthcare-challenge.git
cd neuralbits-healthcare-challenge

# 2. Install requirements (only pandas & numpy)
pip install pandas numpy

# 3. Generate the full database (~3–4 minutes)
python database_generation/create_database.py

# 4. Run complete analysis with beautiful output
python analysis/query_analysis.py
```

That’s it! You’ll see live progress bars and final insights printed directly in your terminal.

---

## Key Business Insights (From Actual Results)

| Insight                              | Value                              |
|--------------------------------------|------------------------------------|
| Most Prescribed Medicine             | **Metoprolol** – 26,338 times (4.06%) |
| Dominant Age Group                   | **Adult (20–60)** – 65.33%         |
| Average Length of Stay               | ~7.5 days across all hospitals     |
| Longest Patient Stays                | 8–14 days (50.13% of cases)        |
| 2024 Total Revenue                   | **₹839.87 Crore**                  |
| Cash vs Credit Ratio                 | ~20% Cash, ~80% Credit             |
| Top Diagnosis + Drug Pair            | Anemia → Sulfamethoxazole (26,866 prescriptions) |

---

## Made with Dedication by  
**Omkar Kadam**  
BE Final Year – IT Engineering  
Terna Engineering College, Nerul, Navi Mumbai  
University of Mumbai (2022–2026)

**Contact:**  
Email: omkarkadam181188@gmail.com  
LinkedIn: https://www.linkedin.com/in/omkarrrr/  
GitHub: https://github.com/omkarrr88

**Submission Date:** 02 December 2025  
**For:** Neuralbits Technologies Internship Evaluation

---

