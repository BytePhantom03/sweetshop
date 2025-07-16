@echo off
echo Running tests and saving report...
pytest tests/ --tb=short > test_report.txt
echo Test report saved to test_report.txt
pause