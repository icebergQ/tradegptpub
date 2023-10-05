# tradegptpub
public library for TradeGPT project


## Scaffold

1. Create a Python Virtual Envrionment `virtualenv ~/.venv` or `python3 -m venv ~/.venv`
    To activate this venv run `source ~/.venv/bin/activate`
2. Create empty files `Makefile`, `requirements.txt`, `main.py`, `Dockerfile`, `tradegtp\__init__.py`
3. Populate `Makefile`
4. Setup Continuous Integration, i.e. check code for issues like lint errors'
5. Build cli using Python Fire library `./cli_fire.py --help`