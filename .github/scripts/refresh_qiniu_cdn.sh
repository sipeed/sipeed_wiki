#!/bin/sh
# Refresh 七牛 (Qiniu) CDN cache for wiki.sipeed.com after a publish.
#
# WHY: the site is uploaded to 腾讯云 COS (the origin), but wiki.sipeed.com is
# served through 七牛 CDN (CNAME -> *.qiniudns.com). 七牛 caches with
# max-age=31536000 (one year), so overwriting a same-named file at the origin is
# invisible to users until the edge cache is busted. A publish that skips this
# step ships stale HTML/JSON to every already-warmed edge node.
#
# WHAT: submit a directory refresh for the site root; 七牛 drops the whole tree
# from the edge and re-pulls from the COS origin on the next request.
#
# Credentials come from the environment (set as GitHub Actions secrets), never
# printed:
#   QINIU_ACCESS_KEY  QINIU_SECRET_KEY
# Optional:
#   QINIU_REFRESH_DIRS  space-separated dir URLs (default: https://wiki.sipeed.com/)
#
# Best-effort: a directory refresh may need extra 七牛 permission and the daily
# dir-refresh quota is only 10, so a failure here MUST NOT fail the deploy — the
# COS upload already succeeded. We warn and exit 0.
set -eu

AK="${QINIU_ACCESS_KEY:-}"
SK="${QINIU_SECRET_KEY:-}"
DIRS="${QINIU_REFRESH_DIRS:-https://wiki.sipeed.com/}"

if [ -z "$AK" ] || [ -z "$SK" ]; then
  echo "WARN: QINIU_ACCESS_KEY / QINIU_SECRET_KEY not set — skipping CDN refresh."
  echo "      Add them under Settings > Secrets and variables > Actions (masked)."
  exit 0
fi

command -v curl    >/dev/null 2>&1 || { echo "WARN: curl not found — skipping CDN refresh.";    exit 0; }
command -v openssl >/dev/null 2>&1 || { echo "WARN: openssl not found — skipping CDN refresh."; exit 0; }

# Build the JSON {"dirs":["u1","u2",...]} body from the space-separated list.
json_dirs=""
for d in $DIRS; do
  [ -n "$d" ] || continue
  if [ -z "$json_dirs" ]; then json_dirs="\"$d\""; else json_dirs="$json_dirs,\"$d\""; fi
  echo "Refreshing CDN dir: $d"
done
BODY="{\"dirs\":[$json_dirs]}"

# 七牛 QBox management token. The signing string is "<path>\n" with the request
# body NOT included (body is only signed for x-www-form-urlencoded, not JSON).
# sign = base64urlsafe(HMAC-SHA1(secret, "<path>\n")).
PATH_REFRESH="/v2/tune/refresh"
SIGN=$(printf '%s\n' "$PATH_REFRESH" \
  | openssl dgst -sha1 -hmac "$SK" -binary \
  | openssl base64 -A | tr '+/' '-_')
TOKEN="QBox $AK:$SIGN"

RESP=$(curl -s -X POST "https://fusion.qiniuapi.com$PATH_REFRESH" \
  -H "Authorization: $TOKEN" \
  -H "Content-Type: application/json" \
  -d "$BODY" || true)
echo "refresh response: $RESP"

case "$RESP" in
  *'"code":200'*)
    echo "CDN dir refresh accepted."
    ;;
  *)
    echo "WARN: CDN dir refresh not confirmed (continuing). Dir refresh may need"
    echo "      extra 七牛 permission, or the daily dir-refresh quota (10/day) is spent."
    ;;
esac
exit 0
