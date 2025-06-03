# Select the input column and the fields to include in the output
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

# Create the "output" column by concatenating the non-null values with labels
def format_output(row):
    lines = []
    for col in output_fields:
        val = row[col]
        if pd.notna(val):
            lines.append(f"{col}: {val}")
    return "\n".join(lines)

# Build new DataFrame
formatted_df = pd.DataFrame()
formatted_df["input"] = df[input_col]
formatted_df["output"] = df.apply(format_output, axis=1)

# Drop rows with empty input or output
formatted_df = formatted_df.dropna(subset=["input", "output"])

# Save to CSV
output_path = "/mnt/data/risk_data_formatted.csv"
formatted_df.to_csv(output_path, index=False)

output_path