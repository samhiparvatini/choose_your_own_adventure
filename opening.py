import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Choose Your Own Adventure!")
root.geometry("800x400")

# Create a label
label = tk.Label(root, text="You wake up in an abandoned asylum with no recollection of how you got there.\n Can you find your way out before the vengeful spirits or a bloodthirsty murderer catches you?", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Let's Start", command=on_button_click)
button.pack(pady=20)

# Run the main loop
root.mainloop()