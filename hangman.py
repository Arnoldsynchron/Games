# Problem Set 2, hangman.py
# Name: Precious Onu
# Collaborators: Self
# Time spent: 20 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    Cond = []
    secret_word = secret_word.lower()
    #letters_guessed = letters_guessed.lower()
    for i in range(len(secret_word)):
        found = False
        for j in range(len(letters_guessed)):
           if  secret_word[i] == letters_guessed[j]:
               found = True
               break
        Cond.append(found)
    return sum(Cond) == len(secret_word)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters = []
    secret_word = secret_word.lower()
    #letters_guessed = letters_guessed.lower()
    for word in secret_word:
        found = '_'
        for guess in letters_guessed:
            if word == guess:
                found = word
                break
        letters.append(found)
    return ' '.join(letters)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    alphabets = string.ascii_lowercase
    letters = []
    #letters_guessed = letters_guessed.lower()
    for word in alphabets:
        found = word
        for guess in letters_guessed:
            if word == guess:
                found = '_'
                break
        if found != '_':
            letters.append(found)
    return ''.join(letters)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # import string
    
    word_length = len(secret_word)
    guesses = 6
    warnings = 3
    available = string.ascii_lowercase
    found = False
    memory = []
    print('Welcome to the game Hangman!')
    print()
    print('Hi there (^_^) I\'m thinking of a word that is', word_length,'letters long')
    while guesses > 0:
        print('---'*20)
        print('You have {} warnings left.'.format(warnings))
        print('You have {} guesses to get it right.\n Remember its {} lettered'.format(guesses, word_length))
        print('==='*15)
        print('Available letters:',available)
    
        prompt = 'Please guess a letter: '
        
        def input_warning(warnings, guesses):
            warnings -= 1
            if not warnings+1 > 0:
                guesses -= 1
                warnings = 3
            return warnings, guesses
        
        def print_out():
            print('You have {} warnings left.'.format(warnings))
            print('You have {} guesses to get it right'. format(guesses))
            
        guesses = guesses
        
        while True:
            letters_guessed = str(input(prompt)).lower()
            try: 
                if len(letters_guessed) != 1:
                    warnings, guesses = input_warning(warnings,guesses)
                    raise Exception ('Please enter a letter')
             
                elif not type(letters_guessed) is str:
                    warnings, guesses = input_warning(warnings,guesses)
                    raise TypeError('Enter a string object please, you typed in a {} object'.format(type(letters_guessed)))

                else:
                    if not str.isalpha(letters_guessed):
                        warnings, guesses = input_warning(warnings,guesses)
                        raise ValueError('Input is not an alphabet')
                
            except TypeError as te:
                print(te)
                print_out()
                continue
            except Exception as e:
                print(e)
                print_out()
                continue
            except ValueError as ve:
                print(ve)
                print_out()
                continue
            
            if len(letters_guessed) == 1 and type(letters_guessed) is str and str.isalpha(letters_guessed):
                break
            

        
        def warning_count(memory, letters_guessed, warnings, guesses):
            mem = False
            for a in memory:
                if letters_guessed == a:
                    mem = True
            if mem:
                if warnings+1>0:
                    warnings -= 1
                    print('Oops! you\'ve already guessed that letter, you now have',warnings,'warnings')
                    if warnings == 0:
                        warnings = 3
                        guesses -=1
                        print('You have no warnings left so you lose one guess')
            return warnings,guesses, mem
                    
        #Vowel reduction mark
        def vowels_effect(letter, guesses):
            vowels = ['a','e','i','o','u']
            vowel = False
            for v in vowels:
                if v == letter:
                    vowel = True
                    break
            if vowel:
                guesses -= 1              
            return guesses        
        
        memory_2 = memory[:]
        def check_prescence(secret_word, letters_guessed, guesses, warnings, memory): #check word prescence
            store = []
            for a in secret_word:
                found = False
                if a == letters_guessed:
                    found = True
                store.append(found)
            if sum(store)>0:
                print(letters_guessed, 'is  present in word')
                warnings, guesses, mem = warning_count(memory,letters_guessed,warnings,guesses)
            else:
                print('Oops!', str(letters_guessed), 'is not in my word:', guessed_word)
                
                warnings, guesses, mem = warning_count (memory, letters_guessed, warnings, guesses)
                
                if not mem:
                    guesses -= 1        #Updates number of guesses
                    guesses = vowels_effect(letters_guessed, guesses)
            return guesses, warnings
        
        for guess in letters_guessed: #Memory update of letters used
            memory.append(guess)
        
        guessed_word = get_guessed_word(secret_word, memory)     
        
        guesses, warnings = check_prescence(secret_word, letters_guessed, guesses, warnings, memory_2)
        
        print()
        print('letters used: ', memory)
        print("Guessed letter(s) in word")
        print('-------------------------')
        print(guessed_word)
        print();print();
        
        if is_word_guessed(secret_word, memory): #if complete word is found
            found = True
            break
        available = get_available_letters(memory)
        
        def count_distinct(secret_word):  #Number of unique letters
            secret_word = list(secret_word)
            secret_word_copy = secret_word[:]  #create a duplicate
            count_no_dup = []
            for word in secret_word:
                count = []
                match = False
                for w in secret_word_copy:
                    if word == w:
                        match = True
                        count.append(1)
                if match:
                    unique_score = 1/sum(count)
                else:
                    unique_score = 0
                count_no_dup.append(unique_score)
            return round(sum(count_no_dup))
        
        distinct_count = count_distinct(secret_word)
        
    if found:
        print()
        print('<|:)', 'Oh! party scatter, party scatter')
        print("'```'`''`'`'`'`'`'`'`'`'`'`'`'`'`'`''`'")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('||||||||||||||||||||||||||||||||||||')
        print()
        print("Congratulations!!!, you're a Natural")
        score = guesses*distinct_count
        print('Your total score for this game is:', score)
    else: 
        print()
        print('(T_T)', ':-o')
        print("Ooops! out of guesses. Play again!")
        print("The secret word was:", secret_word)
        
        
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    store = []
    if len(my_word) == len(other_word):
        
        under_scores = []
        for i, j in zip(my_word,other_word):
            if  i == j or i == '_':
                store.append(i)
                if i == '_':
                    under_scores.append(i)
                    
        if len(store) == len(other_word):

            #Different word:
            def check_diff(my_word, other_word):
                not_in = []
                for letter in other_word:
                    is_match = False
                    for lttr in my_word:
                        if letter == lttr:
                            is_match = True
                            break
                    if not is_match:
                        not_in.append(letter)
                return not_in

            not_in = check_diff(my_word,other_word)

            return len(not_in) == len(under_scores)
    else:
        return None
    
#Count number of under scores
# Count number of letters not in my word
# if number of underscores == numbers of letters not in my word
        #return true


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.replace(' ','')
    for other_word in wordlist:
        if match_with_gaps(my_word,other_word) == True:
            print(other_word)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    # import string
    
    word_length = len(secret_word)
    guesses = 6
    warnings = 3
    available = string.ascii_lowercase
    found = False
    memory = []
    print('Welcome to the game Hangman!')
    print()
    print('Hi there (^_^) I\'m thinking of a word that is', word_length,'letters long')
    while guesses > 0:
        print('---'*20)
        print('You have {} warnings left.'.format(warnings))
        print('You have {} guesses to get it right.\n Remember its {} lettered'.format(guesses, word_length))
        print('==='*15)
        print('Available letters:',available)
    
        prompt = 'Please guess a letter: '
        
        def input_warning(warnings, guesses):
            warnings -= 1
            if not warnings+1 > 0:
                guesses -= 1
                warnings = 3
            return warnings, guesses
        
        def print_out():
            print('You have {} warnings left.'.format(warnings))
            print('You have {} guesses to get it right'. format(guesses))
            
        guesses = guesses
        
        is_star = False
        
        while True:
            letters_guessed = str(input(prompt)).lower()
            if letters_guessed == '*':
                is_star = True
                            
            try: 
                if len(letters_guessed) != 1:
                    warnings, guesses = input_warning(warnings,guesses)
                    raise Exception ('Please enter a letter')
                
                elif not type(letters_guessed) is str:
                    warnings, guesses = input_warning(warnings,guesses)
                    raise TypeError('Enter a string object please, you typed in a {} object'.format(type(letters_guessed)))

                else:
                    if not str.isalpha(letters_guessed) and not is_star:
                            warnings, guesses = input_warning(warnings,guesses)
                            raise ValueError('Input is not an alphabet')
                
            except TypeError as te:
                print(te)
                print_out()
                continue
            except Exception as e:
                print(e)
                print_out()
                continue
            except ValueError as ve:
                print(ve)
                print_out()
                continue
            
            if is_star or str.isalpha(letters_guessed):
                r = True
            if len(letters_guessed) == 1 and type(letters_guessed) is str and r:
                break
            
             
        
        def warning_count(memory, letters_guessed, warnings, guesses):
            mem = False
            for a in memory:
                if letters_guessed == a:
                    mem = True
            if mem:
                if warnings+1>0:
                    warnings -= 1
                    print('Oops! you\'ve already guessed that letter, you now have',warnings,'warnings')
                    if warnings == 0:
                        warnings = 3
                        guesses -=1
                        print('You have no warnings left so you lose one guess')
            return warnings,guesses, mem
                    
        #Vowel reduction mark
        def vowels_effect(letter, guesses):
            vowels = ['a','e','i','o','u']
            vowel = False
            for v in vowels:
                if v == letter:
                    vowel = True
                    break
            if vowel:
                guesses -= 1              
            return guesses        
        if not is_star:
            memory_2 = memory[:]
        def check_prescence(secret_word, letters_guessed, guesses, warnings, memory): #check word prescence
            store = []
            for a in secret_word:
                found = False
                if a == letters_guessed:
                    found = True
                store.append(found)
            if sum(store)>0:
                print(letters_guessed, 'is  present in word')
                warnings, guesses, mem = warning_count(memory,letters_guessed,warnings,guesses)
            else:
                print('Oops!', str(letters_guessed), 'is not in my word:', guessed_word)
                
                warnings, guesses, mem = warning_count (memory, letters_guessed, warnings, guesses)
                
                if not mem:
                    guesses -= 1        #Updates number of guesses
                    guesses = vowels_effect(letters_guessed, guesses)
            return guesses, warnings
        
        
        for guess in letters_guessed: #Memory update of letters used
            memory.append(guess)
        
        if not is_star:
            guessed_word = get_guessed_word(secret_word, memory)     
        
            guesses, warnings = check_prescence(secret_word, letters_guessed, guesses, warnings, memory_2)
        if is_star:
            print('Possible word matches are:', show_possible_matches(guessed_word))
        
        print()
        print('letters used: ', memory)
        print("Guessed letter(s) in word")
        print('-------------------------')
        print(guessed_word)
        print();print();
        
        if is_word_guessed(secret_word, memory): #if complete word is found
            found = True
            break
        available = get_available_letters(memory)
        
        def count_distinct(secret_word):  #Number of unique letters
            secret_word = list(secret_word)
            secret_word_copy = secret_word[:]  #create a duplicate
            count_no_dup = []
            for word in secret_word:
                count = []
                match = False
                for w in secret_word_copy:
                    if word == w:
                        match = True
                        count.append(1)
                if match:
                    unique_score = 1/sum(count)
                else:
                    unique_score = 0
                count_no_dup.append(unique_score)
            return round(sum(count_no_dup))
        
        distinct_count = count_distinct(secret_word)
        
    if found:
        print()
        print('<|:)', 'Oh! party scatter, party scatter')
        print("'```'`''`'`'`'`'`'`'`'`'`'`'`'`'`'`''`'")
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('||||||||||||||||||||||||||||||||||||')
        print()
        print("Congratulations!!!, you're a Natural")
        score = guesses*distinct_count
        print('Your total score for this game is:', score)
    else: 
        print()
        print('(T_T)', ':-o')
        print("Ooops! out of guesses. Play again!")
        print("The secret word was:", secret_word)
        
           

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    
    
