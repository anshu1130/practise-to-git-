# Phishing Triage Runbook

**Owner:** SOC  
**Last Updated:** 2026-02-16  
**Severity Range:** Low → Critical  
**Applies To:** Email-based phishing, credential harvesting, malicious attachments, business email compromise (BEC)

---

## Goal
Quickly determine whether a reported email is malicious, contain user impact, and preserve evidence for follow-up actions.

## Inputs
- Reported message (original .eml if possible)
- User report context (what they clicked, what they entered, when)
- Mail platform logs (message trace / delivery events)
- URL(s), attachment(s), sender domain, reply-to domain

## Scope / Definition
Treat as **phishing** if any of the following are true:
- Unexpected request for credentials, MFA codes, or payment
- Links to login portals not owned by the expected service
- Attachment asks to enable macros or “secure content”
- Sender identity mismatch (display name vs actual domain)
- Message uses urgency, threats, or “action required” language

---

## Triage Checklist (5–10 minutes)

### 1) Confirm the report
- [ ] Identify reporting user and time of receipt
- [ ] Ask: did they click a link, open attachment, enter creds, or approve MFA?
- [ ] Collect the original message (forward-as-attachment or export .eml)

### 2) Quick header review
Look for:
- From / Reply-To mismatch
- SPF/DKIM/DMARC results (pass/fail)
- “Received:” chain anomalies (unexpected hops)
- Suspicious return-path domains

> **Note:** Header anomalies alone don’t prove malice, but they help prioritize.

### 3) Link & domain analysis (safe approach)
- [ ] Extract URL(s) (do **not** click directly)
- [ ] Check domain age / reputation (internal tooling or public reputation sources)
- [ ] Look for punycode / homographs / typosquatting (e.g., `micr0soft`)

### 4) Attachment analysis (safe approach)
- [ ] Identify file type and size
- [ ] If macro-enabled Office file: treat as suspicious by default
- [ ] If archive: inspect names (double extensions like `.pdf.exe`)
- [ ] If possible: run in sandbox / detonation (per policy)

### 5) Determine classification
Choose one:
- **Benign / Marketing / Internal legit**
- **Suspicious** (needs deeper analysis)
- **Confirmed Phish** (malicious)
- **Credential Harvesting**
- **Malware Delivery**
- **BEC / Fraud attempt**

---

## Containment Actions

### If user did NOT interact
- [ ] Quarantine message(s) (if supported)
- [ ] Add block for sender/domain/URL (per policy)
- [ ] Search org for recipients of the same message
- [ ] Notify impacted users with “do not interact” advisory

### If user clicked link but did NOT enter creds
- [ ] Force sign-out (if supported)
- [ ] Reset password if policy requires for click-only events
- [ ] Review sign-in logs for anomalies in the last 24–48 hours

### If user entered creds or approved MFA
- [ ] **Immediate** password reset + revoke sessions/tokens
- [ ] Enforce MFA re-registration (if applicable)
- [ ] Check mailbox rules/forwarding changes
- [ ] Monitor for new device sign-ins and suspicious app consent

---

## Evidence to Capture
- Original message (.eml) and full headers
- Extracted URLs, attachment hashes (SHA256 if possible)
- Message trace: delivery time, recipients, subject, sender
- User interaction statement (what/when)
- Any mailbox rule changes or suspicious sign-ins

---

## Escalation Criteria
Escalate to IR lead if:
- Multiple recipients (campaign)
- Any credential submission / MFA prompt approval
- VIP / finance / executive targets
- Attachment detonation indicates malware
- Signs of mailbox takeover (forwarding rules, OAuth consent, outbound spam)

---

## Close-Out Notes
Document:
- classification
- containment actions taken
- impacted users
- IOCs added/blocked
- follow-ups (monitoring window, additional hunts)

**Related Runbooks:**
- `runbooks/suspicious-login.md`
- `runbooks/endpoint-isolation.md`
