"""print frequency of words"""
import sys
import json
import operator

def hw5(tweet_file):
    """Print top 10 hastags"""
    hash_dict = {}
    for tweet_line in tweet_file:
        try:
            tweet = json.loads(tweet_line)
            hastags = tweet["entities"]["hashtags"]
            for hashtag in hastags:
                try:
                    hash_dict[hashtag["text"]] += 1
                except(KeyError):
                    hash_dict[hashtag["text"]] = 1

        except(KeyError):
            pass

    sorted_hash_dict = sorted(hash_dict.iteritems(), 
        key=operator.itemgetter(1), reverse=True)

    for x in range(0, 10):
        print sorted_hash_dict[x][0], sorted_hash_dict[x][1]




def main():
    """run main program"""
    tweet_file = open(sys.argv[1])
    hw5(tweet_file)

if __name__ == '__main__':
    main()

