SHOW VARIABLES LIKE 'local_infile';

SET GLOBAL local_infile = 1;

-- Disable foreign key checks
SET FOREIGN_KEY_CHECKS = 0;

-- Load customers
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customers.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load pets
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/pets.csv'
INTO TABLE pets
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load products
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/products.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load policies
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/policies.csv'
INTO TABLE policies
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load claims
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/claims.csv'
INTO TABLE claims
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load vet visits
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/vet_visits.csv'
INTO TABLE vet_visits
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load invoice line items
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/invoice_line_items.csv'
INTO TABLE invoice_line_items
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Load claim payments
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/claim_payments.csv'
INTO TABLE claim_payments
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Show row counts
SELECT 'customers' AS table_name, COUNT(*) AS `rows` FROM customers
UNION ALL
SELECT 'pets', COUNT(*) FROM pets
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'policies', COUNT(*) FROM policies
UNION ALL
SELECT 'claims', COUNT(*) FROM claims
UNION ALL
SELECT 'vet_visits', COUNT(*) FROM vet_visits
UNION ALL
SELECT 'invoice_line_items', COUNT(*) FROM invoice_line_items
UNION ALL
SELECT 'claim_payments', COUNT(*) FROM claim_payments;