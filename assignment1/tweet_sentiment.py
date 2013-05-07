import sys
import json

# Returns an int
def get_sentiment(sent_dict, tweet_text):
    """get sentiment value according to sent_file dictionary"""
    sent_value = 0
    word_list = (tweet_text
            .replace('\n', '')
            .replace(',', '')
            .replace('.', '')
            .rsplit(' '))
    for word in word_list:
        try:
            sent_value = sent_value + sent_dict[word]
        except(KeyError):
            pass

    return sent_value

def parse_sentiment(sent_file):
    """returned dictionary of term and sentiment score"""
    sent_dict = {}
    for sent_line in sent_file:
        sent_item = sent_line.replace('\n', '').rsplit('\t')
        sent_dict[sent_item[0]] = float(sent_item[1])
    
    return sent_dict

def hw(sent_file, tweet_file):
    """homework function that loads sent_file to memory and reads
    tweet_file lines then prints sentiment for each line"""
    sent_dict = parse_sentiment(sent_file)
    for tweet_line in tweet_file:
        try:
            tweet = json.loads(tweet_line)
            tweet_text = tweet["text"]
            sentiment = str(get_sentiment(sent_dict, tweet_text))
            print sentiment
        except(KeyError):
            pass






def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
