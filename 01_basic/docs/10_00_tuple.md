# Tuples
- List is mutable , tuple is immutable
- imporve performace

## create
```python
tea_types = ("Black","Green","Oolong")
tea_types = tuple(("Black","Green","Oolong"))
tea_types = ("Tea",) # for one item add , at the end
```

## basic
```python
print(tea_types)
print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:3])
print(tea_types[:2])
print(tea_types[2:])
print(tea_types[1:1])

#adding value/replacing --> not possible since it is immutable
###tea_types[3] = "Herbal"
###tea_types[1:2] = ("Lemon")

#start to insert from position 1 and push other values to back --> not possible
###tea_types[1:1] = ("test","test")

# insert blank
###tea_types[1:3] = []
```

## so how to add values in a tuple???
### add tuple to tuple
```python
more_tea = ("hot lemon","Masala")
all_tea = tea_types + more_tea

tea_types += more_tea

#TypeError: can only concatenate tuple (not "str") to tuple
### all_tea = tea_types + ("Milk")
```
### convert tuple to list then modify and convert it back
```python
tea_types = ("Black","Green","Oolong")
tea_list = list(tea_types)
tea_list.append("hot lemon")
tea_list.append("Masala")
tea_types = tuple(tea_list)
```

## loops
```python
for tea in tea_types:
        print(tea)

for tea in tea_types:
        print(tea,end="-")
```

## condition
```python
if "Oolong" in tea_types:
    print("I have Oolong tea.")
```

## methods
```python
#type
type(tea_type)

#insert in certain position, other values after the position shift one position right
#tea_types.insert(1,"Ginger")

#append method is not available
###tea_types.append("Masala")

#len
len(tea_types)

#count
tea_types.count("Masala")

#pop -> remove last value
#tea_types.pop()

#remove
#tea_types.remove("green")

#delete
del tea_types
tea_types

#copy
tea_varitis_copy = tea_types #point to the same memeory location
#tea_varitis_copy = tea_types.copy() #copy function not available
print(tea_varitis_copy)
```

## comprehension
```python
# try this, it will gave something else haha
squared_num = (x**2 for x in range(10))
print(squared_num)
```
## common use case
```python
#
tea_types = ("Black","Green","Oolong")
(black, green, oolong) = tea_types
black
```
#nested tuple/matrix
```python
nested_tuple = ("",(1,2,3),"")
nested_tuple[1]
nested_tuple[1][1]
```
## reference
![Alt text](/images/list_vs_tuple.png)

https://www.youtube.com/watch?v=ALGOl8pJc44

