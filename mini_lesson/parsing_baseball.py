import argparse

def parse_argument():
    """
    Takes in the name of a baseball player.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--player', required=True, choices=["babe_ruth", "mickey_mantle",
        "lou_gehrig"], help="Name of the player whose stats you'd like to retrieve.")
    args = parser.parse_args()
    player = args.player
    return player

def retrieve_stats(player):
    babe_ruth = {"BA" : .342, "RBIs" : 2213, "GP" : 2503}
    mickey_mantle = {"BA" : .298, "RBIs" : 1509, "GP" : 2401}
    lou_gehrig = {"BA" : .340, "RBIs" : 1995, "GP" : 2164}
    if player == "babe_ruth":
        return babe_ruth
    elif player == "mickey_mantle":
        return mickey_mantle
    elif player == "lou_gehrig":
        return lou_gehrig

def pretty_print(player_stats):
    print ("Batting Average = " + str(player_stats["BA"]))
    print ("Runs Batted In = " + str(player_stats["RBIs"]))
    print ("Career Games Played = " + str(player_stats["GP"]))

def main():
    player = parse_argument()
    player_stats = retrieve_stats(player)
    pretty_print(player_stats)

if __name__ == "__main__":
    main()