from tkinter import *

def select_best_candidate():
    pass

BACKGROUND_COLOR = "#AEADF0"

window = Tk()
window.title("Decision Making")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas_bg_img = PhotoImage(file="res/background.png")
calculate_btn_img = PhotoImage(file="res/calculate_button.png")


canvas = Canvas(height=768, width=1024)
# canvas_background = canvas.create_image(530, 400, image=canvas_bg_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=8, columnspan=6)

# calculate_btn = Button(image=calculate_btn_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=select_best_candidate)
calculate_btn = Button(text="Calculate", highlightthickness=0, borderwidth=0, command=select_best_candidate)
calculate_btn.grid(row=7, column=2, columnspan=2)

option_label = Label(text="Option 1")
option_label.grid(row=0, column=0, columnspan=2)
time_label = Label(text="Time:")
time_label.grid(row=1, column=0)
rating_label = Label(text="Rating:")
rating_label.grid(row=2, column=0)
price_label = Label(text="Price:")
price_label.grid(row=3, column=0)
fuel_label = Label(text="Fuel:")
fuel_label.grid(row=4, column=0)
score_label = Label(text="Score:")
score_label.grid(row=5, column=0)

option_label_2 = Label(text="Option 2")
option_label_2.grid(row=0, column=2, columnspan=2)
time_label_2 = Label(text="Time:")
time_label_2.grid(row=1, column=2)
rating_label_2 = Label(text="Rating:")
rating_label_2.grid(row=2, column=2)
price_label_2 = Label(text="Price:")
price_label_2.grid(row=3, column=2)
fuel_label_2 = Label(text="Fuel:")
fuel_label_2.grid(row=4, column=2)
score_label_2 = Label(text="Score:")
score_label_2.grid(row=5, column=2)

option_label_3 = Label(text="Option 3")
option_label_3.grid(row=0, column=4, columnspan=2)
time_label_3 = Label(text="Time:")
time_label_3.grid(row=1, column=4)
rating_label_3 = Label(text="Rating:")
rating_label_3.grid(row=2, column=4)
price_label_3 = Label(text="Price:")
price_label_3.grid(row=3, column=4)
fuel_label_3 = Label(text="Fuel:")
fuel_label_3.grid(row=4, column=4)
score_label_3 = Label(text="Score:")
score_label_3.grid(row=5, column=4)

bc_label_3 = Label(text="Best Option:")
bc_label_3.grid(row=6, column=2)
bc_label_3 = Label(text="Option X")
bc_label_3.grid(row=6, column=3)


window.mainloop()