# Student Performance Data Analysis

Exploratory data analysis of student academic performance using Python, Pandas, Matplotlib and Seaborn.

## Dataset
Use the Student Academic Performance dataset and save its CSV as `data/student_info.csv`.

The notebook this project is based on examines age, gender, mathematics/reading/writing scores, attendance, parent education, internet access, extra activities and final results.

## Run
```bash
pip install -r requirements.txt
python main.py
```

## Example output
```text
--- FIRST FIVE ROWS ---
[The first five records from student_info.csv are displayed]

--- MISSING VALUES ---
[Missing-value count for each column]

--- AVERAGE SCORES BY GENDER ---
[Mean mathematics, reading and writing scores for each gender]

Analysis completed. Charts are saved in the outputs/ folder.
```
Actual values depend on the CSV dataset you use.

## Output charts
- `outputs/age_distribution.png`
- `outputs/scores_by_gender.png`
- `outputs/results_by_parent_education.png`

## Repository structure
```text
student-performance-data-analysis/
├── data/
│   └── student_info.csv
├── outputs/
├── main.py
├── requirements.txt
└── README.md
```
