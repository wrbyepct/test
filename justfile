lint:
    ./run lint

main:
    poetry run python -m main

precommit-install:
    poetry run pre-commit uninstall; poetry run pre-commit clean; \
    poetry run pre-commit install

clean:
    ./run clean
build:
    ./run build

report:
    ./run test-report-html
