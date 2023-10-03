from tkinter import *

def select_best_candidate():
    pass

BACKGROUND_COLOR = "#1768AC"
PANEL_BACKGROUND_COLOR = "#EFEFEF"
BC_PANEL_BACKGROUND_COLOR = "#BBF2FD"
FONT = ("Calibri", 20)
FONT_BOLD = ("Calibri", 30, "bold")
ENTRY_WIDTH = 5

window = Tk()
window.title("Decision Making")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas_bg_img = PhotoImage(file="res/background.png")
calculate_btn_img = PhotoImage(file="res/calculate_button.png")


canvas = Canvas(height=800, width=1024)
canvas_background = canvas.create_image(513, 400, image=canvas_bg_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=8, columnspan=6)

default_values = [
    [60, 4.9, 15, 2],
    [45, 3.5, 12, 0.5],
    [120, 3, 8, 0]
]

candidates_fields_list = []
for i in range(3):
    candidate_fields = dict()

    candidate_fields['option'] = Label(text=f"Option {i+1}", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['option'].grid(row=0, column=2*i, columnspan=2)

    candidate_fields['time'] = Label(text="Time:     ", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['time'].grid(row=1, column=2*i, sticky='e')
    candidate_fields['time_entry'] = Entry(width=ENTRY_WIDTH, font=FONT)
    candidate_fields['time_entry'].grid(row=1, column=2*i+1, sticky='w')
    candidate_fields['time_entry'].insert(0, default_values[i][0])

    candidate_fields['rating'] = Label(text="Rating:     ", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['rating'].grid(row=2, column=2*i, sticky='e')
    candidate_fields['rating_entry'] = Entry(width=ENTRY_WIDTH, font=FONT)
    candidate_fields['rating_entry'].grid(row=2, column=2*i+1, sticky='w')
    candidate_fields['rating_entry'].insert(0, default_values[i][1])

    candidate_fields['price'] = Label(text="Price:     ", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['price'].grid(row=3, column=2*i, sticky='e')
    candidate_fields['price_entry'] = Entry(width=ENTRY_WIDTH, font=FONT)
    candidate_fields['price_entry'].grid(row=3, column=2*i+1, sticky='w')
    candidate_fields['price_entry'].insert(0, default_values[i][2])

    candidate_fields['fuel'] = Label(text="Fuel:     ", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['fuel'].grid(row=4, column=2*i, sticky='e')
    candidate_fields['fuel_entry'] = Entry(width=ENTRY_WIDTH, font=FONT)
    candidate_fields['fuel_entry'].grid(row=4, column=2*i+1, sticky='w')
    candidate_fields['fuel_entry'].insert(0, default_values[i][3])

    candidate_fields['score'] = Label(text="Score:     ", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['score'].grid(row=5, column=2*i, sticky='e')
    candidate_fields['score_value'] = Label(text="0", background=PANEL_BACKGROUND_COLOR, font=FONT)
    candidate_fields['score_value'].grid(row=5, column=2*i+1, sticky='w')

    candidates_fields_list.append(candidate_fields)

bc_label_3 = Label(text="Best: XXXXXXXXXXX", background=BC_PANEL_BACKGROUND_COLOR, font=FONT_BOLD)
bc_label_3.grid(row=7, column=2,columnspan=2)

calculate_btn = Button(image=calculate_btn_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=select_best_candidate)
# calculate_btn = Button(text="Calculate", highlightthickness=0, borderwidth=0, command=select_best_candidate, font=FONT)
calculate_btn.grid(row=6, column=2, columnspan=2)

window.mainloop()