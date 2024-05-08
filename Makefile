.PHONY: all check-python install run

check-python:
	@if command -v python3 &>/dev/null; then \
	    echo "Python 3 está instalado"; \
	    PYTHON_EXECUTABLE=python3; \
	elif command -v python &>/dev/null; then \
	    echo "Python está instalado"; \
	    PYTHON_EXECUTABLE=python; \
	else \
	    echo "Python no está instalado. Por favor, instale Python y vuelva a intentarlo."; \
	    exit 1; \
	fi

install: check-python
	@if command -v python3 &>/dev/null; then \
	    python3 -m pip install -r requirements.txt; \
	elif command -v python &>/dev/null; then \
	    python -m pip install -r requirements.txt; \
	fi

run: check-python
	@if command -v python3 &>/dev/null; then \
	    python3 main.py; \
	elif command -v python &>/dev/null; then \
	    python main.py; \
	fi

all: install run