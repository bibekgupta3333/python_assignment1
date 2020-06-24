# 14. Write a Python program to sort a list of dictionaries using Lambda.

getSortedDict = lambda input_dict: sorted(input_dict, key=lambda e: e['vehicle'])

if __name__ == "__main__":
    input_dict = [{'vehicle': 'lamgbourgini'}, {'vehicle': 'proshe'}, {'vehicle': 'tata'}, {'vehicle': 'mitsubhishi'},
                  {'vehicle': 'toyota'}]
    print(getSortedDict(input_dict))
