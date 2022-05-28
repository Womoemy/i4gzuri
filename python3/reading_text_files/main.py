# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as openfile:
        file_content = openfile.read()
    return file_content

def count_words():
    # [assignment] Add your code here
    
    # supplying file path and splitting file into words
    text = read_file_content("python3/reading_text_files/story.txt")
    text = text.lower()
    words = text.split()
    words = [word.strip('.,?!') for word in words]
    
    # create dictionary and pass words count to dictionary
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict

print(count_words())