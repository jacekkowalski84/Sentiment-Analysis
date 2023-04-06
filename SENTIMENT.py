import glob

INTERPUNCTION = ".,!?%()[]{}\"-_"
FILES_POSITIVE= glob.glob (r"data\pos\*.txt")
FILES_NEGATIVE= glob.glob (r"data\neg\*.txt")


reviews_positive = {}
reviews_negative = {}

#CREATING LIST OF POSITIVE REVIEWS

for file_positive in FILES_POSITIVE:
    with open (file_positive, encoding='utf-8-sig') as stream: #dopisanie argumentu encoding znalazłem w podowiedziach na slacku
        record = stream.read ()
        for char in INTERPUNCTION:
            record = record.replace (char, " ")
        record = record.replace ("<br />", " ")
        record = set(record.lower().split())
        for word in record:
            if word not in reviews_positive:
                reviews_positive[word] = 0
            reviews_positive[word] += 1
            

#CREATING LIST OF NEGATIVE REVIEWS

for file_negative in FILES_NEGATIVE:
    with open (file_negative, encoding='utf-8-sig') as stream: #dopisanie argumentu encoding znalazłem w podowiedziach na slacku
        record = stream.read ()
        for char in INTERPUNCTION:
            record = record.replace (char, " ")
        record = record.replace ("<br />", " ")
        record = set(record.lower().split())
        for word in record:
            if word not in reviews_negative:
                reviews_negative[word] = 0
            reviews_negative [word] += 1

#ASKING USER FOR A NEW REVIEW AND CHANGING IT TO LIST
 
new_review = input ("Add new review: ")
for char in INTERPUNCTION:
    new_review = new_review.replace (char, " ")
new_review = new_review.lower().split()

#CALCULATING SENTIMENT FOR EACH INDIVIDUAL WORD IN NEW REVIEW

sentiment_count = []

for new_word in new_review:
    positive_count = reviews_positive.get(new_word, 0)
    negative_count = reviews_negative.get(new_word, 0)
    if (positive_count + negative_count) == 0:
        print ("Sentiment of: \"", new_word, "\"= 0.00")
    else:
        word_sentiment = (positive_count - negative_count)/(positive_count + negative_count)
        sentiment_count.append (word_sentiment)
        print ("Sentiment of: \"", new_word, "\"= ", word_sentiment)
    
# CALCULATING SENTIMENT FOR THE WHOLE NEW REVIEW

sentiment_average = sum(sentiment_count)
if sentiment_average > 0:
    label = "positive"
else:
    label = "negative"

print ("This sentence is ", label , sentiment_average)
