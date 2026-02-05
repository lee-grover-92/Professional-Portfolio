CREATE OR REPLACE VIEW dim_customers AS
SELECT
    cu.customer_id,
    CONCAT(cu.first_name, ' ', cu.last_name) AS full_name,
    cu.city,
    cu.country,
    COUNT(DISTINCT p.pet_id) AS pets_owned,
    COUNT(DISTINCT po.policy_id) AS policies_owned,
    COUNT(DISTINCT cl.claim_id) AS total_claims,
    ROUND(SUM(cl.claim_amount), 2) AS total_claim_amount,
    ROUND(SUM(pr.monthly_premium * TIMESTAMPDIFF(MONTH, po.start_date, IFNULL(po.end_date, CURDATE()))), 2) AS total_premiums_paid
FROM customers cu
LEFT JOIN pets p ON cu.customer_id = p.customer_id
LEFT JOIN policies po ON p.pet_id = po.pet_id
LEFT JOIN products pr ON po.product_id = pr.product_id
LEFT JOIN claims cl ON po.policy_id = cl.policy_id
GROUP BY cu.customer_id, full_name, cu.city, cu.country;