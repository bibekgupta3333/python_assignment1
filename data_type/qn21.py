# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def getSortedByLastCount(input_list):
    input_list.sort(key=lambda e: e[1])
    return input_list


if __name__ == "__main__":
    input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(getSortedByLastCount(input_list))
