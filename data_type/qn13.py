# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

def getAlphaNumericalSortedSeq(input_str):
    unique_words = set(input_str)
    unique_words = sorted(unique_words)
    for each in unique_words:
        print(each, end='  ')


if __name__ == "__main__":
    list_words = ['hello', 'what', 'what',
                  'how', 'they', 'bibekG9', 'sun', 'think', 'think', 'think', '1Nepal', '2Asia', '3Kathmandu', '3Kathmandu', '3Kathmandu']
    getAlphaNumericalSortedSeq(list_words)
