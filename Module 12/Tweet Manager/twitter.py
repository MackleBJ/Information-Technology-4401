from Tweet import Tweet
from datetime import datetime
import math
import pickle

def open_old_tweets():
    try:
        tweet_file = open("tweets.pickle", 'rb')
        Tweets = pickle.load(tweet_file)
        tweet_file.close()

        return Tweets

    except:
        Tweets = []

        return Tweets

def tweet_menu():
    print("\nTweet Menu")
    print("- - - - - -")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")

    answer = input("\nWhat would you like to do? ")

    return answer

def make_tweet():
    name = input("What is your name? ")

    while True:
        text = input("What would you like to tweet? ")
        if len(text) > 140:
            print("\nTweets can only be 140 characters!\n")
        else:
            break

    Tweets.append(Tweet(name, text))

    print("{}, your tweet has been saved.".format(name))

def recent_tweets():
    print("\nRecent Tweets")
    print("- - - - - -")

    if len(Tweets) == 0:
        print("There are no recent tweets.")
    else:
        index = (len(Tweets) - 1)
        printed = 0

        while printed < 5 and printed < (len(Tweets)):
            print("\n{} - {}".format(Tweets[index].get_author(), determine_time(Tweets[index].get_age())))
            print("{}".format(Tweets[index].get_text()))
            index -= 1
            printed += 1

def determine_time(time_since_tweet):
    time = time_since_tweet

    if time.seconds >= 3600:
        time = "{}h".format(math.floor(time.seconds/3600))
    elif time.seconds > 60 and time.seconds < 3600:
        time = "{}m".format(math.floor(time.seconds/60))
    elif time.seconds < 60:
        time = "{}s".format(time.seconds)

    return time

def search_tweets():
    if len(Tweets) == 0:
        print("\nThere are no tweets to search.")
    else:
        search_for = input("What would you like to search for? ")
        index = (len(Tweets) - 1)
        printed = 0
        print("Search Results")
        print("- - - - - -")

        for tweet in Tweets:
            text = Tweets[index].get_text()

            if search_for in text:
                print("\n{} - {}".format(Tweets[index].get_author(), determine_time(Tweets[index].get_age())))
                print("{}".format(Tweets[index].get_text()))
                printed += 1

            index -= 1

        if printed == 0:
            print("No tweets contained {}.".format(search_for))

def save_tweets():
    tweet_file = open("tweets.pickle", 'wb')
    pickle.dump(Tweets, tweet_file, pickle.HIGHEST_PROTOCOL)
    tweet_file.close()

Tweets = open_old_tweets()

while True:
    answer = tweet_menu()

    if answer == "1":
        make_tweet()
    elif answer == "2":
        recent_tweets()
    elif answer == "3":
        search_tweets()
    elif answer == "4":
        save_tweets()
        print("Thank you for using the Tweet Manager!")
        exit()
    elif answer == "one" or answer == "two" or answer == "three":
        print("Please enter a numeric value. ")
    else:
        print("Please select a valid option.")
