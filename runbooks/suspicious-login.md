# Suspicious Login Triage Runbook

**Owner:** SOC  
**Last Updated:** 2026-02-16  
**Severity Range:** Medium → Critical  
**Applies To:** IdP anomalies, impossible travel, MFA fatigue, new device sign-in, token theft indicators

---

## Goal
Determine whether an account is compromised, contain access quickly, and prevent persistence.

## Inputs
- Alert details (user, timestamp, source IP, geo, device, app)
- Identity provider logs (SSO / OAuth / MFA events)
- Endpoint / EDR context (if user device is known)
- VPN logs (if applicable)

---

## Quick Decision Tree (2 minutes)
1) Is the login clearly expected (user traveling, known device)?  
→ If yes, document and close as false positive.

2) Is there evidence of password guessing / MFA push spam / new device + unusual geo?  
→ If yes, treat as potential compromise.

3) Did the user approve MFA unexpectedly?  
→ If yes, treat as likely compromise.

---

## Triage Checklist (10 minutes)

### 1) Validate with the user (if permitted)
Ask:
- Are you currently trying to sign in?
- Are you traveling or using a VPN?
- Did you receive unexpected MFA prompts?
- Did you approve any prompt you didn’t initiate?

### 2) Review sign-in context
Look for:
- New country/region
- New device or user-agent
- New application consent
- Multiple failed attempts preceding success
- “Impossible travel” patterns (two distant geos within short time)

### 3) Check for persistence
Common persistence indicators:
- Newly created mailbox rules / forwarding
- Added OAuth app consent / suspicious third-party app
- New MFA method added (phone number, authenticator)
- New admin role assignment / group membership changes

### 4) Scope related activity
- Recent successful logins (24–72 hours)
- Sensitive app access (mail, drive, admin portals)
- Downloads / exports / mass mailbox access
- Outbound email spikes (potential phishing from compromised account)

---

## Containment Actions (choose based on severity)

### Suspicious but unconfirmed
- [ ] Force password reset at next login (or immediate reset)
- [ ] Require MFA challenge
- [ ] Notify user to report any unexpected prompts
- [ ] Add monitoring for account over next 24 hours

### Likely compromise
- [ ] **Reset password immediately**
- [ ] **Revoke active sessions / refresh tokens**
- [ ] **Disable account temporarily** if active attacker suspected
- [ ] Remove unauthorized MFA methods
- [ ] Review and remove mailbox rules/forwarding
- [ ] Remove suspicious OAuth app consents
- [ ] Block source IP / geo (if policy allows)

### Confirmed compromise / high impact
- [ ] Engage IR lead
- [ ] Snapshot logs (IdP + mail + EDR + VPN)
- [ ] Search for lateral movement (shared credentials, reused passwords)
- [ ] Identify and notify additional impacted users

---

## Evidence to Capture
- Sign-in event details (IP, geo, user-agent, device ID)
- MFA events (prompts, approvals, method changes)
- Admin/audit logs for changes (rules, forwarding, consent, groups)
- Timeline of events (failures → success → actions)
- Any suspicious emails sent or files accessed

---

## Recommended Follow-Ups
- Enforce phishing-resistant MFA for high-risk roles (if supported)
- User education: MFA fatigue awareness
- Add conditional access policies (geo restrictions, device compliance)
- Review password reuse exposure and credential hygiene

**Related Runbooks:**
- `runbooks/phishing-triage.md`
- `runbooks/endpoint-isolation.md`
