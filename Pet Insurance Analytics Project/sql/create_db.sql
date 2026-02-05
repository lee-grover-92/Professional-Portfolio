CREATE DATABASE pet_insurance;
USE pet_insurance;

-- -------------------------
-- CUSTOMERS
-- -------------------------
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(50),
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    created_at DATE
);

-- -------------------------
-- PETS
-- -------------------------
CREATE TABLE pets (
    pet_id INT PRIMARY KEY,
    customer_id INT,
    species VARCHAR(20),
    breed VARCHAR(100),
    gender VARCHAR(10),
    birthdate DATE,
    age INT,
    weight_kg DECIMAL(5,2),
    microchip_id VARCHAR(20),
    neutered_spayed TINYINT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- -------------------------
-- PRODUCTS
-- -------------------------
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    coverage_type VARCHAR(50),
    annual_limit INT,
    deductible INT,
    monthly_premium DECIMAL(10,2)
);

-- -------------------------
-- POLICIES
-- -------------------------
CREATE TABLE policies (
    policy_id INT PRIMARY KEY,
    pet_id INT,
    product_id INT,
    start_date DATE,
    end_date DATE,
    age_at_policy_start INT,
    active TINYINT,
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- -------------------------
-- CLAIMS
-- -------------------------
CREATE TABLE claims (
    claim_id INT PRIMARY KEY,
    policy_id INT,
    claim_date DATE,
    claim_amount DECIMAL(10,2),
    diagnosis VARCHAR(100),
    status VARCHAR(20),
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id)
);

-- -------------------------
-- VET VISITS
-- -------------------------
CREATE TABLE vet_visits (
    visit_id INT PRIMARY KEY,
    claim_id INT,
    visit_date DATE,
    vet_clinic VARCHAR(100),
    visit_type VARCHAR(50),
    notes VARCHAR(255),
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

-- -------------------------
-- INVOICE LINE ITEMS
-- -------------------------
CREATE TABLE invoice_line_items (
    line_item_id INT PRIMARY KEY,
    visit_id INT,
    treatment_code VARCHAR(20),
    description VARCHAR(100),
    cost DECIMAL(10,2),
    FOREIGN KEY (visit_id) REFERENCES vet_visits(visit_id)
);

-- -------------------------
-- CLAIM PAYMENTS
-- -------------------------
CREATE TABLE claim_payments (
    payment_id INT PRIMARY KEY,
    claim_id INT,
    payment_date DATE,
    amount_paid DECIMAL(10,2),
    payment_method VARCHAR(50),
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);
