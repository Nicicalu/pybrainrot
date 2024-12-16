# Pybrainrot
Python with rizz. Be a sigma and mog your skibidi toilet opps before they crashout. This language can only be used in Ohio.

Pybrainrot is a Python preprosessor which translates regular Python code into brainrot by replacing certain keywords, operators, and built in functions with iPad kid vocabulary.

Implementation based on [Bython](https://github.com/mathialo/bython).

## Content of README:
- [Pybrainrot](#pybrainrot)
  - [Content of README:](#content-of-readme)
  - [Key features](#key-features)
  - [Code example](#code-example)
  - [Installation](#installation)
  - [Keyword mappings](#keyword-mappings)
  - [Quick intro](#quick-intro)


## Key features

 * Write Python using brainrot terms instead.

 * Run PyBrainrot files using the `pybrainrot` command, just like Python.

 * Translate Python files to pybrainrot and vice versa.

 * Real Python keywords that have defined pybrainrot mappings will not be allowed.

## Code example
![Code Example](https://github.com/shamith09/vscode-pybrainrot/blob/main/code-example.png?raw=true)

## Installation

If you for some reason want to install it from the git repository you can use `git clone` and do a local install instead:

```
$ git clone https://github.com/nicicalu/pybrainrot.git
$ cd pybrainrot
$ pip3 install .
```

The git version is sometimes a tiny bit ahead of the PyPI version, but not significantly.

To uninstall, simply run 

```
$ pip3 uninstall pybrainrot
```

which will undo all the changes.

To install the `vscode-pybrainrot` extension for Visual Studio Code, visit:

[https://marketplace.visualstudio.com/items?itemName=shamith-pasula.vscode-pybrainrot](https://marketplace.visualstudio.com/items?itemName=shamith-pasula.vscode-pybrainrot)

## Keyword mappings

Below is a table of all of the Python keywords or operators that should be replaced by their corresponding pybrainrot keyword. Python keywords that don't have a mapping or aren't in this table can just be used as is. If you want to request that a new mapping be made, please submit a pull request.

| Python Keyword/Operator | pybrainrot Translation                 |
| ----------------------- | -------------------------------------- |
| try/except/finally      | hawk/tuah/spit on that thang           |
| return                  | its giving                             |
| -                       | fanum tax                              |
| +                       | rizz                                   |
| print                   | yap                                    |
| True                    | Aura                                   |
| False                   | Cooked                                 |
| def                     | bop                                    |
| while                   | let him cook                           |
| import                  | glaze                                  |
| from                    | lock in                                |
| class                   | skibidi                                |
| if/elif/else            | chat is this real/yo chat/only in ohio |
| for                     | mewing                                 |
| break                   | just put the fries in the bag bro      |
| continue                | edge                                   |
| assert                  | sus                                    |
| raise                   | crashout                               |
| in                      | diddy                                  |
| is                      |                                        |
| and                     |                                        |
| or                      |                                        |
| not                     |                                        |
| with                    | pookie                                 |
| as                      | ahh                                    |
| global                  | GOAT                                   |
| nonlocal                | motion                                 |
| del                     | delulu                                 |
| yield                   | pause                                  |
| yield from              | pause no diddy                         |
| None                    | NPC                                    |
| pass                    | pluh                                   |
| self                    | unc                                    |
| range                   | huzz                                   |
| >                       | sigma                                  |
| <                       | beta                                   |
| ≥                       | sigma twin                             |
| ≤                       | beta twin                              |
| ==                      | twin                                   |
| =                       |                                        |
| async                   |                                        |
| await                   |                                        |
| open                    | mog                                    |
| read                    |                                        |
| write                   |                                        |
| close                   | demure                                 |
| list                    |                                        |
| set                     |                                        |
| dict                    |                                        |

## Quick intro

pybrainrot works by first translating pybrainrot files (suggested file ending: .brainrot) into Python-files, and then using Python to run them. You therefore need a working installation of Python for pybrainrot to work.


To run a pybrainrot program, simply type

```
$ pybrainrot source.brainrot arg1 arg2 ...
```

to run `source.brainrot` with arg1, arg2, ... as command line arguments. If you want more details on how to run pybrainrot files (flags, etc), type

```
$ pybrainrot -h
```

to print the built-in help page. You can also consult the man page by typing

```
$ man pybrainrot
```

pybrainrot also includes a translator from Python to pybrainrot. This is found via the `py2brainrot` command:

```
$ py2brainrot test.py
```

This will create a pybrainrot file called `test.brainrot`. A full explanation of `py2brainrot`, is found by typing

```
$ py2brainrot -h
```

or by consulting the man page:

```
$ man py2brainrot
```