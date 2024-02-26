# Dictionary
- store values in key value pair

## create
```python
chai_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Bitter"}
chai_types = dict({"Masala":"Spicy","Ginger":"Zesty","Green":"Bitter"})
```
## basic
```python
print(chai_types)
#get values
chai_types["Masala"]
chai_types.get("Masala")

#add values
chai_types["Lemon"] = "sour"

#modify values
chai_types["Green"] = "Fresh"
```

## loops
```python
for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key,value)
```

## condition
```python
if "Masala" in chai_types:
    print("I have masala chai")
```

## method
```python
#length
len(chai_types)

#pop
chai_types.pop("Ginger")

#popitem
chai_types.popitem()

#delete
del chai_types["Green"]

#clear 
chai_types.clear()

#copy
chai_types_copy = chai_types
chai_types_copy = chai_types.copy()
```

## matrix
```python
tea_shop = {
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"strong"}
}

print(tea_shop)

tea_shop["chai"]
tea_shop["chai"]["Ginger"]
```

## comprehension
```python
squared_num = {x:x**2 for x in range(6)}
squared_num
```

## new dictionary from list
```python
keys = ["Masala","Ginger","Lemon"]
default_values = "Delicious"
new_chai_types = dict.fromkeys(keys, default_values)
print(new_chai_types)

new_chai_types = dict.fromkeys(keys,keys) #see what will happen
```

## Reference
https://www.youtube.com/watch?v=DHQWUXeEvow
https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/
