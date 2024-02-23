# Immutable and Mutuable in Python

## Mutable
- changeable
- could change in memory reference point
- List, dictionary

## Immutable
- not changeable
- could not change in memory, new memory point is created 
- once value is created old pointer of variable is moved

## Changing the independent variable
```python
username = 'chai aur code'
username
username = 'chai aur python'
```
Working for immutable objects
### Step 1 : We created an immutable object
We created string attribute/variable called username with value of "chai aur code". 
#### Internally python will create a memory reference and store the value "chai aur code", and the attribute username will point to the memory reference.

![Alt text](/images/04_immutable_step1.png)

### Step 2: We change the immutable object
we reassign the attribute username to "chai aur python"
#### Internally python will create a new memory reference and store the value "chai aur python", and memory reference pointer of the attribute username will point to new memory reference.

![Alt text](/images/04_immutable_step2.png)

### Step 3: Garbage collection
Later garbage collector of python will cleanup the memory reference associated with "chai aur code"

![Alt text](/images/04_immutable_step3.png)

## Changing the dependent variable
```python
x = 10
y = x
#print X
x
#output will be 10
#print y
y
#output will be 10
#change the value of X
x=15
#print x
x
#output will be 15
#print y
y
#output will be 10
```

### Step 1:
![Alt text](/images/04_immutable_indirect_step1.png)

### Step 2:
![Alt text](/images/04_immutable_indirect_step2.png)


## ref_count
- each memory reference has a variable called ref_count.
- ref_count keep the count of how many times the memory is referenced/used by variable
- if ref_count is 0 then, memory will be cleaned by garbage collector

Garbage collector collect/clean number and string in optimized way. It don't clean it immediately.

## Reference
https://www.youtube.com/watch?v=MDZ4y-GgZ8k
