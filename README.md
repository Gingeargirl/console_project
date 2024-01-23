Jedná se o jednoduchý konzolový projekt Pojištěnce.

Projekt je tvořen čtyřmi soubory a je v AJ: 1) insured_person, 2) insurance_management, 3) insurance_evidence, 4) insurance_records.pkl

- insured_person: Soubor obsahuje vytvoření instance třídy pojištěného a výpis v podobě tostring, který vrací vlastnosti pojištěného.
- insurance_management: Do soboru je importován pickle (ukládání souboru) a třída InsuredPerson. Je zde vytvořena třída InsuranceManagement, v které definujeme metody: init() add_insured_person(insured_person) remove_insured_person(first_name, last_name, phone_number)                              display_list(): find_insured_person(first_name, last_name): save_to_file(file_name): load_from_file(file_name):
- insurance_evidence: = main = hlavní části programu, kde se spouští hlavní algoritmus programu
