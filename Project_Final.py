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