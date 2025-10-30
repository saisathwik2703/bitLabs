class Patient:
    """
    Represents a patient record with name, age, and disease.
    This class helps organize the data neatly.
    """
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        """Returns a string representation of the patient for easy printing."""
        return f"Name: {self.name:<10} | Age: {self.age:<3} | Disease: {self.disease}"

    def to_dict(self):
        """Returns the patient data as a dictionary."""
        return {"Name": self.name, "Age": self.age, "Disease": self.disease}

# --- Data Storage ---
# Use a list to store patient objects (records)
patient_records = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu"),
    Patient("Diana", 62, "Hypertension")
]

# --- Core Functions ---

def add_patient_record():
    """Prompts the user for details and adds a new patient to the records."""
    print("\n--- Add New Patient ---")
    name = input("Enter Patient Name: ").strip()
    
    # Input validation for Age
    while True:
        try:
            age = int(input("Enter Patient Age: ").strip())
            if age <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid age. Please enter a positive whole number.")
            
    disease = input("Enter Patient Disease: ").strip()
    
    if name and age and disease:
        new_patient = Patient(name, age, disease)
        patient_records.append(new_patient)
        print(f"✅ Success: Patient '{name}' added to records.")
    else:
        print("❌ Error: All fields must be filled.")

def search_patients_by_disease():
    """
    Searches the patient records for all patients matching a specified disease.
    """
    print("\n--- Search by Disease ---")
    search_term = input("Enter Disease to Search: ").strip()

    if not search_term:
        print("⚠️ Search term cannot be empty.")
        return

    # Case-insensitive search using list comprehension
    found_patients = [
        patient for patient in patient_records 
        if patient.disease.lower() == search_term.lower()
    ]

    if found_patients:
        print(f"\nPatients found with '{search_term}':")
        for patient in found_patients:
            print(f"  - {patient.name} (Age: {patient.age})")
        
        # Expected output format simulation:
        patient_names = [p.name for p in found_patients]
        print(f"\nExpected Output format: Patients with {search_term}: {patient_names}")

    else:
        print(f"No patients found with the disease '{search_term}'.")

def display_all_patients():
    """Displays a formatted list of all current patient records."""
    if not patient_records:
        print("The patient database is currently empty.")
        return

    print("\n" + "=" * 50)
    print(f"CURRENT PATIENT DATABASE ({len(patient_records)} Records)")
    print("-" * 50)
    
    for patient in patient_records:
        print(f"| {patient}")
    
    print("=" * 50)


# --- Main Program Execution ---

print("--- Hospital Patient Management System ---")

while True:
    display_all_patients()
    
    # Display Menu
    print("\nPlease select an action:")
    print("1: Add New Patient Record")
    print("2: Search Patients by Disease")
    print("3: Exit System")
    
    # Get user choice
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("❌ Invalid input. Please enter a number from 1 to 3.")
        continue

    # Process Choice
    if choice == 1:
        add_patient_record()
            
    elif choice == 2:
        search_patients_by_disease()

    elif choice == 3:
        print("\nThank you for using the Patient Management System. Goodbye!")
        break
        
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
        
    print("\n" + "~" * 50 + "\n")
