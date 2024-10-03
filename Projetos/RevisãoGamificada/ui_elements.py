import tkinter as tk

def create_label(root, text, row, column, font, colspan=1):
    label = tk.Label(root, text=text, font=font)
    label.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=10, pady=10)
    return label

def create_button(root, text, command, row, column, font, colspan=1):
    button = tk.Button(root, text=text, command=command, font=font)
    button.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=10, pady=10)
    return button

def create_radio_buttons(root, options, variable, row, font, colspan=1):
    for i, option in enumerate(options):
        radio_button = tk.Radiobutton(root, text=option, variable=variable, value=option, font=font)
        radio_button.grid(row=row + i, column=1, columnspan=colspan, sticky="nsew", padx=10, pady=10)
