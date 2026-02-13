#!/usr/bin/env bash
set -euo pipefail

WS="ws"
OUT="$WS/.venv"
URL="https://www.python.org/ftp/python/3.14.2/python-3.14.2-embed-amd64.zip"
SITE="$WS/.venv/Lib/site-packages"
WHEELHOUSE="wheelhouse"

rm -rf "$WS" "$WHEELHOUSE" dist/* ws.zip
mkdir -p "$OUT" "$SITE" "$WHEELHOUSE" "$WS/library"

touch "$WS/__init__.py" "$WS/library/__init__.py"

python -m build -wn .
WHL=`ls dist/*.whl`

echo "download"
curl -fsSL "$URL" -o python-embed.zip

echo "unzip"
unzip -q python-embed.zip -d "$OUT"
rm -f python-embed.zip

PTH="$(ls -1 "$OUT"/*._pth | head -n1)"
grep -qx './Lib/site-packages' "$PTH" || printf '%s\n' './Lib/site-packages' >>"$PTH"
sed -i 's/^[[:space:]]*#[[:space:]]*\(import[[:space:]]\+site[[:space:]]*\)$/\1/' "$PTH"
grep -q '^[[:space:]]*import[[:space:]]\+site[[:space:]]*$' "$PTH" || printf '%s\n' 'import site' >>"$PTH"

echo "download wheels"
python -m pip -q download --dest "$WHEELHOUSE" --only-binary=:all: \
  --platform win_amd64 --python-version 314 --implementation cp --abi cp314 \
  "$WHL" basedpyright

echo "unpack wheels"
# unpack everything
for whl in "$WHEELHOUSE"/*.whl; do
  unzip -q -o "$whl" -d "$SITE"
done

rm -rf typings
basedpyright --createstub stationeers_pytrapic
mv typings "$WS"
cp scripts/pyrightconfig.json ws/
zip -r ws.zip "$WS"
