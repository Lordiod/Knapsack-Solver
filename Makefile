# Makefile for Knapsack Problem Solver
# Common development tasks

.PHONY: help install install-dev test lint format clean run build dist upload

# Default target
help:
	@echo "Available commands:"
	@echo "  install     - Install production dependencies"
	@echo "  install-dev - Install development dependencies"
	@echo "  test        - Run tests"
	@echo "  lint        - Run linting tools"
	@echo "  format      - Format code with black and isort"
	@echo "  clean       - Clean build artifacts"
	@echo "  run         - Run the application"
	@echo "  build       - Build distribution packages"
	@echo "  dist        - Create distribution files"
	@echo "  upload      - Upload to PyPI (test)"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

# Development
test:
	python test_modules.py
	@echo "Running import tests..."
	python -c "from models import KnapsackSolver; print('✅ Models OK')"
	python -c "from utils import InputValidator; print('✅ Utils OK')"
	python -c "from gui import KnapsackGUI; print('✅ GUI OK')"

lint:
	@echo "Running flake8..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@echo "Running mypy..."
	mypy . --ignore-missing-imports

format:
	@echo "Formatting with black..."
	black .
	@echo "Sorting imports with isort..."
	isort .

# Running
run:
	python main.py

# Building and distribution
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

dist: build
	@echo "Distribution files created in dist/"

upload-test: dist
	@echo "Uploading to Test PyPI..."
	python -m twine upload --repository testpypi dist/*

upload: dist
	@echo "Uploading to PyPI..."
	python -m twine upload dist/*

# Windows-specific commands (if needed)
clean-windows:
	if exist build rmdir /s /q build
	if exist dist rmdir /s /q dist
	if exist *.egg-info rmdir /s /q *.egg-info
	for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	del /s /q *.pyc 2>nul
