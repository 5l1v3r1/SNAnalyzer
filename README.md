# SNAnalyzer
Social Network Analyzer/ Grapher Library for Python 3

!!! SNAnalyzer is demo yet, some features may not work as expected.

## Installing dependencies

SNAnalyzer library uses Graphviz library and binaries for rendering relation graphics. For Ubuntu:
```
sudo apt-get install graphviz
sudo pip3 install graphviz
```
## Input File Syntax

Input file syntax is very easy, just write friends of each person like this:

```
Person One:Friend of Person One,Another Friend of Person One ,...
Person Two:Friend of Person Two
...
```
- Person names can contains UTF-8 characters and space.
- **":"** and **","** characters must be written contiguous.

## Changelog:
#### ** 01-18-2016 **
✔ Gives Dot Code

✔ Graphing relations in different format (Facebook like or Twitter like)

✔ Graphing with different engines. (dot,neato,twopi,circo,fdp)
