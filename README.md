# Simple Python testing example : PyTestStrategy

## Summary
Utilizing `pyenv` and `tox` to set up multi python version testing with min/current 
dependency version checks.
 
## Setup

### System setup
(suggested OSX, you can accomplish this is many different ways)
1. Replace `system` python with brew (get a modern python 3 in place)
2. to support pyenv (it build python from source) ensure you have
   `brew install openssl readline sqlite3 xz zlib`
3. `brew install pyenv`

### Project setup
```bash
$ mkdir python-testing-setup && cd python-testing-setup
$ pyenv versions
  system
  2.7.8
* 3.6.7 (set by /Users/samkeen/.pyenv/version)
  3.6.8
  3.7.1

# create the virtual environment
$ pyenv virtualenv 3.7.1 python-testing-setup
# make python-testing-setup(3.7.1) and 2.7.8 available 
$ pyenv local python-testing-setup 2.7.8
$ pyenv versions
  system
* 2.7.8
  3.6.7
  3.6.8
  3.7.1
  3.7.1/envs/python-testing-setup 
* python-testing-setup (set by /Users/samkeen/python-testing-setup/.python-version)
```

## TODO

- determine best `setup.py`
- utilize hooks to output debug info
```
tox
  ...
runing test env py3 with python version 3.7.1
dependency vertions
Requests: 2.1.4
  ...

```