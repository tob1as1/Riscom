from deserializer3 import get_risk_instance
from pydantic_model3 import Risk

# Ausgeschlossene Funktionalitäten bis dato:
# Umformulierung in gute Risikokommunikation via Textgenerierung 
# Reduktion von positive/ negative framing, e.g. 90% survival chance vs. 10% death risk 
# Reduktion von Framing durch Inhalte, e.g. mehr über Nutzen als über Schaden berichtet 

# Nicht abgedeckte Tabellen-Fälle: 
# Mehr als zwei Cases

# Grafische Implementierung? -> siehe Harding Center Infobox

# mögliche Implementierung: Ausgabe die in Plugin erscheinen soll vollständig in python erstellen und score übergeben für visuelle Anpassung in Plugin, z.B score=0-> Achtung(roter Rahmen)

class RiskProcessor: #@Maurice, @Rashid: Die Implentierung der Klasse ist für euch erstmal egal 
    # Konstruktor
    def __init__(self, risk_instance: Risk):
        self.risk = risk_instance
        self.extract_variables()

    def extract_variables(self):
        # Grundklassifizierung
        self.risk_com = self.risk.risk_com
        self.one_case = self.risk.one_case

        # Absolute risks
        self.abs_risk_base = self.risk.absolute_risk_base
        self.abs_risk_new = self.risk.absolute_risk_new

        # Absolute numbers
        self.abs_number_base = self.risk.absolute_number_base
        self.abs_number_new = self.risk.absolute_number_new

        # Differences
        self.abs_risk_diff = self.risk.absolute_risk_difference
        self.abs_number_diff = self.risk.absolute_number_difference

        # Relative risk
        self.rel_risk = self.risk.relative_risk

        # Verbal risk descriptors
        self.verbal_desc_base = self.risk.verbal_risk_descriptor_base
        self.verbal_desc_new = self.risk.verbal_risk_descriptor_new
        self.verbal_desc_change = self.risk.verbal_risk_descriptor_change

        # Reference class size
        self.ref_class_size_base = self.risk.reference_class_size_base
        self.ref_class_size_new = self.risk.reference_class_size_new

        # Reference class description
        self.ref_class_desc_base = self.risk.reference_class_description_base
        self.ref_class_desc_new = self.risk.reference_class_description_new

        # Sources
        self.source_base = self.risk.source_base
        self.source_new = self.risk.source_new

        # Topic and unit
        self.topic_unit = self.risk.topic_and_unit




# @Maurice @Rashid Das ist die grundlegende Bewertungslogik mit den Print befehlen 
    def process(self):
        output= []
        output.append("\n--- Risk analysis started ---")
        # 1. Grundlegende Klassifizierung
        # 1.1 (-> Ausgabe). Riskokommunikation gegeben: nein -> break & Ausgabe 
        if self.risk_com == 0:
            output.append("1.1: No risk communication provided. Analysis terminated.")
            return "\n".join(output)
        output.append("1.1: Risk communication detected.")

        # 1.2 (-> keine Ausgabe). Unterscheidung zwischen one case und two case -> bereits in Binärvariablen gespeichert
        if self.one_case == 1:
             output.append("1.2: Single case detected.")
        else:
             output.append("1.2: Two cases detected: comparing two risk scenarios.")

        # 2. Berechnung aller fehlenden Größen, soweit möglich
        output.append("\n--- Step 2: Calculations ---")

        # 2.1. Absolute Zahlen aus absolute number und absolute number difference
        if self.one_case == 0:
            if self.abs_number_diff is not None:
                if self.abs_number_base is not None and self.abs_number_new is None:
                    self.abs_number_new = self.abs_number_base - self.abs_number_diff
                    output.append(f"2.1: Calculated absolute number (new) = {self.abs_number_new}")
                elif self.abs_number_new is not None and self.abs_number_base is None:
                    self.abs_number_base = self.abs_number_new + self.abs_number_diff
                    output.append(f"2.1: Calculated absolute number (base) = {self.abs_number_base}")
                 
        # 2.2. Absolute risk from number and reference class size
        if self.abs_number_base is not None and self.ref_class_size_base is not None:
            calculated_base = (self.abs_number_base / self.ref_class_size_base) * 100
            if self.abs_risk_base is None:
                self.abs_risk_base = calculated_base
                output.append(f"2.2: Calculated absolute risk (base) = {self.abs_risk_base:.2f}%")
        if self.abs_number_new is not None and self.ref_class_size_new is not None:
            calculated_new = (self.abs_number_new / self.ref_class_size_new) * 100
            if self.abs_risk_new is None:
                self.abs_risk_new = calculated_new
                output.append(f"2.2: Calculated absolute risk (new) = {self.abs_risk_new:.2f}%")

        # 2.3. Absolute risk from rel_risk
        if self.rel_risk is not None:
            if self.abs_risk_base is not None and self.abs_risk_new is None:
                self.abs_risk_new = self.abs_risk_base * self.rel_risk
                output.append(f"2.3: From relative risk and base absolute risk calculated: absolute risk (new) = {self.abs_risk_new:.2f}%")
            elif self.abs_risk_new is not None and self.abs_risk_base is None:
                self.abs_risk_base = self.abs_risk_new / self.rel_risk
                output.append(f"2.3: From relative risk and new absolute risk calculated: absolute risk (base) = {self.abs_risk_base:.2f}%")

        # 2.4. Relative risk if both absolute risks are given
        if self.abs_risk_base is not None and self.abs_risk_new is not None:
            calculated_rel = self.abs_risk_new / self.abs_risk_base if self.abs_risk_base != 0 else None
            if self.rel_risk is None and calculated_rel is not None:
                self.rel_risk = calculated_rel
                output.append(f"2.4: Calculated relative risk = {self.rel_risk:.2f}")

        # 3. Qualitative assessment of yes/no fields
        output.append("\n--- Step 3: Qualitative Assessment ---")
        # 3.1. Check sources
        if self.source_base or self.source_new:
            output.append("3.1: Sources provided – please verify:")
            if self.source_base:
                output.append(f"     • Source for base risk: {self.source_base}")
            if self.source_new:
                output.append(f"     • Source for new risk: {self.source_new}")
        else:
            output.append("3.1: Warning: No sources provided.")

        # 3.2. Check verbal risk descriptors
        if self.verbal_desc_base or self.verbal_desc_new or self.verbal_desc_change:
            output.append("3.2: Warning: Verbal risk descriptors present. Please verify definitions for:")
            if self.verbal_desc_base:
                output.append(f"     • verbal_risk_descriptor_base: {self.verbal_desc_base}")
            if self.verbal_desc_new:
                output.append(f"     • verbal_risk_descriptor_new: {self.verbal_desc_new}")
            if self.verbal_desc_change:
                output.append(f"     • verbal_risk_descriptor_change: {self.verbal_desc_change}")
        else:
            output.append("3.2: No verbal risk descriptors present.")

        # 3.3. Check reference class descriptions
        if self.ref_class_desc_base or self.ref_class_desc_new:
            output.append("3.3: Reference class description present.")
        else:
            output.append("3.3: Warning: No reference class provided. Please check the text for an explicit description.")

        # 4. Check missing values
        output.append("\n--- Step 4: Missing Values Check ---")
        if self.one_case == 1:
            if self.abs_risk_base is not None:
                output.append("4.1: Absolute risk calculable.")
            else:
                output.append("4.1: No absolute risk provided or calculable – risk communication not transparent.")
        else:
            if self.abs_risk_base is not None and self.abs_risk_new is not None:
                output.append("4.1: Both absolute risks calculable. Risk communication transparent.")
            elif self.abs_risk_base is None and self.abs_risk_new is not None:
                output.append("4.1: Missing absolute risk for base case, but new absolute risk provided – risk communication not transparent.")
            elif self.abs_risk_base is not None and self.abs_risk_new is None:
                output.append("4.1: Base absolute risk provided, but new absolute risk missing – risk communication not transparent.")
            else:
                output.append("4.1: Neither absolute risk provided nor calculable – risk communication not transparent.")

        # 5. Transparent presentation to end user
        output.append("\n--- Step 5: Transparent Presentation ---")
        if self.abs_risk_base is not None:
            per_100_base = self.abs_risk_base
            output.append(f"5.1: Absolute risk (base): {self.abs_risk_base:.2f}% ({per_100_base:.2f} per 100)")
        if self.abs_risk_new is not None:
            per_100_new = self.abs_risk_new
            output.append(f"5.1: Absolute risk (new): {self.abs_risk_new:.2f}% ({per_100_new:.2f} per 100)")
        if self.rel_risk is not None:
            change_pct = abs((self.rel_risk - 1) * 100)
            if self.rel_risk < 1:
                output.append(f"5.2: The risk in the new case is {change_pct:.2f}% lower than in the base case.")
            elif self.rel_risk > 1:
                output.append(f"5.2: The risk in the new case is {change_pct:.2f}% higher than in the base case.")
            else:
                output.append("5.2: The risk in the new case is the same as in the base case.")
        return "\n".join(output)  
            

# Hauptprogramm
if __name__ == "__main__":
    file_path = "Third_Version_MR/4risk_example.json"
    risk_instance = get_risk_instance(file_path)

    processor = RiskProcessor(risk_instance)
    result= processor.process()
    print(result)
