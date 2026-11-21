import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_FILE = Path("data/student_info.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "Place student_info.csv inside the data/ folder. "
        "Expected columns include age, gender, math_score, reading_score, "
        "writing_score, attendance_rate, parent_education, internet_access, "
        "extra_activities and final_result."
    )

df = pd.read_csv(DATA_FILE)
print("\n--- FIRST FIVE ROWS ---")
print(df.head().to_string(index=False))
print("\n--- DATASET INFORMATION ---")
df.info()
print("\n--- SUMMARY STATISTICS ---")
print(df.describe(include="all").to_string())
print("\n--- MISSING VALUES ---")
print(df.isnull().sum().to_string())

if "age" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="age", bins=20, kde=True)
    plt.title("Distribution of Student Age")
    plt.xlabel("Age")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "age_distribution.png")
    plt.close()

score_columns = [c for c in ["math_score", "reading_score", "writing_score"] if c in df.columns]
if "gender" in df.columns and score_columns:
    gender_scores = df.groupby("gender")[score_columns].mean().round(2)
    print("\n--- AVERAGE SCORES BY GENDER ---")
    print(gender_scores.to_string())
    gender_scores.plot(kind="bar", figsize=(9, 5))
    plt.title("Average Scores by Gender")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "scores_by_gender.png")
    plt.close()

if "parent_education" in df.columns and "final_result" in df.columns:
    parent_result = pd.crosstab(df["parent_education"], df["final_result"], normalize="index").round(3)
    print("\n--- FINAL RESULT PROPORTION BY PARENT EDUCATION ---")
    print(parent_result.to_string())
    parent_result.plot(kind="bar", stacked=True, figsize=(10, 5))
    plt.title("Final Results by Parent Education")
    plt.ylabel("Proportion")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "results_by_parent_education.png")
    plt.close()

for col in ["internet_access", "extra_activities"]:
    if col in df.columns and "final_result" in df.columns:
        print(f"\n--- FINAL RESULT COUNTS BY {col.upper()} ---")
        print(pd.crosstab(df[col], df["final_result"]).to_string())

print("\nAnalysis completed. Charts are saved in the outputs/ folder.")
