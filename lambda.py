def run():
    def palindrome(string):
        return string == string [::-1]
    
    print(palindrome('ANA'))

palindrome_Lambda = lambda string : string == string[::-1]

print(palindrome_Lambda("anitalavalatina"))


if __name__ == "__main__":
    run()