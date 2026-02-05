CREATE OR REPLACE VIEW fact_claims_summary AS
SELECT
    c.claim_id,
    c.claim_date,
    c.claim_amount,
    c.status,
    c.diagnosis,
    po.policy_id,
    pr.product_name,
    pr.coverage_type,
    pr.monthly_premium,
    p.pet_id,
    p.species,
    p.breed,
    TIMESTAMPDIFF(YEAR, p.birthdate, c.claim_date) AS age_at_claim,
    cu.customer_id,
    CONCAT(cu.first_name, ' ', cu.last_name) AS customer_name,
    cu.city AS customer_city,
    cu.country AS customer_country
FROM claims c
JOIN policies po ON c.policy_id = po.policy_id
JOIN products pr ON po.product_id = pr.product_id
JOIN pets p ON po.pet_id = p.pet_id
JOIN customers cu ON p.customer_id = cu.customer_id;
