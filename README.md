# Sentiment Analysis
Using Python and its packages to analyze a dataset of film reviews so they can automatically determine the sentiment of new comments and reviews.
Sentiment Analysis

The test data consists of 25000  positive and 25000 negative film reviews located in subfolders 'data\pos' and 'data\neg' respectively.

On scale 1-10 the review is considered negative with rating ranging 1-5 and positive with rating ranging  6-10.

Single file consists of single review.

# How it works
The program analyzes positive and negative reviews by checking how many times each word in the reviews is repeated in both databases, and saves the results in two dictionaries.

Then, the program asks the user to enter their own review.

The review is broken down into individual words. For each word, the sentiment is calculated based on the number of repetitions in positive and negative reviews.


The sentiment of a given word ranges from -1.0 to 1.0 where:

result < 0 indicates a negative sentiment for the word

result > 0 indicates a positive sentiment for the word

result = 0 indicates a neutral sentiment for the word or that the word did not appear in any of the reviews.


For example:

If a word appears 6 times in positive reviews database and 4 times in negative reviews database the sentiment is calculated:

(6 - 4) / (6 + 4) = 2 / 10 = 0.2

The sentiment equals 0.2 which means it's > 0  therefore it's sentiment is positive.


Finally, the program calculates the sentiment of the user's review by calculating the average sentiment of all individual words.

# How to use
Using one's preferred code editor (e.g. VSCode), user enters keyword 'python' followed by filepath. Once the code's executed, user is asked to enter a review to then calculate its sentiment.

# Code and Resources Used
Python Version: 3.10.7

Modules: glob
