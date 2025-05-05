#!/bin/bash

# Create directory for reports
mkdir -p code_reports

echo "🔍 Running pylint (only fatal and error messages)..."
pylint . --disable=all --enable=F,E > code_reports/pylint_report.txt
echo "✔️  Pylint (F, E only) report saved to code_reports/pylint_report.txt"

echo "🔍 Running vulture (dead code)..."
vulture . > code_reports/vulture_report.txt
echo "✔️  Vulture report saved to code_reports/vulture_report.txt"

echo "🔍 Running flake8 (only syntax and undefined name errors)..."
flake8 . --select=E9,F82 > code_reports/flake8_report.txt
echo "✔️  Flake8 (E9, F82 only) report saved to code_reports/flake8_report.txt"

echo ""
echo "✅ Static analysis (focused) completed. Check the code_reports folder."
