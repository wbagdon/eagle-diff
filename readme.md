## What is this?
This simple python script lets you visually diff eagle CAD schematic and board files.

## Installation
 - Download eagle_diff.py somewhere on your path
 - Eagle 7.0.0 - 7.7.0 are auto-detected, using the latest available installed on system

## Prerequisites
 - [Pillow](https://pillow.readthedocs.io/en/3.4.x/index.html)
 - `pip install Pillow`

## Git Setup
### Add this to your .gitconfig:
```
[diff "eagle"]
	command = eagle_diff.py
```
### Add a .gitattributes file to your project with these lines:

```
*.sch diff=eagle
*.brd diff=eagle
```

## Try it out
### Clone this project then:
    git diff v1 v2 main.brd

## Example
### Schematic
![pew pew pew](https://github.com/wbagdon/eagle-diff/raw/master/sch_example.png "lasers pew pew")
### Board
![pew pew pew](https://github.com/wbagdon/eagle-diff/raw/master/brd_example.png "lasers pew pew")

## Contribute
Feel free to send pull requests with fixes/upgrades/whatever.
