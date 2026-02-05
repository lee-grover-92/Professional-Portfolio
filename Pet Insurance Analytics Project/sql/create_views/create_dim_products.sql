CREATE OR REPLACE VIEW dim_products AS
SELECT
    pr.product_id,
    pr.product_name,
    pr.coverage_type,
    pr.monthly_premium,
    pr.annual_limit,
    pr.deductible,
    COUNT(DISTINCT po.policy_id) AS total_policies,
    COUNT(DISTINCT cl.claim_id) AS total_claims,
    ROUND(SUM(cl.claim_amount), 2) AS total_claim_amount,
    ROUND(SUM(pr.monthly_premium * TIMESTAMPDIFF(MONTH, po.start_date, IFNULL(po.end_date, CURDATE()))), 2) AS total_premium_collected,
    ROUND(
        SUM(cl.claim_amount) / NULLIF(SUM(pr.monthly_premium * TIMESTAMPDIFF(MONTH, po.start_date, IFNULL(po.end_date, CURDATE()))), 0),
        2
    ) AS loss_ratio
FROM products pr
LEFT JOIN policies po ON pr.product_id = po.product_id
LEFT JOIN claims cl ON po.policy_id = cl.policy_id
GROUP BY pr.product_id, pr.product_name, pr.coverage_type, pr.monthly_premium, pr.annual_limit, pr.deductible;
