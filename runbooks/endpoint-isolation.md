# Endpoint Isolation Runbook

**Owner:** IR Team  
**Last Updated:** 2026-02-16  
**Severity Range:** Medium → Critical  
**Applies To:** suspected malware, suspicious EDR detections, active C2, data exfil concerns

---

## Goal
Isolate a potentially compromised endpoint to stop spread/exfiltration while preserving evidence for investigation.

## Safety Notes
- Do not power off the device unless instructed by IR lead.
- Preserve volatile data when feasible (processes, network connections).
- Follow your organization’s evidence handling and privacy policies.

---

## When to Isolate
Isolate the endpoint if any of the following are present:
- Confirmed malware execution or ransomware indicators
- Active command-and-control (C2) traffic
- Credential dumping indicators
- Unapproved remote access tooling
- Evidence of lateral movement attempts
- High-confidence EDR detection

If unsure, consult IR lead or on-call escalation.

---

## Immediate Actions (First 5 minutes)

### 1) Identify the asset
- [ ] Hostname and user
- [ ] IP address and network segment
- [ ] Operating system and criticality (VIP, server, production workstation)
- [ ] Current location (office/remote)

### 2) Isolate using EDR (preferred)
- [ ] Use “Network Isolation” / “Contain Host” in EDR console
- [ ] Confirm isolation status
- [ ] Notify user (if required) and instruct them not to reboot or shut down

### 3) If EDR isolation is unavailable
Use the least destructive option:
- Remove from network (disable NIC / disconnect Wi-Fi)
- Move to quarantine VLAN (if supported)
- Block host at switch/firewall (if policy allows)

---

## Evidence Collection (Baseline)
Collect *at minimum*:
- [ ] System time and timezone
- [ ] Running processes and parent-child relationships
- [ ] Active network connections + listening ports
- [ ] Logged-in users and sessions
- [ ] Recent scheduled tasks / autoruns (where possible)
- [ ] Relevant logs (security logs, EDR alert details)

> Tip: If your org uses a triage script, run it now and store output with a timestamp.

---

## Investigation Checklist
- [ ] Identify initial infection vector (email, drive-by, USB, RDP, supply chain)
- [ ] Look for persistence (autoruns, services, scheduled tasks)
- [ ] Check for credential access (LSASS access, browser credential stores)
- [ ] Determine blast radius (other hosts contacted, shared accounts)
- [ ] Extract IOCs for hunting (domains, IPs, file hashes, process names)

---

## Remediation (After Approval)
Only proceed after IR lead approval:
- Remove persistence mechanisms
- Quarantine/delete malicious files
- Patch exploited vulnerability
- Reimage device if integrity cannot be trusted
- Rotate credentials used on the device (user + privileged)

---

## Recovery
- [ ] Restore from known-good state
- [ ] Validate EDR health and policy enforcement
- [ ] Monitor for recurrence (24–72 hours)
- [ ] Document lessons learned and update runbooks/templates

---

## Evidence Handling Notes
- Store evidence in approved location (case folder)
- Record hashes for exported artifacts (when feasible)
- Maintain an evidence log and chain of custody

**Related Runbooks / Templates:**
- `templates/evidence-log.md`
- `templates/incident-report.md`
- `runbooks/suspicious-login.md`
