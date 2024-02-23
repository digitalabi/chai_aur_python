# Python Shell (Command Line Interface - CLI)
The Python shell is a command-line interface that allows you to interact with the Python interpreter. It is a great way to test out code snippets or to learn more about how Python works.

To launch the Python shell, simply open a terminal window, type 'python', and hit enter.

Upon initiation, you'll encounter the Python prompt (>>>), indicating readiness for input.Here, you can input Python code and execute it by hitting enter.
 
The interpreter will then execute the code and print the results to the terminal.

For example, to print the string "Hello, world!", you would type the following code at the prompt:

```python
print("Hello, world!")
```
- to stop the shell press **Ctrl + D** or **Ctrl + Z**

## others example
```python
#use as calculator
3+5
```
```python
#operation with unexpected output
"chai" * 4
```
```python
#declaring variable
score = 100
```
```python
#print variable
score
```
```python
#loops
for c in 'chai'
   print (c)
```

```python
#import inbuild module
import os
```
```python
#run method
os.getcwd()
```

```python
#import inbuild module
import sys
```
```python
#run variable/attribute
sys.platform
```

```python
#to import scripts/module
import hello_chai
```
```python
#run method:
hello_chai.chai("green tea")
```

```python
#run attribute/variable:
hello_chai.chai_one
```

During import system creates binaries, so if we made any changes in our code the we need to
   - either close python shell and reopen it
   - or import reload from importlib 
  
```python
from importlib import reload
reload (hello_chai)
```
```python
#run attribute/variable:
hello_chai.chai_one
```
### Errors:
- NameError:
- AttributeError:
- IndentationError:

Reference video:
https://www.youtube.com/watch?v=OEKrDogH5ew