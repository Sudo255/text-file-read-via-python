# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

def read_file_content(filename):
    #open text file in read mode
    text_file = open(filename, "r")

    #read whole file to a string
    data = text_file.read()
    
    #close file
    text_file.close()

    return data


def count_words():
    # Create an empty dictionary
    d = dict()
    
    text = read_file_content("./story.txt")

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
    
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()
    
        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))
    
        # Split the line into words
        words = line.split(" ")
    
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
    
    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])