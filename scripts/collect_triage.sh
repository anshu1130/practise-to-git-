#!/usr/bin/env bash
# collect_triage.sh
#
# Lightweight endpoint triage collection helper.
# Intended for IR/SOC use to gather baseline artifacts quickly.
#
# NOTE: This is a training repo. Output is best-effort and non-destructive.
# It may not work on all systems or containers.

set -euo pipefail

OUT_DIR="${1:-./triage_out}"
CASE_ID="${CASE_ID:-IR-TRAINING}"
HOST_TAG="${HOST_TAG:-$(hostname 2>/dev/null || echo unknown-host)}"
TS="$(date -u +"%Y%m%dT%H%M%SZ" 2>/dev/null || echo unknown-time)"

mkdir -p "${OUT_DIR}"
RUN_DIR="${OUT_DIR}/${CASE_ID}_${HOST_TAG}_${TS}"
mkdir -p "${RUN_DIR}"

log()  { echo "[collect_triage] $*"; }
save() { cat > "${RUN_DIR}/$1"; }

log "Starting triage collection"
log "Case: ${CASE_ID}"
log "Output: ${RUN_DIR}"
echo "${CASE_ID}" > "${RUN_DIR}/case_id.txt"
echo "${TS}"      > "${RUN_DIR}/collection_time_utc.txt"
echo "${HOST_TAG}" > "${RUN_DIR}/hostname.txt"

# --- System info ---
log "Collecting system info"
{
  echo "time_utc: ${TS}"
  echo "hostname: ${HOST_TAG}"
  echo -n "user: " && (id -un 2>/dev/null || echo "unknown")
  echo -n "uid_gid: " && (id 2>/dev/null || true)
  echo -n "kernel: " && (uname -a 2>/dev/null || echo "unknown")
  echo -n "uptime: " && (uptime 2>/dev/null || true)
} > "${RUN_DIR}/system_info.txt"

# --- Processes ---
log "Collecting process list"
( ps auxww 2>/dev/null || ps -ef 2>/dev/null || echo "ps unavailable" ) > "${RUN_DIR}/processes.txt" || true

# --- Network connections ---
log "Collecting network connections"
{
  echo "### ss -tulpn"
  ss -tulpn 2>/dev/null || true
  echo
  echo "### ss -tpn"
  ss -tpn 2>/dev/null || true
  echo
  echo "### netstat -anp (fallback)"
  netstat -anp 2>/dev/null || true
} > "${RUN_DIR}/network.txt" || true

# --- DNS / resolver info ---
log "Collecting resolver config"
{
  echo "### /etc/resolv.conf"
  cat /etc/resolv.conf 2>/dev/null || true
  echo
  echo "### /etc/hosts"
  cat /etc/hosts 2>/dev/null || true
} > "${RUN_DIR}/resolver.txt" || true

# --- Recent auth/log hints (best effort) ---
log "Collecting auth/log hints (best effort)"
{
  echo "### last (may be empty in containers)"
  last -Faiw 2>/dev/null | head -n 50 || true
  echo
  echo "### who"
  who 2>/dev/null || true
  echo
  echo "### env (redacted keys)"
  env | sed -E 's/(TOKEN|SECRET|PASSWORD|KEY)=.*/\1=[REDACTED]/I' | sort
} > "${RUN_DIR}/auth_hints.txt" || true

# --- Optional: parse IOCs if present ---
IOC_FILE="./data/sample_iocs.csv"
if [[ -f "${IOC_FILE}" ]]; then
  log "Found ${IOC_FILE}; generating quick IOC summary"
  if command -v python3 >/dev/null 2>&1; then
    python3 ./scripts/parse_iocs.py --input "${IOC_FILE}" --summary > "${RUN_DIR}/ioc_summary.txt" 2>/dev/null || true
  else
    echo "python3 not available; skipping IOC summary" > "${RUN_DIR}/ioc_summary.txt"
  fi
fi

# --- Write a simple manifest ---
log "Writing manifest"
{
  echo "case_id=${CASE_ID}"
  echo "host=${HOST_TAG}"
  echo "collection_time_utc=${TS}"
  echo "files:"
  (cd "${RUN_DIR}" && ls -1) | sed 's/^/  - /'
} > "${RUN_DIR}/manifest.txt"

log "Done."
log "Tip: attach ${RUN_DIR} to the case folder and update templates/evidence-log.md"
