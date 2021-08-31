"""Relational Operators Practice"""

__author__ = 730386258

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

left_int = (int(left))
right_int = (int(right))

greater = bool(left_int < right_int)
at_least = bool(left_int >= right_int)
equal = bool(left_int == right_int)
not_equal = bool(left_int != right_int)

greater_string = str(greater)
at_least_string = str(at_least)
equal_string = str(equal)
not_equal_string = str(not_equal)


print(left + " < " + right + " is " + greater_string)
print(left + " >= " + right + " is " + at_least_string)
print(left + " == " + right + " is " + equal_string)
print(left + " != " + right + " is " + not_equal_string)


