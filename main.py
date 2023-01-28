import quizlet_remake_functions
#Function opens the list of flashcards and imports them to this file in two seperate lists
flashcards_file_name = input("What is the name of the flashcard set you would like to use? ")
[terms, definitions] = quizlet_remake_functions.pull_flashcards(flashcards_file_name)
print(terms)
print(definitions)


