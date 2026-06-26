-- 1. Display all records from Fund table
SELECT * FROM dim_fund;

-- 2. Display all NAV records
SELECT * FROM fact_nav;

-- 3. Display all investor transactions
SELECT * FROM fact_transactions;

-- 4. Count total transactions
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- 5. Calculate average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 6. Find maximum NAV
SELECT MAX(nav) AS highest_nav
FROM fact_nav;

-- 7. Find minimum NAV
SELECT MIN(nav) AS lowest_nav
FROM fact_nav;

-- 8. Count transactions by type
SELECT transaction_type, COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Count investors by KYC status
SELECT kyc_status, COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Top 10 highest transaction amounts
SELECT investor_id, amount_inr
FROM fact_transactions
ORDER BY amount_inr DESC
LIMIT 10;