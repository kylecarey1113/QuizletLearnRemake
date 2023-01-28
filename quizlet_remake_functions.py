def pull_flashcards(filename):
    file_flashcards = open(filename, 'r')
    list_flashcards = file_flashcards.readlines()
    
    terms = []
    definitions = []
    for i in range(len(list_flashcards)):
        temp = list_flashcards[i].split(' - ')
        terms.append(temp[0])
        definitions.append(temp[1])

    return(terms, definitions)
