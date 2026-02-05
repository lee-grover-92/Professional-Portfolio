-- 1. Orphaned pets (no matching customer)
SELECT pet_id, customer_id
FROM pets
WHERE customer_id NOT IN (SELECT customer_id FROM customers);

-- 2. Orphaned policies (no matching pet or product)
SELECT policy_id, pet_id, product_id
FROM policies
WHERE pet_id NOT IN (SELECT pet_id FROM pets)
   OR product_id NOT IN (SELECT product_id FROM products);

-- 3. Orphaned claims (no matching policy)
SELECT claim_id, policy_id
FROM claims
WHERE policy_id NOT IN (SELECT policy_id FROM policies);

-- 4. Orphaned vet visits (no matching claim)
SELECT visit_id, claim_id
FROM vet_visits
WHERE claim_id NOT IN (SELECT claim_id FROM claims);

-- 5. Orphaned invoice line items (no matching visit)
SELECT line_item_id, visit_id
FROM invoice_line_items
WHERE visit_id NOT IN (SELECT visit_id FROM vet_visits);

-- 6. Orphaned claim payments (no matching claim)
SELECT payment_id, claim_id
FROM claim_payments
WHERE claim_id NOT IN (SELECT claim_id FROM claims);

-- 7. Null checks (example: pets without birthdate)
SELECT * FROM pets WHERE birthdate IS NULL;

-- 8. Duplicate microchip IDs
SELECT microchip_id, COUNT(*) as count
FROM pets
GROUP BY microchip_id
HAVING COUNT(*) > 1;

-- 9. Negative or zero claim amounts
SELECT * FROM claims WHERE claim_amount <= 0;

-- 10. Payments exceeding claim amount
SELECT cp.claim_id, c.claim_amount, SUM(cp.amount_paid) AS total_paid
FROM claim_payments cp
JOIN claims c ON cp.claim_id = c.claim_id
GROUP BY cp.claim_id, c.claim_amount
HAVING SUM(cp.amount_paid) > c.claim_amount;
