from question import Question #Importing the Class Question from the questions.py file.
question_prompts = [ #Array of prompts for the user to respond to
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [ #Array of Question Objects with the correct answer defined.
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions): #Function named run_test with a single parameter, questions (the array above).
    score = 0 #Variable score that is storing how many correct answers are given
    for Question in questions: #For loop looping over question Class in questions Array
        answer = input(Question.prompt) #Variable answer storing the input from the user, via the prompt assigned to the input via the value passed thru the __init__ function. See more below.
        if answer == Question.answer: #If statement determining if the answer is equal to the answer attribute assigned from the questions array above.
            score += 1 #If they are equal, then increment the score by 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct") #printing on the console a string with the score that is incremented above (number converted to a string), and the length
                                                                            # of the questions being converted from a number to a string.

run_test(questions) #Calling the function and inputting the questions (array)

#answer = input(question.prompt) -- prompt is created in the questions_prompts, then it is called/passed into the questions Array and assigned as a value to the Class Question, storing it as an attribute
                                    # in the first slot/parameter prompt, it is then called later here. Question.prompt is the self.prompt assigned to the file question.py. Question (Object) is a single line in questions, which is being looped over.