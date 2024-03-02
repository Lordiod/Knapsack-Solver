import customtkinter
from tkinter import messagebox

#------------------------------------------{0/1 knapsack solver}------------------------------------------#

def solve_01_knapsack(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    total_value = dp[n][capacity]
    w = capacity
    for i in range(n, 0, -1):
        if total_value <= 0:
            break
        if total_value == dp[i - 1][w]:
            continue
        else:
            selected_items.append(i - 1)
            total_value -= values[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], total_value, selected_items

#------------------------------------------{Fractional knapsack solver}------------------------------------------#

def solve_fractional_knapsack(capacity, weights, values, n):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    max_value = 0
    total_value = 0

    for weight, value in items:
        if capacity >= weight:
            max_value += value
            total_value += value
            capacity -= weight
        else:
            fraction = value / weight
            max_value += fraction * capacity
            total_value += fraction * capacity
            break

    return max_value, total_value

#------------------------------------------{ knapsack Calculator}------------------------------------------#

def calculate_knapsack(fractional):
    
    try:
        capacity = int(capacity_entry.get())
        weights = list(map(int, weight_entry.get().split(',')))
        values = list(map(int, value_entry.get().split(',')))

        if len(weights) != len(values):
            messagebox.showerror("Error", "Please import the same amount of values and weights")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return

    n = len(weights)

    
    if fractional:
        max_value , total_value = solve_fractional_knapsack(capacity, weights, values, n)
        selected_items = None
    else:
        max_value, total_value, selected_items = solve_01_knapsack(capacity, weights, values, n)

    
    if fractional:
        output_label.configure(text="Maximum Value: " + str(max_value) + "\nTotal Value: " + str(total_value))
    else:
        output_label.configure(text="Maximum Value: " + str(max_value) + "\nSelected Items: " + str([selected_items[i] +[1, 1][i % 2] for i in range(len(selected_items))]))

#------------------------------------------{GUI}------------------------------------------#

window = customtkinter.CTk()
window.title("Knapsack Problem")
window.geometry("400x350")
window.resizable(False, False)

capacity_label = customtkinter.CTkLabel(window, text="Capacity:")
capacity_label.pack()
capacity_entry = customtkinter.CTkEntry(window)
capacity_entry.pack()

weight_label = customtkinter.CTkLabel(window, text="Weights (comma-separated):")
weight_label.pack()
weight_entry = customtkinter.CTkEntry(window)
weight_entry.pack()

value_label = customtkinter.CTkLabel(window, text="Values (comma-separated):")
value_label.pack()
value_entry = customtkinter.CTkEntry(window)
value_entry.pack()

knapsack_01_button = customtkinter.CTkButton(window, text="Calculate 0/1 Knapsack",command=lambda: calculate_knapsack(False))
knapsack_01_button.pack()

fractional_button = customtkinter.CTkButton(window, text="Calculate Fractional Knapsack",command=lambda: calculate_knapsack(True))
fractional_button.pack()

output_label = customtkinter.CTkLabel(window, text="")
output_label.pack()

window.mainloop()