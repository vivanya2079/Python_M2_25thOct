import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Label Configuration")

# Create a Label widget with a red background and custom font
label = tk.Label(root, text="Sample Label", bg="red", font=("Times New Roman", 18))

# Pack the Label widget to display it in the window
label.pack()

# Start the GUI event loop
root.mainloop()
