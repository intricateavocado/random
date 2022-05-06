#libraries
import random
import string
import time
from words import words

def hangman():
    global lives
    lives = 0
    def word_selection(words):
        global lives
        c = False #loop variable
        while c == False:
            difficulty_level = input("Pick a difficulty level. 'Easy', 'medium', or 'hard'. Enter choice: ").upper()
            if difficulty_level == 'EASY':
                word = random.choice(words) #chooses word
                word = word.upper()
                while '-' in word or ' ' in word or len(word) > 5:
                    word = random.choice(words)
                    word = word.upper()
                lives = 10
                #validates that word is usable
                c = True
            elif difficulty_level == 'MEDIUM':
                word = random.choice(words) #chooses word
                word = word.upper()
                while '-' in word or ' ' in word or len(word) < 5 or len(word) > 8:
                    word = random.choice(words)
                    word = word.upper()
                lives = 8
                #validates that word is usable
                c = True
            elif difficulty_level == 'HARD':
                word = random.choice(words) #chooses word
                word = word.upper()
                while '-' in word or ' ' in word or len(word) < 8:
                    word = random.choice(words)
                    word = word.upper()
                lives = 6
                #validates that word is usable
                c = True
            else:
                print(f"The word {difficulty_level.lower} is not an option. Please try again.")
                c = False
        return word
    word_select = word_selection(words)
    word = word_select
    word_letters = set(word) #creates a set of the letters in the word
    alphabet = set(string.ascii_uppercase) 
    #creates an alphabet for valid english letters
    used_letters = set() #empty set for used letters
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        user_letter = input("Enter a letter: ").upper()
        if user_letter in alphabet - used_letters:
          #if the inputted letter is valid and not already used, make it used
            if user_letter in  word_letters:
                used_letters.add(user_letter)
                word_letters.remove(user_letter)
                #remove the letter from the letters in the word
            elif user_letter in used_letters:
                print("Invalid guess. Letter has already been used.")
            else:
                used_letters.add(user_letter)
                lives -= 1
                print(f"The word does not contain that letter. You have {lives} left.")
    word_list = [letter if letter in used_letters else '-' for letter in word]
    win = False
    if lives > 0:
        print("You got it! The word was ", word, ".")
        win = True
    else:
        print("You died! The word was ", word,". Better luck next time.")
        win = False
    if win == True:
        print("Great job! Play again?")
    else:
        print("Try again?")
    play_again = input("Y or N: ").upper()
    if play_again == 'Y':
        hangman()


def hangmantimed():
    def word_selection(words):
        global lives
        c = False #loop variable
        while c == False:
            difficulty_level = input("Pick a difficulty level. 'Easy', 'medium', or 'hard'. Enter choice: ").upper()
            if difficulty_level == 'EASY':
                word = random.choice(words) #chooses word
                word = word.upper()
                while '-' in word or ' ' in word or len(word) > 5:
                    word = random.choice(words)
                    word = word.upper()
                lives = 10
                #validates that word is usable
                c = True
            elif difficulty_level == 'MEDIUM':
                word = random.choice(words) #chooses word
                word = word.upper()
                while '-' in word or ' ' in word or len(word) < 5 or len(word) > 8:
                    word = random.choice(words)
                    word = word.upper()
                lives = 8
                #validates that word is usable
                c = True
            elif difficulty_level == 'HARD':
                word = random.choice(words) #chooses word
                word = word.upper()
                while '-' in word or ' ' in word or len(word) < 8:
                    word = random.choice(words)
                    word = word.upper()
                lives = 6
                #validates that word is usable
                c = True
            else:
                print(f"The word {difficulty_level.lower} is not an option. Please try again.")
                c = False
        return word
    t0 = time.time()
    word = word_selection(words)
    word_letters = set(word) #creates a set of the letters in the word
    alphabet = set(string.ascii_uppercase) #creates an alphabet for valid english letters
    used_letters = set() #empty set for used letters
    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        user_letter = input("Enter a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            #if the inputted letter is valid and not already used, make it used
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                #remove the letter from the letters in the word
            elif user_letter in used_letters:
                print("Invalid guess. Letter has already been used.")
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("You got it! The word was: ", ''.join(word_list))
    new_fastest = False
    game_time = int(time.time() - t0)
    all_game_times = [999]
    best_score_prev = min(all_game_times)
    all_game_times.append(game_time)
    best_score = min(all_game_times)
    if best_score_prev == 999:
        #first game
        print(f"It took {len(used_letters)} guesses and {game_time} seconds to guess the word.")
        firstgame = True
    if game_time < best_score_prev and firstgame == False:
        #if faster
        beat_by = best_score_prev - game_time #by how much
        new_fastest = True
    if new_fastest == True:
        print(f"Your time was {game_time} seconds.")
        print(f"You have the new fastest time! You beat the previous best time by {beat_by} seconds.")
    elif new_fastest == False and firstgame == False:
        lost_by = game_time - best_score_prev
        print(f"Your time was {game_time} seconds.")
        print(f"The fastest time is {best_score} seconds. You were {lost_by} seconds away from beating it.")
    if new_fastest == True:
        print("Great job! Even faster?")
        firstgame = False
    else:
        print("Try again?")
        firstgame = False
    play_again = input("Y or N: ").upper()
    if play_again == 'Y':
        hangmantimed()
