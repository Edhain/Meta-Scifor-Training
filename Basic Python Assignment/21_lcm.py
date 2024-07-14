def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = 48
num2 = 64

print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
