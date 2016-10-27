## What is this?
This simple python script lets you visually diff eagle CAD schematic and board files.

## Installation
 - Download eagle-diff.py somewhere on your path
 - Adjust eagle_path variable if it is different

## Prerequisites
 - [PIL](http://www.pythonware.com/products/pil/)

## Git Setup
### Add this to your .gitconfig:
```
[diff "eagle"]
  command = eagle-diff
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
