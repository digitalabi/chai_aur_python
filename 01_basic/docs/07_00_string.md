# String
    'string'
    "string"
    """String"""

```python
chai = "Masala chai"
#first character
first_char = chai[0]
print(first_char)

#slice masala from masala chai
slice_chai = chai[0:6]
print(slice_chai)

number_list = "0123456789"
#print all characters
number_list[:]
#print from certain position till end
number_list[3:]
#print fom begining till certain position
number_list[:7]
#print fom certain position to certain position
number_list[3:7]
# print with certain jump
number_list[0:7:2]
```

## method in string
```python
chai = 'Masala Chai'
#all lower case
print(chai.lower())

#all upper case
print(chai.upper())

chai2 = "   Masala Chai    "

#remove space in string
print(chai.strip())

#replace string -> need to match the case of string/case sensitive
print(chai.replace("Masala","Ginger"))

#find in string, if return -1, that means it didn't find it
print(chai.find("Chai")

#count
print(chai.count("chai"))

#length
print(len(chai))

#escape characters
he_said = "He said, \"Masala chai is awesome.\""
print(he_said)

#raw character
path = r"c:\user\path"
path2 = "c:\\user\\path"
print(path)

```

## convert string to list
```python
chai = "Lemon, Ginger, Masala, Mint"
chai_list = chai.split(", ")
```

## convert list to string
```python
chai_list= ["Lemon","Masala","Ginger"]
chai = ", ".join(chai_list)
```

## loops in string
```python
chai = "Masala Chai"
for letter in chai:
    print(letter)
```

## check if available or not in string
```python
chai = "Masala Chai"

print("Masala" in chai)
```

## placeholder 
```python
#masala chai
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))
```

## Reference
https://www.youtube.com/watch?v=ekrgx893sig
