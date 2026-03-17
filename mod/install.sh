#!/usr/bin/env bash
set -e

exec_dir=$(dirname "$0")

# Might want to put the mod into the steam-visible mods dir.
mod_dir=${STATIONEERS_MOD_DIR:-~/.sa/Stationeers/BepInEx/plugins/}

if [[ ! -f "${exec_dir}/release.sh" ]] ; then
  echo "You must execute $(basename "$0") from the project root" ; exit 1
fi

# build the release version into a dist dir
DIST_DIR="$(pwd)/dist"
export DIST_DIR;
"${exec_dir}/release.sh"

(cd "${mod_dir}" && rm -rf pytrapic && unzip "${DIST_DIR}"/*.zip)
echo "PyTrapIc (Release) installed into ${mod_dir}"