"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if message.startswith('@bob_der_bot'):
        message = message.split(' ',1)[1]
    if "+" in message:
        arguments = message.split('+')
        number1 = int(arguments[0])
        number2 = int(arguments[1])
        return str(number1 + number2)
    if "Which Pokemon is #1" in message:
        return "Digga Bulbasaur"
    return "false"

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (140 chars max)
    berlin_time = datetime.now(timezone('Europe/Berlin'))
    text = berlin_time.strftime("Der HPI-Schuelerkolleg Bot sagt: %H:%M:%S! %A (%d-%m-%Y).")
    return text
