-- 1. Total number of customers and pets
SELECT 
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT pet_id) AS total_pets
FROM pets;

-- 2. Average number of pets per customer
SELECT 
    ROUND(COUNT(*) / COUNT(DISTINCT customer_id), 2) AS avg_pets_per_customer
FROM pets;

-- 3. Top 10 breeds by total claim amount
SELECT p.breed, SUM(c.claim_amount) AS total_claimed
FROM pets p
JOIN policies po ON p.pet_id = po.pet_id
JOIN claims c ON po.policy_id = c.policy_id
GROUP BY p.breed
ORDER BY total_claimed DESC
LIMIT 10;

-- 4. Loss ratio by product
SELECT 
    pr.product_name,
    COUNT(DISTINCT po.policy_id) AS total_policies,
    SUM(pr.monthly_premium * TIMESTAMPDIFF(MONTH, po.start_date, IFNULL(po.end_date, CURDATE()))) AS total_premium,
    SUM(c.claim_amount) AS total_claims,
    ROUND(
        SUM(c.claim_amount) / NULLIF(SUM(pr.monthly_premium * TIMESTAMPDIFF(MONTH, po.start_date, IFNULL(po.end_date, CURDATE()))), 0),
        2
    ) AS loss_ratio
FROM products pr
JOIN policies po ON pr.product_id = po.product_id
LEFT JOIN claims c ON po.policy_id = c.policy_id
GROUP BY pr.product_name;


-- 5. Claim approval rate by diagnosis
SELECT 
    diagnosis,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN status = 'Approved' THEN 1 ELSE 0 END) AS approved,
    ROUND(SUM(CASE WHEN status = 'Approved' THEN 1 ELSE 0 END) / COUNT(*), 2) AS approval_rate
FROM claims
GROUP BY diagnosis
ORDER BY total_claims DESC;

-- 6. Average claim amount by species
SELECT p.species, ROUND(AVG(c.claim_amount), 2) AS avg_claim_amount
FROM pets p
JOIN policies po ON p.pet_id = po.pet_id
JOIN claims c ON po.policy_id = c.policy_id
GROUP BY p.species;

-- 7. Most expensive vet clinics (by average visit cost)
SELECT 
    vv.vet_clinic,
    ROUND(AVG(ili.cost), 2) AS avg_treatment_cost,
    COUNT(DISTINCT vv.visit_id) AS total_visits
FROM vet_visits vv
JOIN invoice_line_items ili ON vv.visit_id = ili.visit_id
GROUP BY vv.vet_clinic
ORDER BY avg_treatment_cost DESC
LIMIT 10;

-- 8. Customer lifetime value (CLV) estimate
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(DISTINCT p.pet_id) AS pets_owned,
    COUNT(DISTINCT po.policy_id) AS policies,
    ROUND(SUM(pr.monthly_premium * TIMESTAMPDIFF(MONTH, po.start_date, IFNULL(po.end_date, CURDATE()))), 2) AS total_premiums
FROM customers c
JOIN pets p ON c.customer_id = p.customer_id
JOIN policies po ON p.pet_id = po.pet_id
JOIN products pr ON po.product_id = pr.product_id
GROUP BY c.customer_id, customer_name
ORDER BY total_premiums DESC
LIMIT 20;