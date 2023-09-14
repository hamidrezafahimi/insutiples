import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2,3,4,5,6,7]
win = [2,3,4,5,6,7,8,9]
loop = [3,2,4,6,5,8,8,9]
lose = [1,2,4,7,5,3,8,5]
eps = [0.02,0.04,0.08,0.06,0.03,0.07,0.06,0.04]
score = [90,80,70,60,50,40,30,20]

fig=plt.figure()
ax=fig.add_subplot(111, label="1")
ax2=fig.add_subplot(111, label="2", frame_on=False)

ax2.yaxis.tick_right()
ax2.set_ylabel('Score', color='blue')
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='y', colors='blue')

plt.grid(True)

def plotLearning(x, win_rate, loop_rate, lose_rate, epsilons, avg_scores):

    ax.plot(x, win_rate, label="Win Rate", color='green')
    ax.plot(x, loop_rate, label="Loop Rate", color='yellow')
    ax.plot(x, lose_rate, label="Lose Rate", color='red')
    ax.plot(x, np.array(epsilons)*100, label="epsilon", color='black')
    ax.set_xlabel("Game Number")
    
    ax.legend()
    
    ax2.plot(x, avg_scores, color='blue', label="p")
    plt.show()


if __name__ == '__main__':
    
    plotLearning(x, win, loop, lose, eps, score)