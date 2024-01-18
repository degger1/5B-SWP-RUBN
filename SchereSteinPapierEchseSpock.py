"""
https://bigbangtheory.fandom.com/de/wiki/Stein,_Papier,_Schere,_Echse,_Spock
http://www.samkass.com/theories/RPSSL.html

1) Implement the game in the console                                 ✅
2) Computer vs. Player mode                                           ✅
3) Count wins for each symbol                                         ✅
4) Count total occurrences of each symbol                              ✅
5) Persist data storage options                                       ✅
6) Offer a menu for games, statistics                                 ✅

Logic:
    Rock (0) beats Lizard (3) and Scissors (4)
    Spock (1) beats Scissors (4) and Rock (0)
    Paper (2) beats Rock (0) and Spock (1)
    Lizard (3) beats Spock (1) and Paper (2)
    Scissors (4) beats Paper (2) and Lizard (3)


    => Player loses when:
    1: Rock (0) - Lizard (3) || Scissors (4) => -3 || -4 mod 5 => 2 || 1
    2: Spock (1) - Scissors (4) || Rock (0) => -3 || 1 mod 5 => 2 || 1
    3: Paper (2) - Rock (0) || Spock (1) => 2 || 1 mod 5 => 2 || 1
    => Player wins if (player_choice - cpu_choice) mod 5 = 3 || 4
    => Tie, if (player_choice - cpu_choice) mod 5 = 0

    0 - Rock
    1 - Spock
    2 - Paper
    3 - Lizard
    4 - Scissors

"""
import random


def name_to_number(name):
    return {'stein': 0, 'spock': 1, 'papier': 2, 'echse': 3, 'schere': 4}.get(name, "ERROR Name")


def number_to_name(number):
    return {0: 'stein', 1: 'spock', 2: 'papier', 3: 'echse', 4: 'schere'}.get(number, "ERROR Number")


def load_statistics(filename):
    stats = {'stein': 0, 'spock': 0, 'papier': 0, 'echse': 0, 'schere': 0}
    try:
        with open(filename, "r") as file:
            for line in file:
                choice, count = line.split(": ")
                if choice in stats:
                    stats[choice] = int(count)
    except FileNotFoundError:
        print(f"Keine existierende Datei wurde gefunden. Es wurde eine neue erstellt: {filename}")
    return stats


def update_statistics(choice, stats):
    if choice in stats:
        stats[choice] += 1


def save_statistics(stats, filename):
    with open(filename, "w") as file:
        for choice, count in stats.items():
            file.write(f"{choice}: {count}\n")


# Main game function
def game(player_choice, cpu_win_count, player_win_count, draw, stats):
    print(f"Ihre Wahl: {player_choice}")
    update_statistics(player_choice, stats)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print(f"Computer Wahl: {comp_choice}")
    difference = (player_number - comp_number) % 5
    if difference == 1 or difference == 2:
        print("Computer gewinnt!")
        cpu_win_count += 1
    elif difference == 3 or difference == 4:
        print("Sie gewinnen!")
        player_win_count += 1
    else:
        print("Unentschieden!")
        draw += 1
    return cpu_win_count, player_win_count, draw


def main():
    stats_filename = 'stats.txt'
    stats = load_statistics(stats_filename)
    cpu_win_count, player_win_count, draw = 0, 0, 0

    while True:
        print("\nMENU\n"
              "1. Gegen Computer antreten\n"
              "2. Statistik anzeigen\n"
              "3. Verlassen\n")
        choice = input("Was möchten Sie machen? (1-3)").strip()

        if choice == '1':
            while True:
                play_again = input('Wollen Sie starten? [j/n]: ').strip().lower()
                if play_again == 'j':
                    player_choice = input('Wähle "Stein", "Papier", "Schere", "Echse", oder "Spock": ').strip().lower()
                    if player_choice in ['stein', 'papier', 'schere', 'echse', 'spock']:
                        cpu_win_count, player_win_count, draw = game(player_choice, cpu_win_count, player_win_count,
                                                                     draw, stats)

                    else:
                        print("Ungültige Eingabe!")
                elif play_again == 'n':
                    break
                else:
                    print('Ungültige Eingabe!')
        elif choice == '2':
            print("\nStatistik:")
            for choice, count in stats.items():
                print(f"{choice}: {count}")
        elif choice == '3':
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie zwischen 1, 2, oder 3 aus")

    save_statistics(stats, stats_filename)
    print(f"\nSpielzusammenfassung: Cpu Siege: {cpu_win_count}, Ihre Siege: {player_win_count}, Unentschieden: {draw}")


if __name__ == "__main__":
    main()