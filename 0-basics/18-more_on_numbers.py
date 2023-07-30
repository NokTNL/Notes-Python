# Complex numbers
complex_num = 1+2j # Complex number literal
complex_num = complex(1, 2) # Using the `complex()` constructor works as well

print(type(complex_num)) # <class 'complex'>
print(complex_num.real, complex_num.imag) # 1.0 2.0

# Built-in math functions
print(abs(-1)) # 1
print(round(1.50)) # 2