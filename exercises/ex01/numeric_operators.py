"""Numeric Operators Practice"""

__author__ = "730386258"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

Left_int = (int(left))
Right_int = (int(right))

power = str(Left_int ** Right_int)
division = str(Left_int / Right_int)
intdivision = str(Left_int // Right_int)
modulo = str(Left_int % Right_int)

print(left + " ** " + right + " is " + power)
print(left + " / " + right + " is " + division)
print(left + " // " + right + " is " + intdivision)
print(left + " % " + right + " is " + modulo)