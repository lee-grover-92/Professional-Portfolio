import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

# CONFIGURATION

NUM_CUSTOMERS = 60_000
NUM_PETS = 100_000
NUM_PRODUCTS = 27
NUM_POLICIES = 120_000
NUM_CLAIMS = 200_000

NUM_VET_VISITS = 250_000
NUM_INVOICE_ITEMS = 600_000
NUM_CLAIM_PAYMENTS = 300_000

OUTPUT_DIR = "./pet_data_project/data/raw/"

TODAY = date.today()

# SPECIES DISTRIBUTION

SPECIES_WEIGHTS = {
    "Dog": 0.58,
    "Cat": 0.37,
    "Rabbit": 0.05
}

# BREEDS

dog_breeds = [
    "Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog",
    "Bulldog", "Poodle", "Beagle", "Rottweiler", "Yorkshire Terrier", "Boxer",
    "Dachshund", "Great Dane", "Siberian Husky", "Doberman", "Shih Tzu",
    "Miniature Schnauzer", "Cavalier King Charles Spaniel", "Australian Shepherd",
    "Border Collie", "Chihuahua", "Pug", "Maltese", "Cocker Spaniel",
    "Bernese Mountain Dog", "Basset Hound", "Akita", "Weimaraner", "Newfoundland",
    "St. Bernard", "Greyhound", "Whippet", "Staffordshire Bull Terrier",
    "English Springer Spaniel", "Boston Terrier", "Havanese", "Samoyed",
    "Irish Setter", "Shiba Inu", "Papillon", "Collie", "Airedale Terrier",
    "Alaskan Malamute", "Belgian Malinois", "Bullmastiff", "Cane Corso",
    "Chow Chow", "Pointer", "Rhodesian Ridgeback", "Vizsla", "Goldendoodle",
    "Labradoodle"
]

cat_breeds = [
    "Siamese", "Persian", "Maine Coon", "Bengal", "Sphynx", "British Shorthair",
    "Ragdoll", "Scottish Fold", "Abyssinian", "Birman", "Russian Blue",
    "Norwegian Forest Cat", "Savannah", "Oriental Shorthair", "Devon Rex",
    "Cornish Rex", "American Shorthair", "Turkish Angora", "Himalayan",
    "Tonkinese", "Manx", "Egyptian Mau", "Chartreux", "Balinese", "Snowshoe",
    "Somali", "Japanese Bobtail", "Korat", "Munchkin", "Ocicat", "Siberian"
]

rabbit_breeds = [
    "Dutch", "Lionhead", "Mini Lop", "Rex", "Flemish Giant", "Netherland Dwarf",
    "English Lop", "French Lop", "Harlequin", "Havana", "Silver Fox",
    "American Fuzzy Lop", "Mini Rex", "Californian", "New Zealand White"
]

BREEDS = {
    "Dog": dog_breeds,
    "Cat": cat_breeds,
    "Rabbit": rabbit_breeds
}

BRACHY_DOG_BREEDS = {
    "French Bulldog", "Bulldog", "Pug", "Boston Terrier", "Shih Tzu",
    "Cavalier King Charles Spaniel", "Boxer"
}

# DIAGNOSES (EXPANDED + WEIGHTED BY SPECIES

# Core diagnosis universe (for reference / mapping)
ALL_DIAGNOSES = [
    # General
    "Allergy", "Injury", "Dental Issue", "Skin Condition", "Digestive Issue",
    "Ear Infection", "Eye Infection", "Respiratory Issue", "Parasites",
    "Tumor", "Laceration", "Abscess", "Heatstroke", "Poisoning",
    "Foreign Body Ingestion", "Dehydration", "Fever", "Infection (General)",
    "Soft Tissue Trauma", "Behavioural Issue",

    # Dog-specific
    "Hip Dysplasia", "Elbow Dysplasia", "Cruciate Ligament Rupture",
    "Pancreatitis", "Bloat (GDV)", "Kennel Cough", "Heartworm", "Epilepsy",
    "Anal Gland Infection", "Dermatitis", "Cherry Eye",
    "Intervertebral Disc Disease (IVDD)",

    # Cat-specific
    "Urinary Blockage", "Feline Asthma", "Feline Leukemia Virus (FeLV)",
    "Feline Immunodeficiency Virus (FIV)", "Hyperthyroidism", "Kidney Disease",
    "Stomatitis", "Hairball Obstruction",
    "Feline Lower Urinary Tract Disease (FLUTD)",

    # Rabbit-specific
    "GI Stasis", "Dental Malocclusion", "Snuffles (Pasteurella)",
    "Myxomatosis", "E. Cuniculi", "Flystrike", "Pododermatitis",
    "Respiratory Infection"
]

# Species-specific weighted diagnosis sets
DIAGNOSES = {
    "Dog": [
        ("Allergy", 0.07), ("Injury", 0.10), ("Dental Issue", 0.06),
        ("Skin Condition", 0.08), ("Digestive Issue", 0.08),
        ("Ear Infection", 0.10), ("Eye Infection", 0.04),
        ("Respiratory Issue", 0.05), ("Parasites", 0.05),
        ("Tumor", 0.04), ("Laceration", 0.03), ("Abscess", 0.02),
        ("Foreign Body Ingestion", 0.03), ("Soft Tissue Trauma", 0.03),
        ("Hip Dysplasia", 0.04), ("Elbow Dysplasia", 0.02),
        ("Cruciate Ligament Rupture", 0.03), ("Pancreatitis", 0.03),
        ("Bloat (GDV)", 0.01), ("Kennel Cough", 0.03),
        ("Epilepsy", 0.02), ("Anal Gland Infection", 0.03),
        ("Dermatitis", 0.03), ("Intervertebral Disc Disease (IVDD)", 0.02)
    ],
    "Cat": [
        ("Allergy", 0.07), ("Injury", 0.08), ("Dental Issue", 0.08),
        ("Skin Condition", 0.06), ("Digestive Issue", 0.07),
        ("Ear Infection", 0.06), ("Eye Infection", 0.05),
        ("Respiratory Issue", 0.06), ("Parasites", 0.05),
        ("Tumor", 0.04), ("Laceration", 0.03), ("Abscess", 0.03),
        ("Urinary Blockage", 0.08), ("Feline Asthma", 0.04),
        ("Feline Leukemia Virus (FeLV)", 0.02),
        ("Feline Immunodeficiency Virus (FIV)", 0.02),
        ("Hyperthyroidism", 0.05), ("Kidney Disease", 0.05),
        ("Stomatitis", 0.03), ("Hairball Obstruction", 0.03),
        ("Feline Lower Urinary Tract Disease (FLUTD)", 0.05)
    ],
    "Rabbit": [
        ("GI Stasis", 0.20), ("Dental Malocclusion", 0.18),
        ("Injury", 0.08), ("Parasites", 0.08),
        ("Skin Condition", 0.08), ("Eye Infection", 0.05),
        ("Respiratory Infection", 0.10), ("Abscess", 0.05),
        ("Snuffles (Pasteurella)", 0.08), ("Flystrike", 0.05),
        ("Pododermatitis", 0.05)
    ]
}

# Diagnosis → typical claim amount ranges (GBP)
DIAGNOSIS_COST_RANGES = {
    "Allergy": (80, 400),
    "Injury": (150, 1200),
    "Dental Issue": (200, 900),
    "Skin Condition": (80, 500),
    "Digestive Issue": (120, 800),
    "Ear Infection": (80, 300),
    "Eye Infection": (80, 300),
    "Respiratory Issue": (150, 900),
    "Parasites": (60, 250),
    "Tumor": (500, 3000),
    "Laceration": (120, 700),
    "Abscess": (120, 600),
    "Heatstroke": (300, 1500),
    "Poisoning": (250, 2000),
    "Foreign Body Ingestion": (400, 2500),
    "Dehydration": (120, 600),
    "Infection (General)": (120, 700),
    "Soft Tissue Trauma": (150, 900),
    "Hip Dysplasia": (800, 3000),
    "Elbow Dysplasia": (700, 2500),
    "Cruciate Ligament Rupture": (900, 3500),
    "Pancreatitis": (400, 2000),
    "Bloat (GDV)": (1200, 5000),
    "Kennel Cough": (120, 500),
    "Epilepsy": (200, 1200),
    "Anal Gland Infection": (80, 300),
    "Dermatitis": (80, 500),
    "Intervertebral Disc Disease (IVDD)": (800, 3500),
    "Urinary Blockage": (400, 2000),
    "Feline Asthma": (150, 800),
    "Feline Leukemia Virus (FeLV)": (300, 1500),
    "Feline Immunodeficiency Virus (FIV)": (300, 1500),
    "Hyperthyroidism": (250, 1200),
    "Kidney Disease": (300, 2000),
    "Stomatitis": (200, 900),
    "Hairball Obstruction": (120, 600),
    "Feline Lower Urinary Tract Disease (FLUTD)": (250, 1500),
    "GI Stasis": (200, 1200),
    "Dental Malocclusion": (150, 800),
    "Snuffles (Pasteurella)": (150, 700),
    "Myxomatosis": (200, 1200),
    "E. Cuniculi": (150, 800),
    "Flystrike": (250, 1200),
    "Pododermatitis": (150, 700),
    "Respiratory Infection": (150, 900)
}

# VET CLINICS (EXPANDED)

VET_CLINICS = [
    "Happy Paws Clinic", "Greenfield Vets", "PetCare Hospital",
    "Northside Animal Clinic", "Valley Veterinary Centre",
    "Riverside Veterinary Group", "BlueCross Animal Hospital",
    "Oakwood Companion Care", "St. Francis Pet Clinic",
    "Millbrook Animal Health", "Southdown Vets",
    "Thames Valley Pet Hospital", "Cotswold Veterinary Centre",
    "Willow Tree Vets", "Harbour View Veterinary Practice",
    "Meadowbrook Veterinary Surgery", "Lakeside Animal Health",
    "Birchwood Vets", "Ashfield Companion Clinic",
    "Redhill Veterinary Group", "Forest Edge Vets",
    "Beacon Hill Animal Hospital", "Parkside Veterinary Centre",
    "Riverbank Vets", "Westgate Animal Clinic",
    "Maple Leaf Veterinary Surgery", "Orchard Lane Vets",
    "Kingswood Pet Hospital", "Seaside Veterinary Practice",
    "Hilltop Animal Care", "Brookside Veterinary Group",
    "Cedar Grove Vets", "Longbridge Animal Clinic",
    "Northgate Veterinary Centre", "Silverwood Vets",
    "Elm House Animal Hospital", "Paws & Claws Veterinary Surgery",
    "The Pet Wellness Centre", "The Animal Health Hub"
]

# TREATMENT CODES (EXPANDED + WEIGHTED)

TREATMENTS = [
    # Consultations
    ("CONSULT", "Consultation Fee", 0.20),
    ("FOLLOW", "Follow-up Consultation", 0.10),
    ("OOH", "Out-of-Hours Consultation", 0.03),
    ("EMERG", "Emergency Consultation", 0.04),
    ("EXAM", "Full Physical Exam", 0.05),

    # Diagnostics
    ("BLOOD", "Blood Test", 0.06),
    ("URINE", "Urinalysis", 0.03),
    ("XRAY", "X-Ray Imaging", 0.05),
    ("ULTRA", "Ultrasound", 0.04),
    ("MRI", "MRI Scan", 0.01),
    ("CT", "CT Scan", 0.01),
    ("ECG", "Electrocardiogram", 0.01),
    ("BIOPSY", "Tissue Biopsy", 0.01),
    ("CULTURE", "Bacterial Culture", 0.01),
    ("CYTO", "Cytology", 0.01),
    ("ALLERGY", "Allergy Testing", 0.01),

    # Treatments / Procedures
    ("MED", "Medication", 0.10),
    ("INJECT", "Injection", 0.04),
    ("IVFLUID", "IV Fluids", 0.03),
    ("WOUND", "Wound Care", 0.03),
    ("CAST", "Casting / Splint", 0.01),
    ("SUTURE", "Suturing", 0.02),
    ("DENT", "Dental Treatment", 0.03),
    ("DENTCLEAN", "Dental Cleaning", 0.02),
    ("NEUTER", "Neuter/Spay", 0.02),
    ("SURG", "Surgery (General)", 0.03),
    ("ORTHO", "Orthopaedic Surgery", 0.01),
    ("OPHTH", "Ophthalmic Procedure", 0.01),
    ("ENT", "Ear Treatment", 0.02),
    ("GASTRO", "Gastrointestinal Procedure", 0.01),

    # Preventative
    ("VACC", "Vaccination", 0.04),
    ("FLEATICK", "Flea/Tick Treatment", 0.02),
    ("DEWORM", "Deworming", 0.02),
    ("MICROCHIP", "Microchipping", 0.01),

    # Rehab / Specialist
    ("PHYSIO", "Physiotherapy", 0.01),
    ("HYDRO", "Hydrotherapy", 0.01),
    ("CHIRO", "Chiropractic", 0.005),
    ("BEHAV", "Behavioural Assessment", 0.005)
]

# PRODUCTS

PRODUCTS = [
    ("Lifetime Essential", "Lifetime"),
    ("Lifetime Plus", "Lifetime"),
    ("Lifetime Premier", "Lifetime"),
    ("Lifetime Elite", "Lifetime"),
    ("Lifetime Ultra", "Lifetime"),
    ("Lifetime Supreme", "Lifetime"),
    ("Time-Limited Basic", "Time-Limited"),
    ("Time-Limited Standard", "Time-Limited"),
    ("Time-Limited Extra", "Time-Limited"),
    ("Time-Limited Premium", "Time-Limited"),
    ("Max Benefit 1k", "Maximum Benefit"),
    ("Max Benefit 3k", "Maximum Benefit"),
    ("Max Benefit 5k", "Maximum Benefit"),
    ("Max Benefit 7k", "Maximum Benefit"),
    ("Max Benefit 10k", "Maximum Benefit"),
    ("Accident-Only Basic", "Accident-Only"),
    ("Accident-Only Plus", "Accident-Only"),
    ("Accident-Only Elite", "Accident-Only"),
    ("Dental Care Add-on", "Add-on"),
    ("Physiotherapy Add-on", "Add-on"),
    ("Travel Cover Add-on", "Add-on"),
    ("Senior Pet Add-on", "Add-on"),
    ("Puppy/Kitten Booster", "Add-on"),
    ("Rabbit Essential", "Small Pet"),
    ("Rabbit Plus", "Small Pet"),
    ("Small Mammal Basic", "Small Pet"),
    ("Small Mammal Premium", "Small Pet")
]

# HELPERS

def weighted_choice(items, weights):
    return random.choices(items, weights=weights, k=1)[0]

def random_claim_amount_for_diagnosis(diagnosis):
    low, high = DIAGNOSIS_COST_RANGES.get(diagnosis, (50, 5000))
    base = random.uniform(low, high)
    return round(base, 2)

def species_weight(species):
    if species == "Dog":
        return round(random.uniform(5, 55), 1)
    elif species == "Cat":
        return round(random.uniform(2, 8), 1)
    else:
        return round(random.uniform(1, 4), 1)

def adjust_dog_diagnosis_weights_for_brachy(breed, diag_list, diag_weights):
    if breed not in BRACHY_DOG_BREEDS:
        return diag_weights
    adjusted = []
    for d, w in zip(diag_list, diag_weights):
        if d in ["Respiratory Issue", "Skin Condition", "Dermatitis", "Eye Infection"]:
            adjusted.append(w * 1.8)
        else:
            adjusted.append(w)
    total = sum(adjusted)
    return [w / total for w in adjusted]


# GENERATION FUNCTIONS

def generate_customers(n):
    rows = []
    for i in range(1, n + 1):
        rows.append({
            "customer_id": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address().replace("\n", ", "),
            "city": fake.city(),
            "country": fake.country(),
            "created_at": fake.date_between(start_date="-8y", end_date="today")
        })
    return pd.DataFrame(rows)

def generate_pets(num_pets, num_customers):
    rows = []
    species_list = list(SPECIES_WEIGHTS.keys())
    species_weights = list(SPECIES_WEIGHTS.values())

    pets_created = 0
    pet_id = 1

    for customer_id in range(1, num_customers + 1):
        if pets_created >= num_pets:
            break

        r = random.random()
        if r < 0.15:
            num_for_customer = 0
        elif r < 0.70:
            num_for_customer = 1
        elif r < 0.92:
            num_for_customer = 2
        elif r < 0.98:
            num_for_customer = 3
        else:
            num_for_customer = 4

        for _ in range(num_for_customer):
            if pets_created >= num_pets:
                break

            species = weighted_choice(species_list, species_weights)
            breed = random.choice(BREEDS[species])
            age = random.randint(1, 18)
            birthdate = fake.date_between(start_date=f"-{age+1}y", end_date=f"-{age}y")

            rows.append({
                "pet_id": pet_id,
                "customer_id": customer_id,
                "species": species,
                "breed": breed,
                "gender": random.choice(["Male", "Female"]),
                "birthdate": birthdate,
                "age": age,
                "weight_kg": species_weight(species),
                "microchip_id": fake.unique.ean(length=13),
                "neutered_spayed": random.choice([0, 1])
            })

            pet_id += 1
            pets_created += 1

    return pd.DataFrame(rows)

def generate_products():
    rows = []
    for i, (name, category) in enumerate(PRODUCTS, start=1):
        rows.append({
            "product_id": i,
            "product_name": name,
            "coverage_type": category,
            "annual_limit": random.choice([1000, 2000, 4000, 8000, 12000]),
            "deductible": random.choice([50, 75, 100, 150, 250]),
            "monthly_premium": round(random.uniform(8, 95), 2)
        })
    return pd.DataFrame(rows)

def generate_policies(n, pets_df, num_products):
    rows = []
    pet_ids = pets_df["pet_id"].tolist()

    for i in range(1, n + 1):
        pet_id = random.choice(pet_ids)
        birthdate = pets_df.loc[pets_df.pet_id == pet_id, "birthdate"].values[0]

        start = fake.date_between(start_date="-5y", end_date="today")
        end = start + timedelta(days=random.randint(180, 365 * 3))

        if random.random() < 0.10:
            cancel_days = random.randint(30, 365)
            end = min(end, start + timedelta(days=cancel_days))

        age_at_start = start.year - pd.to_datetime(birthdate).year

        active = 1 if (end >= TODAY and random.random() > 0.15) else 0

        rows.append({
            "policy_id": i,
            "pet_id": pet_id,
            "product_id": random.randint(1, num_products),
            "start_date": start,
            "end_date": end,
            "age_at_policy_start": age_at_start,
            "active": active
        })
    return pd.DataFrame(rows)

def generate_claims(n, pets_df, policies_df):
    rows = []
    for i in range(1, n + 1):
        policy_id = random.randint(1, len(policies_df))
        policy_row = policies_df.loc[policies_df.policy_id == policy_id].iloc[0]
        pet_id = policy_row["pet_id"]
        pet_row = pets_df.loc[pets_df.pet_id == pet_id].iloc[0]
        species = pet_row["species"]
        breed = pet_row["breed"]

        diag_list, diag_weights = zip(*DIAGNOSES[species])

        if species == "Dog":
            diag_weights = adjust_dog_diagnosis_weights_for_brachy(breed, diag_list, diag_weights)

        diagnosis = weighted_choice(diag_list, diag_weights)

        claim_date = fake.date_between(
            start_date=policy_row["start_date"],
            end_date=min(policy_row["end_date"], TODAY)
        )
        claim_amount = random_claim_amount_for_diagnosis(diagnosis)

        rows.append({
            "claim_id": i,
            "policy_id": policy_id,
            "claim_date": claim_date,
            "claim_amount": claim_amount,
            "diagnosis": diagnosis,
            "status": random.choice(["Open", "Closed", "Pending", "Rejected"])
        })
    return pd.DataFrame(rows)

def generate_vet_visits(n, claims_df):
    rows = []
    visit_types = ["Consultation", "Follow-up", "Emergency", "Surgery", "Diagnostics"]
    visit_weights = [0.45, 0.25, 0.10, 0.05, 0.15]

    for i in range(1, n + 1):
        claim_id = random.randint(1, len(claims_df))
        claim_date = claims_df.loc[claims_df.claim_id == claim_id, "claim_date"].values[0]

        visit_date = fake.date_between(start_date=claim_date, end_date=TODAY)
        visit_type = weighted_choice(visit_types, visit_weights)

        rows.append({
            "visit_id": i,
            "claim_id": claim_id,
            "visit_date": visit_date,
            "vet_clinic": random.choice(VET_CLINICS),
            "visit_type": visit_type,
            "notes": fake.sentence()
        })
    return pd.DataFrame(rows)

def generate_invoice_line_items(n, vet_visits_df):
    rows = []
    codes, descs, weights = zip(*TREATMENTS)
    code_to_desc = dict(zip(codes, descs))

    for i in range(1, n + 1):
        visit_id = random.randint(1, len(vet_visits_df))
        code = weighted_choice(codes, weights)
        desc = code_to_desc[code]

        if code in ["CONSULT", "FOLLOW", "OOH", "EMERG", "EXAM"]:
            cost = random.uniform(30, 120)
        elif code in ["MED"]:
            cost = random.uniform(20, 180)
        elif code in ["INJECT"]:
            cost = random.uniform(30, 120)
        elif code in ["BLOOD", "URINE", "XRAY", "ULTRA", "ECG", "CULTURE", "CYTO", "ALLERGY"]:
            cost = random.uniform(80, 400)
        elif code in ["MRI", "CT"]:
            cost = random.uniform(600, 2000)
        elif code in ["DENT", "DENTCLEAN"]:
            cost = random.uniform(150, 800)
        elif code in ["SURG", "ORTHO", "GASTRO", "OPHTH"]:
            cost = random.uniform(400, 3000)
        elif code in ["IVFLUID"]:
            cost = random.uniform(80, 400)
        elif code in ["WOUND", "CAST", "SUTURE", "ENT"]:
            cost = random.uniform(80, 500)
        elif code in ["VACC", "FLEATICK", "DEWORM", "MICROCHIP"]:
            cost = random.uniform(25, 120)
        elif code in ["PHYSIO", "HYDRO", "CHIRO", "BEHAV"]:
            cost = random.uniform(60, 250)
        else:
            cost = random.uniform(20, 1500)

        rows.append({
            "line_item_id": i,
            "visit_id": visit_id,
            "treatment_code": code,
            "description": desc,
            "cost": round(cost, 2)
        })
    return pd.DataFrame(rows)

def generate_claim_payments(n, claims_df):
    rows = []
    for i in range(1, n + 1):
        claim_id = random.randint(1, len(claims_df))
        claim_row = claims_df.loc[claims_df.claim_id == claim_id].iloc[0]
        claim_date = claim_row["claim_date"]
        claim_amount = claim_row["claim_amount"]

        paid = round(claim_amount * random.uniform(0.2, 1.0), 2)

        rows.append({
            "payment_id": i,
            "claim_id": claim_id,
            "payment_date": fake.date_between(start_date=claim_date, end_date=TODAY),
            "amount_paid": paid,
            "payment_method": random.choice(["Bank Transfer", "Credit Card Refund", "Cheque"])
        })
    return pd.DataFrame(rows)


# MAIN

if __name__ == "__main__":
    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Generating customers...")
    customers_df = generate_customers(NUM_CUSTOMERS)
    customers_df.to_csv(OUTPUT_DIR + "customers.csv", index=False)

    print("Generating pets...")
    pets_df = generate_pets(NUM_PETS, NUM_CUSTOMERS)
    pets_df.to_csv(OUTPUT_DIR + "pets.csv", index=False)

    print("Generating products...")
    products_df = generate_products()
    products_df.to_csv(OUTPUT_DIR + "products.csv", index=False)

    print("Generating policies...")
    policies_df = generate_policies(NUM_POLICIES, pets_df, NUM_PRODUCTS)
    policies_df.to_csv(OUTPUT_DIR + "policies.csv", index=False)

    print("Generating claims...")
    claims_df = generate_claims(NUM_CLAIMS, pets_df, policies_df)
    claims_df.to_csv(OUTPUT_DIR + "claims.csv", index=False)

    print("Generating vet visits...")
    vet_visits_df = generate_vet_visits(NUM_VET_VISITS, claims_df)
    vet_visits_df.to_csv(OUTPUT_DIR + "vet_visits.csv", index=False)

    print("Generating invoice line items...")
    invoice_items_df = generate_invoice_line_items(NUM_INVOICE_ITEMS, vet_visits_df)
    invoice_items_df.to_csv(OUTPUT_DIR + "invoice_line_items.csv", index=False)

    print("Generating claim payments...")
    claim_payments_df = generate_claim_payments(NUM_CLAIM_PAYMENTS, claims_df)
    claim_payments_df.to_csv(OUTPUT_DIR + "claim_payments.csv", index=False)

    print("FULL DATASET GENERATION COMPLETE!")