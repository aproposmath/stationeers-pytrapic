#!/usr/bin/env bash
set -e
stationeers_mod_dir=${STATIONEERS_MOD_DIR:-~/.sa/Stationeers/BepInEx/plugins}

if [[ ! -f Main.csproj ]] ; then
  echo "You must execute $(basename "$0") from the project root" ; exit 1
fi

mod_dir="${stationeers_mod_dir}/pytrapic"

rm -rf bin/Debug

# ~/.local/share/nvim/mason/bin/csharpier format *.cs
# xmllint --format Main.csproj -o Main.csproj
# xmllint --format Main.props -o Main.props
dotnet build -c Debug Main.csproj

mkdir -p "${mod_dir}/"
cp bin/Debug/*/PyTrapIC.dll "${mod_dir}/"
cp -r About "${mod_dir}/"
echo "Installed PyTrapIc (Debug) into ${mod_dir}"