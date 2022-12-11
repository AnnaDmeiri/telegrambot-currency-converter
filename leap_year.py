x = int (input())
def is_leap_year(x):
    if x % 400 == 0: return True
    if x % 100 == 0: return False
    if x % 4 == 0: return True
    return False
print(is_leap_year(x=2000))

print(is_leap_year(x=2003))

print(is_leap_year(x=2004))

print(is_leap_year(x=2005))




