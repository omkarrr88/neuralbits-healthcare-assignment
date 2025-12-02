====================================================================================================
                         NEURALBITS HEALTHCARE ANALYSIS QUERIES
====================================================================================================

----------------------------------------------------------------------------------------------------
QUERY 1: Average Patients Per Month, Week, and Year
----------------------------------------------------------------------------------------------------

Explanation:
This shows the average number of patients admitted per month, week, and year
for each hospital. Used for capacity planning and resource allocation.

 hospital_id                             hospital_name  avg_patients_per_month  avg_patients_per_week  avg_patients_per_year
           1 KLES Dr Prabhakar Kore Hospital, Belagavi                  555.56                 125.79                6666.67
           2         Parul Sevashram Hospital, Gujarat                  555.56                 125.79                6666.67
           3  MGM Institute of Health Sciences, Mumbai                  555.56                 125.79                6666.67
           4         Sharda University Hospital, Delhi                  555.56                 125.79                6666.67
           5        DY Patil University Hospital, Pune                  555.56                 125.79                6666.67

----------------------------------------------------------------------------------------------------
QUERY 2: Hospital Occupancy Analysis
----------------------------------------------------------------------------------------------------

Explanation:
Occupancy rate measures bed utilization. Higher occupancy indicates
good resource usage, but too high means insufficient beds.

 hospital_id                             hospital_name  weekly_occupancy  monthly_occupancy  yearly_occupancy
           1 KLES Dr Prabhakar Kore Hospital, Belagavi            125.56             527.24           4955.87
           2         Parul Sevashram Hospital, Gujarat            125.45             526.78           4952.51
           3  MGM Institute of Health Sciences, Mumbai            125.67             527.70           4959.24
           4         Sharda University Hospital, Delhi            125.56             527.24           4955.87
           5        DY Patil University Hospital, Pune            125.56             527.24           4955.87

----------------------------------------------------------------------------------------------------
QUERY 3: Age-wise Patient Categorization
----------------------------------------------------------------------------------------------------

Explanation:
Groups patients by age for targeted healthcare services and
resource planning for different age groups.

 age_category  patient_count  percentage
Adult (20-60)          65326       65.33
 Senior (60+)          34674       34.67

----------------------------------------------------------------------------------------------------
QUERY 4: Top 10 Most Consumed Medicines
----------------------------------------------------------------------------------------------------

Explanation:
Identifies top medicines for inventory management and procurement planning.

   medicine_name  times_prescribed  percentage_of_all  unique_patients
      Metoprolol             26338               4.06            26338
       Ibuprofen             26307               4.05            26307
       Albuterol             26182               4.03            26182
      Lisinopril             26173               4.03            26173
     Amoxicillin             26167               4.03            26167
      Amlodipine             26101               4.02            26101
Sulfamethoxazole             26098               4.02            26098
        Cefixime             26090               4.02            26090
      Ranitidine             26010               4.00            26010
         Aspirin             25985               4.00            25985

----------------------------------------------------------------------------------------------------
QUERY 5: Top 3 Medicines Per Diagnosis Type
----------------------------------------------------------------------------------------------------

Explanation:
Shows standard treatment protocols for each diagnosis.
Useful for quality control and clinical best practices.

diagnosis_name    medicine_name  prescription_count  rank
        Anemia Sulfamethoxazole                2686     1
        Anemia          Aspirin                2668     2
        Anemia        Albuterol                2659     3
  Appendicitis       Ranitidine                2705     1
  Appendicitis       Omeprazole                2674     2
  Appendicitis      Clopidogrel                2667     3
     Arthritis       Metoprolol                2703     1
     Arthritis       Lisinopril                2696     2
     Arthritis    Ciprofloxacin                2653     3
        Asthma      Amoxicillin                2619     1
        Asthma    Ciprofloxacin                2617     2
        Asthma Sulfamethoxazole                2611     3
    Bronchitis        Albuterol                2707     1
    Bronchitis      Amoxicillin                2675     2
    Bronchitis       Cetirizine                2653     3
      COVID-19         Cefixime                2702     1
      COVID-19        Metformin                2697     2
      COVID-19     Azithromycin                2692     3
 Cholecystitis      Amoxicillin                2654     1
 Cholecystitis        Ibuprofen                2633     2
 Cholecystitis    Ciprofloxacin                2610     3
        Dengue      Fluticasone                2693     1
        Dengue       Amlodipine                2689     2
        Dengue       Metoprolol                2688     3
  Dyslipidemia       Cetirizine                2708     1
  Dyslipidemia       Lisinopril                2703     2
  Dyslipidemia       Ranitidine                2691     3
     Gastritis   Mefenamic Acid                2693     1
     Gastritis       Metoprolol                2685     2
     Gastritis         Cefixime                2669     3

... (Total 60 results, showing first 30)

----------------------------------------------------------------------------------------------------
QUERY 6: Average Length of Hospital Stay
----------------------------------------------------------------------------------------------------

Average Length of Stay by Hospital:
 hospital_id                             hospital_name  average_days  min_days  max_days  total_patients
           1 KLES Dr Prabhakar Kore Hospital, Belagavi          7.55         1        14           20000
           2         Parul Sevashram Hospital, Gujarat          7.52         1        14           20000
           3  MGM Institute of Health Sciences, Mumbai          7.46         1        14           20000
           4         Sharda University Hospital, Delhi          7.49         1        14           20000
           5        DY Patil University Hospital, Pune          7.53         1        14           20000

Distribution of Length of Stay:
los_category  patient_count  percentage
    1-3 Days          21242       21.24
    4-7 Days          28630       28.63
   8-14 Days          50128       50.13

Explanation:
Average LOS affects bed availability and costs. Lower LOS means better efficiency.

----------------------------------------------------------------------------------------------------
QUERY 7: Monthly and Yearly Income Analysis
----------------------------------------------------------------------------------------------------

Yearly Income Breakdown:
year  cash_income  credit_income  total_income  cash_percentage  transaction_count
2024 1.705908e+09   6.692843e+09  8.398751e+09            20.31              33236
2023 1.672504e+09   6.736770e+09  8.409274e+09            19.89              33202
2022 1.744601e+09   6.745060e+09  8.489661e+09            20.55              33562

Monthly Income Breakdown (Recent 12 months):
  month  cash_income  credit_income  total_income  cash_percentage
2024-12 144730283.73   568421487.08  713151770.81            20.29
2024-11 134876213.70   560035087.83  694911301.53            19.41
2024-10 146833411.41   560221991.05  707055402.46            20.77
2024-09 146691711.78   550943989.67  697635701.45            21.03
2024-08 153061118.11   566204572.73  719265690.84            21.28
2024-07 143788180.01   555744311.36  699532491.37            20.55
2024-06 124933345.75   552951836.26  677885182.01            18.43
2024-05 144751223.92   563185310.61  707936534.53            20.45
2024-04 135542588.26   548289755.07  683832343.33            19.82
2024-03 153682477.26   567649268.29  721331745.55            21.31
2024-02 132855160.04   522488393.85  655343553.89            20.27
2024-01 144162378.63   576706541.30  720868919.93            20.00

Explanation:
Financial analysis helps with cash flow planning and revenue forecasting.

====================================================================================================
ANALYSIS COMPLETE
====================================================================================================

All queries executed successfully!
Check the results above for insights from your healthcare database.