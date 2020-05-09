MODULE := gigabloat
BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@poetry run python3 -m $(MODULE) scan tests/test_files

test:
	@poetry run pytest

lint:
	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@poetry run pylint --rcfile=setup.cfg **/*.py
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@poetry run flake8
	@echo "\n${BLUE}Running Bandit against source files...${NC}\n"
	@poetry run bandit -r --ini setup.cfg

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml reports

.PHONY: clean test