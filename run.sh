#!/bin/bash

VENV_NAME=msi-env

python -m venv ${VENV_NAME}
source ${VENV_NAME}/bin/activate
pip install -r requirements-main.txt