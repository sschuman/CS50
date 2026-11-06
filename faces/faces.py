# Implement a function called [convert] that accepts
# a [str] as input and returns that same input with any :)
# converted to a smiley face emoji and any :( converted 
# to a frowning face emoji. All other text should be returned unchanged.
def main():

    phrase = input("Please enter anything you would like: ")

    def convert(phrase):
        phrase = phrase.replace(":)", "🙂")
        phrase = phrase.replace(":(", "🙁")
        return phrase

    print(convert(phrase))

main()