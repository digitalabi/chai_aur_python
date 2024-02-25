# Import

## math
```python
import math
```
### floor --> take towards lower end
```python
math.floor(3.9) # result is 3
math.floor (-3.5) # result is -4
```
### trunc --> take towards zer
```python
math.trunc(2.8) # result is 2
math.trunc(-2.8) # result is -2
```

### complex number
```python
2 +1j
(2+1j) *3 # result is (6+3j)
```

### Hex number starts with 0x
#### **0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F**
```python
0xFF
```

### Octal number starts with 0o
#### **0,1,2,3,4,5,6,7**
```python
0o20
```

### Binary number starts with 0b
#### **0,1**
```python
0b100
```
### conversion
```python
hex(64)
oct(64)
bin(64)
int(64)

int('40',16) # 'value' should respect the base ie. value coule be anything from 0-9,A-F for base16
int('64',8)  # 'value' should respect the base ie. value coule be anything from 0-7 for base8
int('10',2)  # 'value' should respect the base ie. value coule be anything from 0-1 for base2
# if we do different we will get ValueError
int('12',2) #will get error because '12' is not of base 2
```

### bitwise operation
```python
X<<2
X|2
```

## random

```python
import random

#to get random value between 0-1
random.random()

#to get random integer between the two number
random.radint(1,10)

#to get random in your choice
l1 = ['lemon','masala','ginger','mint']
random.choice(l1)

#to shuffle the list
random.shuffle(l1)
```

## Decimal
```python
# issues 0.1 + 0.1 + 0.1 - 0.3
from decimal import Decimal
Decimal ('0.1') + Decimal ('0.1') + Decimal ('0.1') - Decimal ('0.3')
```

## Fraction
```python
from fractions import Fraction
myFra = Fraction(2,7)
myFra        # O/P: Fraction(2,7)
print(myFra) # O/P: 2/7
str(myFra)   # O/P: '2/7'
repr(myFra)  # O/P: 'Fraction(2, 7)'
```

## set
```python
setone = {1,2,3,4}
settwo = {1,3}
intersection = setone & settwo
union = setone | settwo

#empty set
set()
setone - {1,2,3,4}
```

## check type
```python
type(setone)
type(set())
type({})
type (True)
```

## Boolean
```python
True == 1 #True
False == 0 #True
True is 1 #False
True + 4 #5
```