try:
    num = int(input("enter a number"))
    sum = 10 / num
except ValueError:
    print("invalid inout")
finally:
    print("code executed")