from deserializer import get_risk_instance

# Dies noch automatisieren -> für jede Inferenz wird Output-Datei erstellt, 
# worauf die python-logik automatisch Zugriff hat
file_path = "output/4risk_example.json"
risk_instance = get_risk_instance(file_path)



# Variablen extrahieren aus risk_instance und definieren

#Grundklassifizierung 
risk_com = risk_instance.risk_com
one_case = risk_instance.one_case

# Absolute risks
abs_risk_base = risk_instance.absolute_risk_base
abs_risk_new = risk_instance.absolute_risk_new

# Absolute numbers
abs_number_base = risk_instance.absolute_number_base
abs_number_new = risk_instance.absolute_number_new

# Differences
abs_risk_diff = risk_instance.absolute_risk_difference
abs_number_diff = risk_instance.absolute_number_difference

# Relative risk
rel_risk = risk_instance.relative_risk

# Verbal risk descriptors
verbal_desc_base = risk_instance.verbal_risk_descriptor_base
verbal_desc_new = risk_instance.verbal_risk_descriptor_new
verbal_desc_change = risk_instance.verbal_risk_descriptor_change

# Reference class size
ref_class_size_base = risk_instance.reference_class_size_base
ref_class_size_new = risk_instance.reference_class_size_new

# Reference class description
ref_class_desc_base = risk_instance.reference_class_description_base
ref_class_desc_new = risk_instance.reference_class_description_new

# Sources
source_base = risk_instance.source_base
source_new = risk_instance.source_new

# Topic and unit
topic_unit = risk_instance.topic_and_unit



# Ausgeschlossene Funktionalitäten bis dato
# Umformulierung in gute Risikokommunikation via Textgenerierung 
# Reduktion von positive/ negative framing, e.g. 90% survival chance vs. 10% death risk 
# Reduktion von Framing durch Inhalte, e.g. mehr über Nutzen als über Schaden berichtet 

# 1. Grundlegende Klassifizierung 
# 1.1 (-> Ausgabe). Riskokommunikation gegeben: nein -> break & Ausgabe 
# 1.2 (-> keine Ausgabe). Unterscheidung zwischen one case und two case -> bereits in Binärvariablen gespeichert 


# 2 (-> keine Ausgabe) & als loop mit n = 2 ?. Berechnung aller fehlenden Größen, soweit möglich 
# 2.1. Berechnung des absoluten Risikos aus gegebener absoluten number und reference class size
# 2.2. Berechnung absoluter Zahlen aus absolute number (base case bzw. new case) und absolute number difference 
# 2.2. Berechnung des absoluten Risikos (base case bzw. new case) aus absoluten Risiko (new case bzw. base case) und relativem Risiko 
# 2.3. Berechnung des relativen Risikos, falls beide absoluten Risiken gegeben sind (bzw. beide indirekt berechenbar sind)


# 3 (-> Ausgabe). Bewertung von ja/ nein Strings (sources, verbal risk descriptors, reference classes) -> für one und two case Fall 
# 3.1. Prüfung, ob Sources gegeben: ja -> Meldung zur Überprüfung, nein -> Meldung Achtung 
# 3.2. Prüfung, ob verbale Risikodeskriptoren gegegeben: ja -> Meldung Achtung, schauen ob genauer gegeben
# 3.3. Prüfung, ob reference class(es) gegeben sind: nein -> Meldung Achtung, worauf beziehen sich Aussagen 


# 4 (-> Ausgabe). Bewertung, welche Größen nicht gegeben sind 
# 4.1. Absolute risk(s) berechenbar?: nein -> Meldung, Risikokommunikation intransparent 

# 5 (-> Ausgabe). Transparente Risikodarstellung für den Endnutzer 
# 5.1. Umrechnung und Ausgabe der absolute risk(s) in (a) Prozentzahl und (b) x in 100 -> Reduzierung von ratio bias # Hier grafische Darstellung möglich
