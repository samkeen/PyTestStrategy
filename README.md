# Simple Python testing example : PyTestStrategy

## Summary
Python testing with min/current dependency version checks.
 
## Setup

### System setup
(suggested OSX, you can accomplish this is many different ways)
1. Replace `system` python with brew (get a modern python 3 in place)
2. To support pyenv (it builds python from source) ensure you have
   `brew install openssl readline sqlite3 xz zlib`
3. `brew install pyenv`

### Project setup

Set up a virtual env with python 3.7.x
If you use `pyenv`, ensure you have a 3.7.x available and activate it
```
$ pyenv versions
  system
  2.7.8
  3.6.7
  3.6.8
  3.7.1
  3.7.1/envs/tmp-project3.7
* 3.7.4 (set by /Users/samkeen/.pyenv/version)
```
Then run: 
```
$ python -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
$ tox
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