"""write a program in Python to classify triangles and use an automated test platform
   The calculation is accurate to the two decimal places"""
def classify_triangle(a, b, c):
    """identify if it a triangle
    if it's a triangle, identify the type of the triangle"""
    if a + b <= c or a + c <= b or b + c <= a:
        return "It's not a triangle."

    if a == b == c:
        return "It's an equilateral triangle."

    if (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
        if round(a*a + b*b, 2) == round(c*c, 2) or round(a*a + c*c, 2) == round(b*b, 2) or round(b*b + c*c, 2) == round(a*a, 2):
            return "It's an isosceles and right triangle."
        return "It's an isosceles triangle."
    if a != b and a != c and b != c:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "It's a right and scalene triangle."
        return "It's a scalene triangle."


def user_input():
    """acquire the parameter entered by user
       check if parameters is valid"""
    while True:
        a = input("Please input three length of triangle size A:")
        b = input("Please input three length of triangle size B:")
        c = input("Please input three length of triangle size C:")
        try:
            return float(a), float(b), float(c)
            break
        except ValueError:
            return "Please input numeral values"

if __name__ == '__main__':
    a, b, c = user_input()
    print(classify_triangle(a, b, c))
