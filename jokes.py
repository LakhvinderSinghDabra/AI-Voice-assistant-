import pyjokes
def speakJokes():
    joke=pyjokes.get_joke()
    print(joke)
    return joke
speakJokes()
    