"""print frequency of words"""
import sys
import json

def hw3(tweet_file):
    """Print top 10 hastags"""
    word_list = []
    word_dict = {}
    for tweet_line in tweet_file:
        try:
            tweet = json.loads(tweet_line)
            tweet_text = tweet["text"]
            words = (tweet_text
            .replace('\n', ' ')
            .replace(',', ' ')
            .replace('.', ' ')
            .replace(':', ' ')
            .split())
            word_list.extend(words)
        except(KeyError):
            pass

    total_words = len(word_list)
    #iterate through words and count word frequency in word_dict
    for word in word_list:
        if word.strip() != "":
            try:
                word_dict[word.strip()] += 1
            except(KeyError):
                word_dict[word.strip()] = 1

    #go through word_dict and print word frequency
    #divided by total number of words
    for term, frequency in word_dict.iteritems():
        try:
            print term.encode('utf-8'), float(frequency) / float(total_words)
        except(UnicodeDecodeError):
            pass





def main():
    """run main program"""
    tweet_file = open(sys.argv[1])
    hw5(tweet_file)

if __name__ == '__main__':
    main()

