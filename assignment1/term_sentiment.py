"""import system library"""
import sys
import json

def get_sentiment(sent_dict, tweet_text):
    """get sentiment value according to sent_file dictionary"""
    sent_value = 0
    word_list = (tweet_text
            .replace('\n', ' ')
            .replace(',', ' ')
            .replace('.', ' ')
            .rsplit(' '))
    for word in word_list:
        try:
            sent_value = sent_value + sent_dict[word]
        except(KeyError):
            pass

    return sent_value

#return words not in the sent_file dictionary
def get_words_not_in_dict(sent_dict, tweet_text):
    """ return array or words not in dictionary"""
    new_terms = []
    word_list = (tweet_text
            .replace('\n', '')
            .replace(',', '')
            .replace('.', '')
            .rsplit(' '))
    for word in word_list:
        try:
            sent_dict[word]
        except(KeyError):
            new_terms.append(word)

    return new_terms


def hw2(sent_file, tweet_file):
    """returns nothing. called by the main function"""
    sent_dict = {}
    new_terms_dict = {}
    for sent_line in sent_file:
        sent_item = sent_line.replace('\n', '').rsplit('\t')
        sent_dict[sent_item[0]] = int(sent_item[1])

    for tweet_line in tweet_file:
        try:
            tweet = json.loads(tweet_line)
            tweet_text = tweet["text"]
            sentiment = get_sentiment(sent_dict, tweet_text)
            unknown_words = get_words_not_in_dict(sent_dict, tweet_text)
            for word in unknown_words:
                try:
                    new_terms_dict[word].append(sentiment)
                except(KeyError):
                    if word != "":
                        new_terms_dict[word] = []
                        new_terms_dict[word].append(sentiment)

        except(KeyError):
            pass

    for new_term, sent_values in new_terms_dict.iteritems():
        sent_average = float(sum(sent_values))/float(len(sent_values))
        print new_term.encode('utf-8'), str(sent_average)




def lines(fp):
    """returns number of lines in a file"""
    print str(len(fp.readlines()))

def main():
    """run main program"""
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw2(sent_file, tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
