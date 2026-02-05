-- Products and premiums
SELECT product_name, monthly_premium
FROM products;

-- Most expensive products
SELECT product_name, monthly_premium
FROM products
ORDER BY monthly_premium DESC;

-- Claims over a certain limit (£1,000)
SELECT claim_id, claim_amount 
FROM claims 
WHERE claim_amount > 1000;

-- Largest claims
SELECT claim_id, claim_amount
FROM claims
ORDER BY claim_amount DESC
LIMIT 20;

-- Pet Demographics (most common breeds)
SELECT 
    breed,
    COUNT(*) AS breed_count
FROM pets
GROUP BY breed
ORDER BY breed_count DESC
LIMIT 20;

-- Highest value customers (top 1%)
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(
        TIMESTAMPDIFF(MONTH, p.start_date, p.end_date) 
        * pr.monthly_premium
    ) AS total_revenue
FROM customers c
JOIN pets pe ON pe.customer_id = c.customer_id
JOIN policies p ON p.pet_id = pe.pet_id
JOIN products pr ON pr.product_id = p.product_id
GROUP BY c.customer_id
ORDER BY total_revenue DESC
LIMIT 600;  -- top 1% of 60,000 customers

-- Claim Severity Bands (low/medium/high)
SELECT 
    CASE 
        WHEN claim_amount < 200 THEN 'Low'
        WHEN claim_amount BETWEEN 200 AND 1000 THEN 'Medium'
        ELSE 'High'
    END AS severity_band,
    COUNT(*) AS claim_count
FROM claims
GROUP BY severity_band
ORDER BY claim_count DESC;

-- Average Time from Claim to Payment (operational efficiency)
SELECT 
    AVG(DATEDIFF(cp.payment_date, c.claim_date)) AS avg_days_to_payment
FROM claims c
JOIN claim_payments cp ON cp.claim_id = c.claim_id;

-- Claims Frequency by Policy (risk indicator)
SELECT 
    p.policy_id,
    COUNT(c.claim_id) AS claim_count
FROM policies p
LEFT JOIN claims c ON c.policy_id = p.policy_id
GROUP BY p.policy_id
ORDER BY claim_count DESC
LIMIT 20;

-- Customer Life Value
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(
        TIMESTAMPDIFF(MONTH, p.start_date, p.end_date) 
        * pr.monthly_premium
    ) AS lifetime_value
FROM customers c
JOIN pets pe ON pe.customer_id = c.customer_id
JOIN policies p ON p.pet_id = pe.pet_id
JOIN products pr ON pr.product_id = p.product_id
GROUP BY c.customer_id
ORDER BY lifetime_value DESC
LIMIT 20;
