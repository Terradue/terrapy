#!/bin/sh

mkdir -p .venv/bin
curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh > .venv/bin/openapi-generator-cli
chmod u+x .venv/bin/openapi-generator-cli
export PATH=$PATH:.venv/bin