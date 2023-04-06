import glob


FILES_POSITIVE= glob.glob (r"data\pos\*.txt")
FILES_NEGATIVE= glob.glob (r"data\neg\*.txt")


def text_conversion (text):
    INTERPUNCTION = ".,!?%()[]{}\"-_"
    for char in INTERPUNCTION:
        text = text.replace (char, " ")
    text = text.lower().replace("<br />", " ").split()


def reviews_to_list (files_path):
    reviews = {}
    for file in files_path:
        with open (file, encoding='utf-8-sig') as stream: 
            record = stream.read ()
            text_conversion(record)
            for word in record:
                reviews [word] = reviews.get(word,0)
                reviews [word] += 1
    return (reviews)
            

def new_review(): 
    new_review = input ("Add new review: ")
    text_conversion(new_review)
    return (new_review)


def word_sentiment (pos_reviews, neg_reviews, new_review):
    sentiment_count = []
    for new_word in new_review:
        positive_count = pos_reviews.get(new_word, 0)
        negative_count = neg_reviews.get(new_word, 0)
        if (positive_count + negative_count) == 0:
            print ("Sentiment of: \"", new_word, "\"= 0.00")
        else:
            word_sentiment = (positive_count - negative_count)/(positive_count + negative_count)
            print ("Sentiment of: \"", new_word, "\"= ", word_sentiment)
            sentiment_count.append (word_sentiment)
    return (sentiment_count)
    
def review_sentiment (word_sentiment):
    sentiment_average = sum(word_sentiment)
    sentiment_average = len.word_sentiment()
    if sentiment_average > 0:
        label = "positive"
    else:
        label = "negative"

    print ("This sentence is ", label , sentiment_average)


def main():
    pos = reviews_to_list (FILES_POSITIVE)
    neg = reviews_to_list (FILES_NEGATIVE)
    new = new_review()
    ws = word_sentiment(pos, neg, new)
    review_sentiment(ws)


if __name__ == "__main__":
    main()
    print ("This is the end.")

