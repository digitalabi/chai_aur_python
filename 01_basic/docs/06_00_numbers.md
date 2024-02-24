# Numbers in Python

## Operators
    +
    -
    *
    /
    //
    %
    **
    -

In Python, number operators are used to perform various arithmetic operations on numeric data types such as integers, floating-point numbers, and complex numbers. Here are the common number operators in Python:

1. **Addition (`+`)**: Adds two operands.
   ```python
   result = 5 + 3  # result is 8
   ```

2. **Subtraction (`-`)**: Subtracts the right operand from the left operand.
   ```python
   result = 5 - 3  # result is 2
   ```

3. **Multiplication (`*`)**: Multiplies two operands.
   ```python
   result = 5 * 3  # result is 15
   ```

4. **Division (`/`)**: Divides the left operand by the right operand (always returns a float).
   ```python
   result = 5 / 3  # result is 1.6666666666666667
   ```

5. **Floor Division (`//`)**: Divides the left operand by the right operand and returns the integer value of the quotient.
   ```python
   result = 5 // 3  # result is 1
   ```

6. **Modulus (`%`)**: Returns the remainder of the division of the left operand by the right operand.
   ```python
   result = 5 % 3  # result is 2
   ```

7. **Exponentiation (`**`)**: Raises the left operand to the power of the right operand.
   ```python
   result = 5 ** 3  # result is 125
   ```

8. **Negation (`-`)**: Negates the operand.
   ```python
   result = -5  # result is -5
   ```

These operators can be used with different numeric data types, including integers, floats, and complex numbers, and they follow the usual rules of arithmetic. 

### Additionally, Python supports the use of parentheses `()` to specify the order of operations, just like in standard mathematics. Best practice is to use the clear code.

```python
(2+3)*4 #result is 20
```

### It is also best practice to convert the value to desired data type, instead of allowing explicit conversion

```python
#not best practice
40 + 2.23
#if you want result in integer
40 + int (2.23)
#if you want result in float
float(40) + 2.23
```
### python could support large numbers
```python
2 ** 1000 
# result is 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

```python
x,y,z
# (2,3,4) as tuple
```

## diff between repr(), str(), print()

```python
result = 1/3

result          #0.3333333333333333
repr(result)    #'0.3333333333333333'
str(result)     #'0.3333333333333333'
print(result)   e#0.3333333333333333
```

### repr()
    This function returns a string representation of an object that can be used to recreate the object. It aims to provide a precise, unambiguous representation of the object. It's mainly used for debugging and logging purposes. The string returned by repr() should ideally contain all the information needed to reconstruct the object. It's primarily meant for developers rather than end-users.

    In Python, an unambiguous representation means that the string returned by repr() should provide all the necessary information to identify and reconstruct the object exactly as it is.

### str()
    This function returns a string representation of an object that is more readable and user-friendly. It's intended for producing output for end-users. Unlike repr(), str() focuses on providing a human-readable representation rather than a precise one. 

### difference
    repr() aims for unambiguity, str() aims for readability.

    However, it's worth noting that for many built-in types in Python, the __repr__() and __str__() methods return similar or identical results. This is because Python often defines the __str__() method to call __repr__(), falling back to the more technical representation if a more human-readable one is not explicitly provided.

```python
from fractions import Fraction
myFra = Fraction(2,7)
myFra         # O/P: Fraction(2,7)
print(myFra)  # O/P: 2/7
str(myFra)    # O/P: '2/7'
repr(myFra)   # O/P: 'Fraction(2, 7)'
```

## Comparision
    ==
    !=    
    <
    >
    <=
    =>

In Python, conditional operators are used to perform comparisons between integers (and other types) and produce boolean results (`True` or `False`). Here are the commonly used conditional operators for integers:

1. **Equal to (`==`)**: Checks if two integers are equal.
   ```python
   x = 5
   y = 3
   result = x == y  # result is False
   ```

2. **Not equal to (`!=`)**: Checks if two integers are not equal.
   ```python
   x = 5
   y = 3
   result = x != y  # result is True
   ```

3. **Greater than (`>`)**: Checks if the left integer is greater than the right integer.
   ```python
   x = 5
   y = 3
   result = x > y  # result is True
   ```

4. **Less than (`<`)**: Checks if the left integer is less than the right integer.
   ```python
   x = 5
   y = 3
   result = x < y  # result is False
   ```

5. **Greater than or equal to (`>=`)**: Checks if the left integer is greater than or equal to the right integer.
   ```python
   x = 5
   y = 3
   result = x >= y  # result is True
   ```

6. **Less than or equal to (`<=`)**: Checks if the left integer is less than or equal to the right integer.
   ```python
   x = 5
   y = 3
   result = x <= y  # result is False
   ```

### logical operators
    and
    or
    not

#### and 
    Tea and Biscuit

#### or
    Tea or Coffee

#### not
    not sugar

Operators can be combined with logical operators (`and`, `or`, `not`) to form more complex conditions. For example:

```python
x = 5
y = 3
z = 7
result = (x > y) and (x < z)  # result is True
```

This checks if `x` is greater than `y` and less than `z`, which evaluates to `True`.

## Reference
https://www.youtube.com/watch?v=E4GNbP4SbKM