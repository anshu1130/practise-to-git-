# Evidence Log Template

> **Purpose:** Track what was collected, from where, and how it is stored.  
> Use this for investigations that may require repeatability, compliance review, or legal hold.

---

## Case Info

- **Incident ID:** IR-YYYY-####  
- **Primary Responder:**  
- **Date Opened (UTC):**  
- **Evidence Storage Location:** (case folder path / vault / ticket link)  
- **Retention Policy:** (if applicable)

---

## Collection Notes
- Use UTC timestamps where possible.
- Record hashes for exported files when feasible.
- Avoid collecting unnecessary sensitive/personal data.
- If evidence is transferred, record the transfer in the chain-of-custody section.

---

## Evidence Items

| Item ID | Collected (UTC) | Collector | Source System | Description | File Name / Artifact | Hash (SHA256) | Storage Location |
|---|---|---|---|---|---|---|---|
| E-001 | YYYY-MM-DD HH:MM | Name | HOST-123 | EDR alert export | edr_alert.json | (optional) | case-folder/exports/ |
| E-002 | YYYY-MM-DD HH:MM | Name | user mailbox | Original phishing email (.eml) | report.eml | (optional) | case-folder/email/ |

---

## Chain of Custody (if needed)

| Transfer # | Date/Time (UTC) | From | To | Method | Notes |
|---|---|---|---|---|---|
| 1 | YYYY-MM-DD HH:MM | Responder A | Responder B | Secure share | Hand-off for after-hours coverage |

---

## Validation Checklist
- [ ] Evidence stored in approved location
- [ ] Access restricted to incident team
- [ ] Hashes recorded for critical artifacts (where feasible)
- [ ] Transfers documented (if applicable)
- [ ] Sensitive data handled per policy

---

## Additional Notes
Use this section for any context that doesn’t fit the tables above.
