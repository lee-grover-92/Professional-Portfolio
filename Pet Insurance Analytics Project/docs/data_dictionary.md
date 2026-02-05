# 📚 Data Dictionary – Pet Insurance Analytics Project

This data dictionary describes the structure and meaning of each table and column in the pet insurance analytics database.

---

## 🧑‍💼 `customers`

| Column        | Data Type      | Description                              |
|---------------|----------------|------------------------------------------|
| `customer_id` | INT (PK)       | Unique identifier for each customer      |
| `first_name`  | VARCHAR(50)    | Customer's first name                    |
| `last_name`   | VARCHAR(50)    | Customer's last name                     |
| `email`       | VARCHAR(100)   | Customer's email address                 |
| `phone`       | VARCHAR(50)    | Customer's phone number                  |
| `address`     | VARCHAR(255)   | Street address                           |
| `city`        | VARCHAR(100)   | City of residence                        |
| `country`     | VARCHAR(100)   | Country of residence                     |
| `created_at`  | DATE           | Date the customer account was created    |

---

## 🐶 `pets`

| Column            | Data Type      | Description                                      |
|-------------------|----------------|--------------------------------------------------|
| `pet_id`          | INT (PK)       | Unique identifier for each pet                   |
| `customer_id`     | INT (FK)       | Links to `customers.customer_id`                 |
| `species`         | VARCHAR(20)    | Species of the pet (e.g., Dog, Cat)              |
| `breed`           | VARCHAR(100)   | Breed of the pet                                 |
| `gender`          | VARCHAR(10)    | Gender of the pet (e.g., Male, Female)           |
| `birthdate`       | DATE           | Date of birth                                    |
| `age`             | INT            | Age in years (calculated from birthdate)         |
| `weight_kg`       | DECIMAL(5,2)   | Weight in kilograms                              |
| `microchip_id`    | VARCHAR(20)    | Unique microchip identifier                      |
| `neutered_spayed` | TINYINT        | 1 = Yes, 0 = No                                  |

---

## 📦 `products`

| Column            | Data Type      | Description                                      |
|-------------------|----------------|--------------------------------------------------|
| `product_id`      | INT (PK)       | Unique identifier for each insurance product     |
| `product_name`    | VARCHAR(100)   | Name of the insurance product                    |
| `coverage_type`   | VARCHAR(50)    | Type of coverage (e.g., Accident, Comprehensive) |
| `annual_limit`    | INT            | Maximum annual coverage amount                   |
| `deductible`      | INT            | Annual deductible amount                         |
| `monthly_premium` | DECIMAL(10,2)  | Monthly premium cost                             |

---

## 📄 `policies`

| Column               | Data Type     | Description                                  |
|----------------------|---------------|----------------------------------------------|
| `policy_id`          | INT (PK)       | Unique identifier for each policy           |
| `pet_id`             | INT (FK)       | Links to `pets.pet_id`                      |
| `product_id`         | INT (FK)       | Links to `products.product_id`              |
| `start_date`         | DATE           | Policy start date                           |
| `end_date`           | DATE           | Policy end date                             |
| `age_at_policy_start`| INT            | Pet's age at the time of policy start       |
| `active`             | TINYINT        | 1 = Active, 0 = Inactive                    |

---

## 🧾 `claims`

| Column         | Data Type      | Description                                    |
|----------------|----------------|------------------------------------------------|
| `claim_id`     | INT (PK)       | Unique identifier for each claim               |
| `policy_id`    | INT (FK)       | Links to `policies.policy_id`                  |
| `claim_date`   | DATE           | Date the claim was submitted                   |
| `claim_amount` | DECIMAL(10,2)  | Total amount claimed                           |
| `diagnosis`    | VARCHAR(100)   | Diagnosis or reason for the claim              |
| `status`       | VARCHAR(20)    | Claim status (e.g., Approved, Denied, Pending) |

---

## 🏥 `vet_visits`

| Column       | Data Type      | Description                                 |
|--------------|----------------|---------------------------------------------|
| `visit_id`   | INT (PK)       | Unique identifier for each vet visit        |
| `claim_id`   | INT (FK)       | Links to `claims.claim_id`                  |
| `visit_date` | DATE           | Date of the vet visit                       |
| `vet_clinic` | VARCHAR(100)   | Name of the veterinary clinic               |
| `visit_type` | VARCHAR(50)    | Type of visit (e.g., Emergency, Routine)    |
| `notes`      | VARCHAR(255)   | Additional notes or observations            |

---

## 💳 `invoice_line_items`

| Column         | Data Type      | Description                                 |
|----------------|----------------|---------------------------------------------|
| `line_item_id` | INT (PK)       | Unique identifier for each invoice line     |
| `visit_id`     | INT (FK)       | Links to `vet_visits.visit_id`              |
| `treatment_code`| VARCHAR(20)   | Code for the treatment or procedure         |
| `description`  | VARCHAR(100)   | Description of the treatment or service     |
| `cost`         | DECIMAL(10,2)  | Cost of the treatment                       |

---

## 💰 `claim_payments`

| Column         | Data Type      | Description                                   |
|----------------|----------------|-----------------------------------------------|
| `payment_id`   | INT (PK)       | Unique identifier for each payment            |
| `claim_id`     | INT (FK)       | Links to `claims.claim_id`                    |
| `payment_date` | DATE           | Date the payment was issued                   |
| `amount_paid`  | DECIMAL(10,2)  | Amount paid to the customer or vet            |
| `payment_method`| VARCHAR(50)   | Method of payment (e.g., Bank Transfer, Card) |

---

For questions or suggestions, feel free to contact the project owner.
