import json

def stats(player1_pairs, player2_pairs, first_record):
    '''Records game stats externally in JSON format.'''
    try:
        filename = 'stats.json'
        with open(filename) as f:
            stats = json.load(f)
    except FileNotFoundError:
        filename = 'stats.json'
        with open(filename, 'w') as f:
            json.dump(first_record, f)
    else:
        if len(player1_pairs) > len(player2_pairs):
            stats["Player1"]+=1
        elif len(player2_pairs) > len(player1_pairs):
            stats["Player2"]+=1
        else:
            stats["Draws"]+=1
        filename = 'stats.json'
        with open(filename, 'w') as f:
            json.dump(stats, f)