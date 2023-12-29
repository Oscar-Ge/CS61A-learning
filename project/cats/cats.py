"""Typing test implementation"""

from optparse import HelpFormatter
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    k1=k
    for i in range(len(paragraphs)):
        if k1==0 and select(paragraphs[i]):
            return paragraphs[i]
        elif select(paragraphs[i]):
            k1-=1
    return ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def helper(topics):
        a=remove_punctuation(topics)
        c=lower(a)
        b=split(c)
        for j in range(len(topic)):
            for k in range(len(b)):
                if b[k]==topic[j]:
                    return True
        return False    
    return helper
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    ans=0
    len_typed=len(typed_words)
    len_reference=len(reference_words)
    if len_typed==0 or len_reference==0:
        return 0.0
    else:
        leng=min(len_typed, len_reference)
        for i in range(leng):
            if typed_words[i]==reference_words[i]:
                ans+=1
        return ans/len_typed*100.0


    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    mint=elapsed/60
    lent=len(typed)/5
    return lent/mint
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    mini=diff_function(user_word, valid_words[0], limit)
    ans=0
    for i in range(len(valid_words)):
        if valid_words[i]==user_word:
            return valid_words[i]
        else:
            if diff_function(user_word, valid_words[i], limit) < mini:
                mini=diff_function(user_word, valid_words[i], limit)
                ans=i
    if mini<=limit:
        return valid_words[ans]
    else:
        return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    lens=len(start)
    leng=len(goal)
    mini=min(lens, leng)
    diff=abs(lens-leng)
    def helper(dif, i=0):
        if i==mini:
            return dif
        if dif>limit:
            return dif
        if start[i]!=goal[i]:
            dif+=1
        i+=1
        return helper(dif, i)
    return helper(diff)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    '''def helper(s, g, ans=0):
        if ans>limit:
            return ans
        ans1=ans
        for i in range(g, len(goal)):
            if start(s)==goal(i):
                s1=s
                i1=i
                while True:
                    s1+=1
                    i1+=1
                    if s1==len(start) or i1==len(goal):
                    if start(s1)!=goal(i1):
                        ans+=abs(s-i)
                        s=s1+1
                        i=i1+1
                        break
        if ans1-ans==0:
            s+=1
        return(s, g, )'''
    # If the length difference is greater than the limit, return a large number
    if abs(len(start) - len(goal)) > limit:
        return float('inf')
    # Create a 2D array to store the minimum edit distances
    dp = [[0] * (len(goal) + 1) for _ in range(len(start) + 1)]
    # Initialize the first row and column
    for i in range(len(start) + 1):
        dp[i][0] = i
    for j in range(len(goal) + 1):
        dp[0][j] = j
    # Fill in the DP table
    for i in range(1, len(start) + 1):
        for j in range(1, len(goal) + 1):
            if start[i - 1] == goal[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Remove
                                  dp[i][j - 1],      # Add
                                  dp[i - 1][j - 1])  # Substitute
            if dp[i][j] > limit:
                return float('inf')
    # The minimum edit distance is at the bottom-right cell
    return dp[len(start)][len(goal)]




def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    ans=0
    for i in range(len(prompt)):
        if i==len(typed):
            break
        if typed[i]!=prompt[i]:
            break
        else:
            ans+=1
    progress=ans/len(prompt)
    d={'id': user_id, 'progress': progress}
    send(d)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times=[[0 for i in range(len(times_per_player[0])-1)] for j in range(len(times_per_player))]
    for i in range(len(times_per_player)):
        for j in range(len(times_per_player[i])-1):
            times[i][j]=times_per_player[i][j+1]-times_per_player[i][j]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    ans=[[] for i in range(len(player_indices))]
    for i in word_indices:
        wd=word_at(game, i)
        an=0
        temp=time(game, 0, i)
        for j in player_indices:
            if time(game, j, i)<temp:
                temp=time(game, j, i)
                an=j
        ans[an].append(wd)
    return ans
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)