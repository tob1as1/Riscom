import pandas as pd

# === 1. Load the Excel file ===
df = pd.read_excel("Data1.0.xlsx")

# === 2. Define the text and output fields ===
text_col = "Unnamed: 0"

output_fields = [
    'Risk communication',
    'Absolute risk (base case)', 'Absolute risk (new case)',
    'Absolute number (base case)', 'Absolute number (new case)',
    'Absolute risk difference', 'Relative risk difference',
    'Absolute number difference',
    'Verbal risk descriptor (base case)', 'Verbal risk descriptor (new situation)',
    'Verbal risk descriptor (change from base to new)',
    'Reference class size (base case: absolute number)',
    'Reference class size (new case: absolute number)',
    'Reference class description (base case)', 'Reference class description (new case)',
    'Source (base case)', 'Source (new situation)', 'Topic and unit'
]

# === 3. Format output string ===
def format_output(row):
    lines = []
    for col in output_fields:
        val = row.get(col)
        if pd.isna(val):
            lines.append(f"{col}: null")
        else:
            lines.append(f"{col}: {val}")
    return "\n".join(lines)

# === 4. Build training DataFrame ===
formatted_df = pd.DataFrame()
formatted_df["input"] = df[text_col]
formatted_df["output"] = df.apply(format_output, axis=1)

# Drop rows with missing input text
formatted_df = formatted_df.dropna(subset=["input"])

# === 5. Save to CSV ===
output_path = "risk_data_formatted.csv"
formatted_df.to_csv(output_path, index=False)
print(f"✅ Saved: {output_path} with 'input' and 'output' columns including nulls.")
