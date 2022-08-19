#!/bin/bash
set -o nounset -o pipefail -o errexit

# Load all variables from .env and export them all for Ansible to read
set -o allexport
source "$(dirname "$0")/.env"
set +o allexport

# Run Ansible
exec ansible-playbook playbook-install.yml  --extra-vars "ansible_become_pass=1234" --extra-vars "ansible_become_user=snahashispappu"