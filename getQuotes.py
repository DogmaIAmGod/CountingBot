from quotes import returnQuotes
import random


def getRandomQuote() -> str:
    quotesArray = returnQuotes()
    randomQuote = random.randrange(0, len(quotesArray))
    return quotesArray[randomQuote]
