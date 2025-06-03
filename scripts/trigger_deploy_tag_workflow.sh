#!/bin/bash
TAG=$1

gh api \
    -X POST \
    -H 'Content-Type: application/json' \
    https://api.github.com/repos/eddcorts/curso_devops_receitas/dispatches \
    -f "event_type=manual_deploy" \
    -F "client_payload[tag]=$TAG"
