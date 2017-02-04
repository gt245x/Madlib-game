#quizzes for the three game option.
easy_game = '''The basketball team located in __1__ has won 17 NBA championship, the
most of any team. On March 2, 1962, this NBA hall of famer __2__ scored 100 points in
one game which is the most one player has scored in one game. This player __3__ has
scored more points in the playoffs than any other player. Most blocked shots in NBA history
belongs to __4__. The country to win the first Olympic Gold medal in basketball was __5__.
Basketball became an Olympic sport in the year __6__. A basketball hoop is __7__ feet from the ground'''

medium_game = '''__1__ is a widely used high-level, general-purpose, interpreted, dynamic programming language.
It was conceived in the late 1980s and its implementation begain in 1989 by __2__, it's principal author.
Some python expressions are similar to languages such as C and Java while some are not. Pythin uses "and", "or",
"not" for its __3__ operators rather than the symbolic '&&', '||', and '!' used in Java and C. Some of python
statement expression include __4__ which defines a function or method and the __5__ statement, which executes
over an iterable object, capturing each element to a local variable for use by the attached block'''

hard_game = '''NASA was created in response to the Soviet Union launch of its first satellite,
__1__ 1 in 1957. Project __2__ was the first human spaceflight of the United States running from 1958 through
1963 and John Glenn became the first American to circle the earth making three orbits.
On July 20, 1969, the Apollo Lunar Module with Neil Armstrong and __3__ landed on the lunar surface.The only
astronaut to ever hit golf on the moon is __4__. Six total space shuttle orbiters built by the United States
are Enterprise, Columbia, Challenger, Discovery, Atlantis and __5__. In 2012, __6__ a car
sized robotic rover landed on target on Mars'''



#The answers to the question in a list
answer_easygame = ['boston','wilt chamberlain','michael jordan','hakeem olajuwon','usa','1936','10']
answer_mediumgame = ['python','guido van rossum','boolean','def','for']
answer_hardgame = ['sputnik','mercury','buzz aldrin','alan shepard','endeavour','curiosity']

#use of dictionary to access the question and answers
game_level_templates = {"easy" : easy_game, "medium" : medium_game, "hard": hard_game}
games = {"easy" : answer_easygame, "medium" : answer_mediumgame, "hard" : answer_hardgame }
MAX_NUMBER_OF_GUESSES = 5   #maxium number of guesses for each question


# Method to ask user of gamelevel to play
def game_level():
    user_input = raw_input("Possible choices include easy, medium, and hard. Make a choice:  ")
    user_input = user_input.strip()
    while True:
        if user_input in ("easy", "medium", "hard"):
            return user_input
        else:
            print user_input + " is not an option. Choices include easy, medium or hard."
            user_input = raw_input("Please try again   ")

# Function replaces the question in the quiz with the correct answer
def replace(string,blank_space,game_answer,q):
    i = 0
    while i <= q:
        replaced = string.replace(blank_space[i],game_answer[i])
        i += 1
        string = replaced
    print string

#Function check users answer input with the correct answer
def check_answer(game_level_value, answer_input,q):
    game_answer_list = games[game_level_value]
    game_correct_answer = game_answer_list[q]
    answer_input = answer_input.strip()
    return answer_input.lower() != game_correct_answer




# playgame method to confirm users answers for each question.
def play_game():
    print "Howdy, welcome to Udacity playgame. Please select a game difficulty by typing it in!"
    game_level_value = game_level()


    q = 0 #question number
    print game_level_templates[game_level_value]
    game_answer_list = games[game_level_value]
    len_game_answer_list = len(game_answer_list)
    number_of_guesses = 0
    while q < len_game_answer_list:
        number_of_guesses = 0
        while number_of_guesses < MAX_NUMBER_OF_GUESSES:
            answer_input = raw_input("What should be substituted for _" + str(q + 1) + "_?  ")
            if check_answer(game_level_value, answer_input,q) == True:
                number_of_guesses = number_of_guesses + 1
                if number_of_guesses == MAX_NUMBER_OF_GUESSES:
                    print "You suck dude! Program terminates"
                    return
                else:
                    print "You made a mistake, try again. You have " + str(MAX_NUMBER_OF_GUESSES - number_of_guesses) + " chances left"
            else:
                print "Correct"
                replace((game_level_templates[game_level_value]),blank_space,game_answer_list,q)
                q += 1
                break
    print "You correctly answered all the questions"

play_game()