from datetime import datetime

# Class to create tweets.
class Tweet:

    # Method ot assign initial values.
    def __init__(self, name, text):
        self.__author = name
        self.__text = text
        self.__age = datetime.now()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        current_time = datetime.now()
        time_since_tweet = current_time - self.__age
        
        return time_since_tweet
