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

    return word_count

print(word_counter("twain.txt"))


