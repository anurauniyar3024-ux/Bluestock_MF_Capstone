# Data Dictionary

## Dataset 1: NAV History

| Column    | Data Type | Description                         |
| --------- | --------- | ----------------------------------- |
| amfi_code | Integer   | Unique AMFI code of the mutual fund |
| date      | Date      | NAV date                            |
| nav       | Float     | Net Asset Value of the mutual fund  |

---

## Dataset 2: Investor Transactions

| Column             | Data Type | Description                  |
| ------------------ | --------- | ---------------------------- |
| investor_id        | String    | Unique investor ID           |
| transaction_date   | Date      | Date of transaction          |
| amfi_code          | Integer   | AMFI code of the mutual fund |
| transaction_type   | String    | SIP, Lumpsum or Redemption   |
| amount_inr         | Integer   | Transaction amount in INR    |
| state              | String    | Investor's state             |
| city               | String    | Investor's city              |
| city_tier          | String    | Tier of the city             |
| age_group          | String    | Investor age group           |
| gender             | String    | Investor gender              |
| annual_income_lakh | Float     | Annual income in lakhs       |
| payment_mode       | String    | Mode of payment              |
| kyc_status         | String    | KYC verification status      |
