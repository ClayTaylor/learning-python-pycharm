
#Milkshake Language
#vowels -> h
#-------

#cat = cht
#dog = dhg

def translate (phrase): #Function named translate with a single parameter named phrase
    translation = "" # Variable set to a string
    for letter in phrase: #For loop named letter looping over phrase
        if letter in "AEIOUaeiou": #If statement checking to see if letter has any upper and/or lowercase vowels
            translation = translation + "h" #Variable translation is equal to itself plus the letter 'h' replacing the vowels if the If statement above is True
        else: #If statement if the above is false, return the translation + the letter originally posted if the letter is a consonant.
            translation = translation + letter
    return translation #Returning the variable translation from the function
print(translate(input("Enter a phrase: "))) #printing the result of the function (translate) and taking the input for the phrase from a user input.

