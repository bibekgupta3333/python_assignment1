# 39. Write a Python program to unpack a tuple in several variables.

# i have used globals dictionary
def unpackTupleIntoVar(input_tuple):
    obj = {}
    for each in range(len(input_tuple)):
        obj.update({f'var{each}': input_tuple[each]})
        # globals()[f'var{each}']=input_tuple[each]
    globals().update(obj)
    print(var0, var1, var4)


if __name__ == "__main__":
    input_tuple = tuple(range(10))

    unpackTupleIntoVar(input_tuple)
