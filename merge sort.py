import random
import matplotlib.pyplot as plt

def merge_sort_animation(arr, ax, fig):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_animation(left_half, ax, fig)
    right_half = merge_sort_animation(right_half, ax, fig)

    return merge_animation(left_half, right_half, arr, ax, fig)

def merge_animation(left, right, arr, ax, fig):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Update the original array with sorted values
    for i in range(len(merged)):
        arr[i] = merged[i]

    # Update the plot with the current state of the array
    ax.clear()
    ax.bar(range(len(arr)), arr, color='skyblue')
    fig.canvas.draw()
    plt.pause(0.1)  # Pause to visualize the changes

    return arr

# Generate a random array of 10 elements
random_array = [random.randint(1, 50) for _ in range(10)]

# Set up the plot for animation
fig, ax = plt.subplots()
ax.bar(range(len(random_array)), random_array, color='skyblue')

# Sort the array using merge sort with animation
sorted_array = merge_sort_animation(random_array, ax, fig)

plt.show()
