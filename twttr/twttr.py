"""Remove vowels from text entered by the user."""
def main():

    def shorten(word: str) -> str:
        vowels = "aeiouAEIOU"
        return "".join(character for character in word if character not in vowels)

    word = str(input("Please write a word to shorten: "))

    print(shorten(word))


main()