# Incident Report Template

> **Use this template for all confirmed incidents.**  
> If this is a suspected incident still under investigation, mark status as **Investigating** and update as you learn more.

---

## Header

- **Incident ID:** IR-YYYY-####  
- **Status:** Investigating / Contained / Eradicated / Recovered / Closed  
- **Severity:** Low / Medium / High / Critical  
- **Incident Type:** Phishing / Malware / Account Compromise / Data Exfil / Insider / Other  
- **Reported By:** (name/team/system)  
- **Assigned To:** (primary responder)  
- **Start Time (UTC):**  
- **Detection Time (UTC):**  
- **Containment Time (UTC):**  
- **Close Time (UTC):**  
- **Impacted Systems:** (hosts, accounts, apps)  
- **Impacted Users:** (count + key roles)  
- **Customer Impact:** None / Suspected / Confirmed (details)

---

## Executive Summary (5–7 sentences)
Describe what happened, how it was detected, impact, and current status. Keep this readable for non-technical stakeholders.

---

## Scope & Impact
- **Affected Assets:** (hosts, accounts, services, mailboxes, endpoints)
- **Data Exposure:** None / Suspected / Confirmed  
  - If confirmed, describe *what* data and *how* determined.
- **Operational Impact:** (downtime, access loss, productivity, degraded services)
- **Business Impact:** (financial, regulatory, reputational)

---

## Timeline (UTC)
> Add entries in chronological order. Use UTC for consistency.

| Time (UTC) | Event |
|---|---|
| YYYY-MM-DD HH:MM | Alert triggered / user reported email |
| YYYY-MM-DD HH:MM | Initial triage completed |
| YYYY-MM-DD HH:MM | Containment action taken |
| YYYY-MM-DD HH:MM | IOC hunt performed |
| YYYY-MM-DD HH:MM | Recovery steps completed |

---

## Detection & Investigation

### Detection Source
- Alert name / rule / system:
- Why it fired:
- Confidence level:
- Any false positive history:

### What We Observed
- Key logs reviewed:
- Key findings:
- Suspicious behaviors:
- Related events/cases:

### Root Cause (if known)
- Initial access vector:
- Vulnerability / misconfiguration:
- User action involved (if applicable):
- Why controls did/didn’t stop it:

---

## Indicators of Compromise (IOCs)
> Include only validated IOCs. Add context where possible.

### Domains / URLs
- `example.com` (source: ..., confidence: ...)

### IP Addresses
- `203.0.113.10` (source: ..., confidence: ...)

### File Hashes
- SHA256: `...` (file name: ..., source: ...)

### Process / Artifact Names
- `evil.exe` (path: ..., host: ...)

---

## Containment Actions
List what you did to stop the incident from expanding.

- [ ] Accounts disabled / sessions revoked
- [ ] Endpoint isolated
- [ ] Malicious email quarantined
- [ ] Firewall blocks applied
- [ ] OAuth consents revoked
- [ ] Other:

**Details:**
- What:
- Where:
- When (UTC):
- Who approved (if required):

---

## Eradication Actions
List how the threat was removed.

- [ ] Persistence removed
- [ ] Malware quarantined/deleted
- [ ] Patches applied
- [ ] Credentials rotated
- [ ] System reimaged
- [ ] Other:

**Details:**
- What:
- Where:
- When (UTC):

---

## Recovery Actions
List steps to restore normal operations and validate integrity.

- [ ] System restored to known-good state
- [ ] Services validated
- [ ] Monitoring increased (window: ___)
- [ ] User notified / training provided
- [ ] Other:

**Details:**
- What:
- Where:
- When (UTC):

---

## Lessons Learned

### What Went Well
- 

### What Needs Improvement
- 

### Preventative Actions / Follow-Ups
| Action | Owner | Due Date | Status |
|---|---|---|---|
| Example: Enforce phishing-resistant MFA for admins | IAM | YYYY-MM-DD | Open |

---

## References / Evidence
- Case folder link:
- Evidence log:
- Ticket(s):
- Related alerts:
- Screenshots or exports location:

---

## Approval & Closure
- **Reviewed By:**  
- **Closure Notes:**  
- **Final Severity:**  
- **Date Closed (UTC):**
