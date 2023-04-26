#EXAMPLE REVIEW
#python PORTFOLIO/!commity/Sentiment-Analysis/commit_6/SENTIMENT.py "This was such an amazing movie. The performances of all the actors were astonishing. I didn't like some of the dialog but overal I enjoyed the movie. I give it 8/10." 1

"""
Usage:
python SENTIMENT.py <new_review> <word_count>
"""

import click
import glob


FILES_POSITIVE= glob.glob (r"PORTFOLIO\Sentiment-Analysis\data\pos\*.txt")
FILES_NEGATIVE= glob.glob (r"PORTFOLIO\Sentiment-Analysis\data\neg\*.txt")


def text_conversion (text: str)-> list[str]:
    INTERPUNCTION = ".,!?%()[]{}\"-_"
    text.lower().replace("<br />", " ")
    for char in INTERPUNCTION:
        text = text.replace (char, ".")
    sentences = text.split('.')
    return sentences


def get_phrases (sentences: list[str], word_count:int)->list[str]:
    phrases =[]
    for s in sentences:
        words = s.split()
        for i, w in enumerate(words):
            if i < len(words)-word_count+1:
                phrase = w
                counter = 1
                while counter < word_count:
                    phrase = f'{phrase} {words[i + counter]}'
                    counter += 1
                phrases.append (phrase)
    return phrases


def open_file (filepath: str)-> str:
        with open (filepath, encoding='utf-8-sig') as stream: 
            record = stream.read ()
        return record


def reviews_sentiment (filepaths: list[str], word_count: int)-> dict[str,int]:
    review = {}
    for f in filepaths:
        text_review = open_file (f)
        sentences = text_conversion(text_review)
        phrases = get_phrases (sentences, word_count)
        for p in phrases:
            review [p] = review.get(p,0)
            review [p] += 1
    return review
            

def new_review_to_word_groups (new_review: str, word_count: int)-> list [str]: 
    new_sentences = text_conversion(new_review)
    new_phrases = get_phrases (new_sentences, word_count)
    return new_phrases


def generate_phrase_sentiment (pos_reviews: dict[str,int], neg_reviews: dict[str,int], phrase:str)-> float:
    pos_count = pos_reviews.get(phrase, 0)
    neg_count = neg_reviews.get(phrase, 0)
    phrase_sentiment = 0
    if pos_count==0 and neg_count == 0:
        pass
    elif (pos_count + neg_count) == 0:
        phrase_sentiment = 0
    else:
        phrase_sentiment = float("%.3f" % ((pos_count - neg_count)/(pos_count + neg_count)))
        print (f'{phrase_sentiment:8}  {phrase}')
    return phrase_sentiment


def generate_review_sentiment (sentiment_count: list[float])->None:
    sentiment_average = 0
    if len(sentiment_count) == 0:
        label = 'neutral'
    else:    
        sentiment_average = sum(sentiment_count)/ len(sentiment_count)
        if sentiment_average > 0:
            label = "positive"
        elif sentiment_count == 0:
            label = 'neutral'
        else:
            label = "negative"
    print (f'\n This reviews sentiment is {label}:', "%.3f" % sentiment_average)


@click.command()
@click.argument('new_review')
@click.argument('word_count')
def main(new_review: str, word_count: int)-> None:
    print ('SENTIMENT WORD / PHRASE')
    sentiment_count = []
    for i in range(1,int(word_count)+1):
        pos_reviews = reviews_sentiment (FILES_POSITIVE, i)
        neg_reviews = reviews_sentiment (FILES_NEGATIVE, i)
        new_phrases = new_review_to_word_groups (new_review, i)
        for np in new_phrases:
            np_sentiment = generate_phrase_sentiment(pos_reviews, neg_reviews, np)
            sentiment_count.append(np_sentiment)
    generate_review_sentiment (sentiment_count)

    
if __name__ == "__main__":
    main()

