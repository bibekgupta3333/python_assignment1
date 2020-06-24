# 32. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def getNthIteration(num):
    obj = {}
    for each in range(1, num+1):
        obj.update({each: each**2})
    return obj


if __name__ == "__main__":
    num = 10
    print(getNthIteration(num))
