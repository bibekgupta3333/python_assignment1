# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


def isListDictEmpty(input_list):
    if isinstance(input_list, list):
        for each in input_list:
            if bool(each) and (isinstance(each, dict) or isinstance(each, set)):
                return False

        return True
    else:
        return "please give a list as argument"


if __name__ == "__main__":
    input_list = [{}, {}, {}]
    print(isListDictEmpty(input_list))
