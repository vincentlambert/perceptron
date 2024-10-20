#
# gmake
#
SHELL := /bin/bash
CHDIR_SHELL := $(SHELL)

.ONESHELL: # Applies to every targets in the file!
.SHELLFLAGS += -e # stop at the first failure

PYTHON := python3.11

#
# Setup
#
init-venv:
	@echo "***** $@"
	${PYTHON} -m venv ./.venv

update-venv: init-venv
	@echo "***** $@"
	@source .venv/bin/activate
	cd src
	pip install --upgrade pip
	pip install -r requirements.txt

install-black: update-venv
	@echo "***** $@"
	@source .venv/bin/activate
	pip install black

install-pylint: update-venv
	@echo "***** $@"
	@source .venv/bin/activate
	pip install pylint

install-mypy: update-venv
	@echo "***** $@"
	@source .venv/bin/activate
	pip install mypy

init-project: update-venv install-black install-pylint install-mypy
