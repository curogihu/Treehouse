if __name__ == "__main__":
    import csv
    import math

    def extract_keyword_soccer_players(p_f, keyword):
        reader = csv.reader(p_f)
        p_f.seek(0)                 # for dealing with re-read the csv file
        header = next(reader)       # skip header line
        players_list = []

        for player in reader:
            if player[2] == keyword:
                players_list.append(player)

        return players_list

    with open('soccer_players.csv', 'r') as f_read_csv:
        experience_players = extract_keyword_soccer_players(f_read_csv, 'YES')
        no_experience_players = extract_keyword_soccer_players(f_read_csv, 'NO')

# Dragons, Sharks and Raptors.

    teams = ['Dragons', 'Sharks', 'Raptors']

    with open('teams.txt', 'w') as f_txt:
        for i, (experience_player, no_experience_player) in enumerate(zip(experience_players, no_experience_players)):

            # team have six players, three have soccer experience, the last have no experience.
            if i % 3 == 0:
                f_txt.write(teams[math.floor(i / 3)] + '\n')

            f_txt.write(('{}, {}, {} and {}\n'.format(*experience_player)))
            f_txt.write(('{}, {}, {} and {}\n'.format(*no_experience_player)))

            # add new line to improve readability
            if i % 3 == 2:
                f_txt.write('\n')
