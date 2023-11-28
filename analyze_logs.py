# analyze_logs.py
import pandas as pd
import matplotlib.pyplot as plt

def load_logs():
    return pd.read_csv('./tictactoe_log.csv', header=None, names=['Mode', 'Winner'])

def generate_statistics(logs):
    #Counting wins per player
    win_counts = logs['Winner'].value_counts()

    #Bar chart of wins
    plt.bar(win_counts.index, win_counts.values)
    plt.title('Wins per Player')
    plt.xlabel('Player')
    plt.ylabel('Number of Wins')
    plt.savefig('wins_per_player.png')  # Save the plot as an image file
    plt.show()
    


if __name__ == '__main__':
    logs_data = load_logs()
    generate_statistics(logs_data)
