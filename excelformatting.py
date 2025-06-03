import pandas as pd

# === 1. Load Excel ===
input_excel_path = "Data1.0.xlsx"  # Update path if needed
df = pd.read_excel(input_excel_path)

# === 2. Define columns ===
input_col = "Risk communication"

output_fields = [
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

# === 3. Format output fields ===
def format_output(row):
    lines = []
    for col in output_fields:
        val = row.get(col)
        if pd.notna(val):
            lines.append(f"{col}: {val}")
    return "\n".join(lines)

# === 4. Build new DataFrame ===
formatted_df = pd.DataFrame()
formatted_df["input"] = df[input_col]
formatted_df["output"] = df.apply(format_output, axis=1)

# Drop empty entries
formatted_df = formatted_df.dropna(subset=["input", "output"])

# === 5. Save to CSV ===
output_csv_path = "risk_data_formatted.csv"
formatted_df.to_csv(output_csv_path, index=False)
print(f"✅ CSV saved to: {output_csv_path}")
