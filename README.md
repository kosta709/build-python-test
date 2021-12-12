# Python build executable tests

https://pyinstaller.readthedocs.io/en/stable/

## Prerequisite
```
virtualenv .pyenv
source .pyenv/bin/activate
pip install -r requirements.txt
```
## Build Manually
```
pyinstaller --onefile getos.py
```
the executable is created in `dist/getos`

## Build Github Actions
- [Virtual Environments](https://github.com/actions/virtual-environments)
- [Release Action](https://github.com/softprops/action-gh-release)


