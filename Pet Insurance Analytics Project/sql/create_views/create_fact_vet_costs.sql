CREATE OR REPLACE VIEW fact_vet_costs AS
SELECT
    vv.visit_id,
    vv.visit_date,
    vv.vet_clinic,
    vv.visit_type,
    ili.treatment_code,
    ili.description,
    ili.cost,
    vv.claim_id,
    po.policy_id,
    p.pet_id,
    cu.customer_id
FROM invoice_line_items ili
JOIN vet_visits vv ON ili.visit_id = vv.visit_id
JOIN claims cl ON vv.claim_id = cl.claim_id
JOIN policies po ON cl.policy_id = po.policy_id
JOIN pets p ON po.pet_id = p.pet_id
JOIN customers cu ON p.customer_id = cu.customer_id;
