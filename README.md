# Sentiment Analysis
Using Python and its packages to analyze a dataset of film reviews so they can automatically determine the sentiment of new comments and reviews.
Sentiment Analysis

The test data consists of 25000  positive and 25000 negative film reviews located in subfolders 'data\pos' and 'data\neg' respectively.

On scale 1-10 the review is considered negative with rating ranging 1-5 and positive with rating ranging  6-10.

Single file consists of single review.

# How it works

To run the program 2 arguments mus be given:
- new review : string
- word count : integer

For example:

Given the review: 

>*"This was an amazing movie."*

If the "block size" argument = 1, the program will generate sentiment scores for each single word:

>*"This" "was" "an" "amazing" "movie"*

before calculating the average sentiment score for the entire review.

If the "block size" argument = 2, sentiment will be additionaly generated for each consecutive two-word combination in the review:

>*"This was" "was an" "an amazing" "amazing movie"*

making it more precise. The same process can be repeated for larger block sizes.

The program analyzes positive and negative reviews from test data by checking how many times each word or phrase in the reviews is repeated in both databases, and saves the results in two dictionaries.

Then the user review is broken down into individual words or phrases. For each one, the sentiment is calculated based on the number of repetitions in positive and negative reviews.


The sentiment of a given word/phrase ranges from -1.0 to 1.0 where:

result < 0 indicates a negative sentiment for the word

result > 0 indicates a positive sentiment for the word

result = 0 indicates a neutral sentiment for the word or that  

words that did not appear in any of the reviews are ommited


For example:

If a word appears 6 times in positive reviews database and 4 times in negative reviews database the sentiment is calculated:

(6 - 4) / (6 + 4) = 2 / 10 = 0.2

The sentiment equals 0.2 which means it's > 0  therefore it's sentiment is positive.


Finally, the program calculates the sentiment of the user's review by calculating the average sentiment of all individual words.

# How to use
Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' followed by filepath then the review argument (string) and "block size" argument (integer).

# Code and Resources Used
Python Version: 3.10.7

Modules: click, glob
