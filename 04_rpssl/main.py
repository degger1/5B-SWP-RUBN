import random
import json


def choose_player_input():
    while (True):
        print("\n" + "-" * 25)
        print("Rock..........0")
        print("Lizard........1")
        print("Spock.........2")
        print("Scissors......3")
        print("Paper.........4")
        print("Choose!")
        my_in = input()

        try:
            ret_choice_player = int(my_in)
        except ValueError:
            print("incorrect input")
        else:
            if ret_choice_player >= 0 and ret_choice_player <= 4:
                return ret_choice_player
            else:
                print("incorrect input")


def convert_to_str(n):
    """
        Rock..........0
        Lizard........1
        Spock.........2
        Scissors......3
        Paper.........4
    """

    # wer python version < 3.10 verwendet, hat pech :(
    match n:
        case 0:
            return 'rock'

        case 1:
            return 'lizard'

        case 2:
            return 'spock'

        case 3:
            return 'scissors'

        case 4:
            return 'paper'


def compare(pl, ai):
    if pl == 'scissors' and ai == 'paper':
        return 'player'
    elif ai == 'scissors' and pl == 'paper':
        return 'ai'

    elif pl == 'paper' and ai == 'rock':
        return 'player'
    elif ai == 'paper' and pl == 'rock':
        return 'ai'

    elif pl == 'rock' and ai == 'lizard':
        return 'player'
    elif ai == 'rock' and pl == 'lizard':
        return 'ai'

    elif pl == 'lizard' and ai == 'spock':
        return 'player'
    elif ai == 'lizard' and pl == 'spock':
        return 'ai'

    elif pl == 'spock' and ai == 'scissors':
        return 'player'
    elif ai == 'spock' and pl == 'scissors':
        return 'ai'

    elif pl == 'scissors' and ai == 'lizard':
        return 'player'
    elif ai == 'scissors' and pl == 'lizard':
        return 'ai'

    elif pl == 'lizard' and ai == 'paper':
        return 'player'
    elif ai == 'lizard' and pl == 'paper':
        return 'ai'

    elif pl == 'paper' and ai == 'spock':
        return 'player'
    elif ai == 'paper' and pl == 'spock':
        return 'ai'

    elif pl == 'spock' and ai == 'rock':
        return 'player'
    elif ai == 'spock' and pl == 'rock':
        return 'ai'

    elif pl == 'rock' and ai == 'scissors':
        return 'player'
    elif ai == 'rock' and pl == 'scissors':
        return 'ai'

    return 'draw'


def ask_continue_playing():
    while (True):
        print("\ncontinue playing?")
        print("Yes...........y")
        print("No............n")
        my_in = input()

        if my_in == 'y':
            return True
        elif my_in == 'n':
            return False
        else:
            print("incorrect input")


def save_stats(my_dictionary, name):
    with open('./data/' + name + '.json', 'w') as outfile:
        json.dump(my_dictionary, outfile)


def load_stats(name):
    try:
        with open('./data/' + name + '.json', 'r') as outfile:
            json_str = outfile.read()
            return json.loads(json_str)
    except FileNotFoundError:
        return None


def load_dictionaries():
    prev_w = load_stats('win_dict')
    prev_p = load_stats('player_symbol_dict')
    prev_a = load_stats('ai_symbol_dict')

    if (prev_w is None):
        wins = {'draw': 0, 'player': 0, 'ai': 0}
    else:
        wins = prev_w

    if (prev_a is None):
        p_symb = {'rock': 0, 'lizard': 0, 'spock': 0, 'scissors': 0, 'paper': 0}
    else:
        p_symb = prev_p

    if (prev_a is None):
        ai_symb = {'rock': 0, 'lizard': 0, 'spock': 0, 'scissors': 0, 'paper': 0}
    else:
        ai_symb = prev_a

    return wins, p_symb, ai_symb


def main_menu_input():
    while (True):
        print("\n" + "-" * 25)
        print("RPSSL.........0")
        print("Statistics....1")
        print("Quit..........9")
        print("Choose!")
        my_in = input()

        try:
            menu_select = int(my_in)
        except ValueError:
            print("incorrect input")
        else:
            if menu_select == 0:
                return 'RPSSL'

            elif menu_select == 1:
                return 'statistics'

            elif menu_select == 9:
                return 'quit'

            else:
                print("incorrect input")

    return menu_select


def show_statistics(win, pl_s, ai_s):
    print("\n" + "-" * 25)
    print("Wins Statistics:")
    for w in win:
        print(w + "..........." + str(win[w]))

    print("\nPlayer Choice Statistics:")
    for p in pl_s:
        print(p + "..........." + str(pl_s[p]))

    print("\nAI Choice Statistics:")
    for a in ai_s:
        print(a + "..........." + str(ai_s[a]))


def main():
    # ------------------------------------------------------------------------------------------------- #
    # LOAD STATISTICS
    win_dict, player_symbol_dict, ai_symbol_dict = load_dictionaries()

    # ------------------------------------------------------------------------------------------------- #
    # MAIN MENU
    while True:
        main_menu_option = main_menu_input()

        # ------------------------------------------------------------------------------------------------- #
        # RPSSL GAME
        if main_menu_option == 'RPSSL':
            continue_playing = True
            while continue_playing:
                player_choice = convert_to_str(choose_player_input())
                ai_choice = convert_to_str(random.randint(0, 4))

                player_symbol_dict[player_choice] = player_symbol_dict[player_choice] + 1
                ai_symbol_dict[ai_choice] = ai_symbol_dict[ai_choice] + 1

                res = compare(player_choice, ai_choice)
                win_dict[res] = win_dict[res] + 1

                print('\n' + player_choice + ' --- ' + ai_choice)
                print(res + " wins!\n")

                continue_playing = ask_continue_playing()

            # json saving deactivated for sqlite
            # save_stats(player_symbol_dict, 'player_symbol_dict')
            # save_stats(ai_symbol_dict, 'ai_symbol_dict')
            # save_stats(win_dict, 'win_dict')

        # ------------------------------------------------------------------------------------------------- #
        # STATISTICS
        if main_menu_option == 'statistics':
            show_statistics(win_dict, player_symbol_dict, ai_symbol_dict)

        # ------------------------------------------------------------------------------------------------- #
        # QUIT
        if main_menu_option == 'quit':
            url = 'http://127.0.0.1:5000/postPlayerChoice'
            query = player_symbol_dict
            requests.post(url, data=query)
            break

    print("\n" + "=" * 25)
    print("END OF PROGRAMM")


if __name__ == '__main__':
    main()
