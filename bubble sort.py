import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def bubble_sort_animation(data):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Animation")

    rects = ax.bar(range(len(data)), data, color='#FFB7CE')

    def update(frame):
        for rect, height in zip(rects, frame):
            rect.set_height(height)
        return rects

    ani = animation.FuncAnimation(fig, update, frames=bubble_sort_frames(data), blit=True, repeat=False)
    plt.show()


def bubble_sort_frames(data):
    n = len(data)
    frames = []

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                frames.append(data.copy())

    return frames


# Example usage:
my_data = np.random.randint(1, 50, 10)
bubble_sort_animation(my_data)
