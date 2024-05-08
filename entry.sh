#!/bin/bash

if command -v python3 &>/dev/null; then
    PYTHON_EXECUTABLE=python3
elif command -v python &>/dev/null; then
    PYTHON_EXECUTABLE=python
else
    echo "Python no esta instalado. Por favor, instale Python y vuelva a intentarlo."
    exit 1
fi

$PYTHON_EXECUTABLE -m pip install -r requirements.txt