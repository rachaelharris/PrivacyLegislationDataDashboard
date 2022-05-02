from textblob import TextBlob
import sys, re, operator, string

def convert_file_to_string(file):
    #open text file in read mode
    text_file = open(file, "r")

    #read whole file to a string
    data = text_file.read()
    return data

""" Approach to analyze one file. """

# convert file to string to analyze contents
string_contents = convert_file_to_string('data/Wisconsin-SB997.tex')

""" Approach to analyze files within a whole folder. """
# analyze whole folder
# directory_name = 'data'

# for file_name in os.listdir(directory_name):
#     i = os.path.join(directory_name, file_name)
#     if os.path.isfile(i):
#         string_contents = convert_file_to_string(i)
#         string_contents = string_contents.encode().decode()

# cast to TextBlob for sentiment analysis
blob = TextBlob(string_contents)

# print analysis
result = blob.sentiment.polarity
print(result)

if result > 0:
    print("label: positive")
if result == 0:
    print("label: neutral")
if result < 0:
    print("label: negative")

def filter_chars_and_normalize(str_data):
    """
    Takes a string and returns a copy with all non-alphanumeric
    chars replaced by white space
    """
    pattern = re.compile(r'[\W_]+')
    return pattern.sub(' ', str_data).lower()

def scan(str_data):
    """
    Takes a string and scans for words, returning
    a list of words.
    """
    return str_data.split()

def remove_stop_words(word_list):
    """
    Takes a list of words and returns a copy with all stop
    words removed
    """
    with open('stop_words.txt') as f:
        stop_words = f.read().split(',')
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in stop_words]

def frequencies(word_list):
    """
    Takes a list of words and returns a dictionary associating
    words with frequencies of occurrence
    """
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs

def sort(word_freq):
    """
    Takes a dictionary of words and their frequencies
    and returns a list of pairs where the entries are
    sorted by frequency
    """
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

def print_all(word_freqs):
    """
    Takes a list of pairs where the entries are sorted by frequency and print them recursively.
    """
    if(len(word_freqs) > 0):
        print(word_freqs[0][0], ' - ', word_freqs[0][1])
        print_all(word_freqs[1:]);

if __name__ == "__main__":
    str_data = string_contents
    str_data = filter_chars_and_normalize(str_data)
    word_list = scan(str_data)
    word_list = remove_stop_words(word_list)
    word_freq = frequencies(word_list)
    word_freqs = sort(word_freq)

    for tf in word_freqs[0:5]:
        print(tf[0], "-", tf[1])
