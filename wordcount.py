# put your code here.
def word_counter(filename):
    """Count how many times a space-separated word appears.
    """

    file = open(filename)

    word_count = {}

    for line in file:
        words = line.strip("\n").split(" ")
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    # Iterate through dictionary and print:
    for key, value in word_count.items():
        print(f"{key} {value}")


    return word_count

word_counter("test.txt")


