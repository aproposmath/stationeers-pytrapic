#!/usr/bin/env bash
set -e

if [[ ! -f Main.csproj ]]; then
  echo "Run from project root"; exit 1
fi

dist_dir="${DIST_DIR:-dist}"
dotnet clean Main.csproj
dotnet build -c Release Main.csproj  # PublishDist target handles dist/ population

(cd "${dist_dir}" && zip -r PyTrapIC.zip pytrapic && echo "Released to ${dist_dir}/pytrapic/")
