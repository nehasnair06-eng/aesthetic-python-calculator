import customtkinter as ctk
import math


# ---------------- APP SETTINGS ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Calculator")
app.geometry("390x650")
app.resizable(False, False)


# ---------------- COLORS ----------------

BG = "#0F1117"
DISPLAY = "#181B24"
BUTTON = "#222631"
BUTTON_HOVER = "#2C3140"
PURPLE = "#9B7EDE"
PINK = "#E58BAE"
TEXT = "#F5F5F7"
SECONDARY = "#9CA3AF"


# ---------------- VARIABLES ----------------

expression = ""


# ---------------- FUNCTIONS ----------------

def press(value):
    global expression

    expression += value
    display.configure(text=expression)


def clear():
    global expression

    expression = ""
    display.configure(text="0")


def backspace():
    global expression

    expression = expression[:-1]

    if expression:
        display.configure(text=expression)
    else:
        display.configure(text="0")


def calculate():
    global expression

    try:
        exp = expression.replace("×", "*")
        exp = exp.replace("÷", "/")

        result = eval(exp)

        expression = str(result)
        display.configure(text=expression)

    except ZeroDivisionError:
        expression = ""
        display.configure(text="Cannot divide by 0")

    except:
        expression = ""
        display.configure(text="Error")


def square_root():
    global expression

    try:
        value = float(expression)
        result = math.sqrt(value)

        expression = str(result)
        display.configure(text=expression)

    except:
        expression = ""
        display.configure(text="Error")


def percentage():
    global expression

    try:
        value = float(expression)
        result = value / 100

        expression = str(result)
        display.configure(text=expression)

    except:
        expression = ""
        display.configure(text="Error")


# ---------------- HEADER ----------------

header = ctk.CTkLabel(
    app,
    text="CALCULATOR",
    font=("Segoe UI", 13, "bold"),
    text_color=SECONDARY
)

header.pack(
    pady=(25, 5)
)


# ---------------- DISPLAY ----------------

display_frame = ctk.CTkFrame(
    app,
    width=350,
    height=130,
    corner_radius=25,
    fg_color=DISPLAY
)

display_frame.pack(
    padx=20,
    pady=(10, 20)
)

display_frame.pack_propagate(False)


display = ctk.CTkLabel(
    display_frame,
    text="0",
    font=("Segoe UI", 38, "bold"),
    text_color=TEXT,
    anchor="e"
)

display.pack(
    fill="both",
    expand=True,
    padx=20
)


# ---------------- BUTTON FRAME ----------------

buttons = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

buttons.pack(
    padx=20
)


# ---------------- BUTTON FUNCTION ----------------

def create_button(
    text,
    row,
    column,
    command,
    color=BUTTON,
    hover=BUTTON_HOVER
):

    button = ctk.CTkButton(
        buttons,
        text=text,
        command=command,
        width=75,
        height=65,
        corner_radius=22,
        font=("Segoe UI", 20, "bold"),
        fg_color=color,
        hover_color=hover,
        text_color=TEXT
    )

    button.grid(
        row=row,
        column=column,
        padx=6,
        pady=6
    )


# ---------------- ROW 1 ----------------

create_button(
    "AC",
    0, 0,
    clear,
    color="#343846"
)

create_button(
    "⌫",
    0, 1,
    backspace,
    color="#343846"
)

create_button(
    "%",
    0, 2,
    percentage,
    color="#343846"
)

create_button(
    "÷",
    0, 3,
    lambda: press("÷"),
    color=PURPLE,
    hover="#AE91F0"
)


# ---------------- ROW 2 ----------------

create_button(
    "7",
    1, 0,
    lambda: press("7")
)

create_button(
    "8",
    1, 1,
    lambda: press("8")
)

create_button(
    "9",
    1, 2,
    lambda: press("9")
)

create_button(
    "×",
    1, 3,
    lambda: press("×"),
    color=PURPLE,
    hover="#AE91F0"
)


# ---------------- ROW 3 ----------------

create_button(
    "4",
    2, 0,
    lambda: press("4")
)

create_button(
    "5",
    2, 1,
    lambda: press("5")
)

create_button(
    "6",
    2, 2,
    lambda: press("6")
)

create_button(
    "-",
    2, 3,
    lambda: press("-"),
    color=PURPLE,
    hover="#AE91F0"
)


# ---------------- ROW 4 ----------------

create_button(
    "1",
    3, 0,
    lambda: press("1")
)

create_button(
    "2",
    3, 1,
    lambda: press("2")
)

create_button(
    "3",
    3, 2,
    lambda: press("3")
)

create_button(
    "+",
    3, 3,
    lambda: press("+"),
    color=PURPLE,
    hover="#AE91F0"
)


# ---------------- ROW 5 ----------------

create_button(
    "√",
    4, 0,
    square_root,
    color="#343846"
)

create_button(
    "0",
    4, 1,
    lambda: press("0")
)

create_button(
    ".",
    4, 2,
    lambda: press(".")
)

create_button(
    "=",
    4, 3,
    calculate,
    color=PINK,
    hover="#F09DBB"
)


# ---------------- KEYBOARD ----------------

def keyboard(event):

    key = event.keysym

    if event.char in "0123456789.+-*/()":
        press(event.char)

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()


app.bind("<Key>", keyboard)


# ---------------- RUN ----------------

app.mainloop()