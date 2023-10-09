from tkinter import *

from attribute import Attribute
from decision_maker import DecisionMaker
from delegation_candidate import DelegationCandidate
from utility_preference import UtilityPreference


default_values = [
    [60, 4.9, 15, 2],
    [45, 3.5, 12, 0.5],
    [120, 3, 8, 0]
]

options = [
    "Car",
    "Motorcycle",
    "Pedestrian"
]

PLOT = True
TIME_WEIGHT = 1
RATING_WEIGHT = 1
# TIME_WEIGHT = 0.75
# RATING_WEIGHT = 0.25
# TIME_WEIGHT = 0.75
# RATING_WEIGHT = 0.25

# Utility Preference Settings
times = [0, 30, 60, 90, 120] 
times_preference = [100, 90, 70, 50, 0]
time_up = UtilityPreference("Time", times, times_preference)

ratings = [2.5, 3.5, 4.5, 5] 
ratings_preference = [0, 30, 70, 100]
ratings_up = UtilityPreference("Rating", ratings, ratings_preference)

def select_best_candidate():
    global candidates_fields_list
    times = []
    ratings = []
    prices = []
    fuel_consumptions = []
    # risks = []
    candidates_list = []
    dm = DecisionMaker()

    for i in range(3):
        times.append(Attribute("Time", float(candidates_fields_list[i]["time_entry"].get()), TIME_WEIGHT))
        ratings.append(Attribute("Rating", float(candidates_fields_list[i]["rating_entry"].get()), RATING_WEIGHT))
        prices.append(Attribute("Price", float(candidates_fields_list[i]["price_entry"].get())))
        fuel_consumptions.append(Attribute("Fuel", float(candidates_fields_list[i]["fuel_entry"].get())))
        times[i].set_utility_preference(time_up)
        ratings[i].set_utility_preference(ratings_up)

        candidate = DelegationCandidate(options[i])
        candidate.add_benefit(times[i])
        candidate.add_benefit(ratings[i])
        candidate.add_cost(prices[i])
        candidate.add_cost(fuel_consumptions[i])
        candidates_list.append(candidate)
        dm.add_candidate(candidate=candidate)
        # candidate.add_risk(risk_1)
        candidates_fields_list[i]['score_value'].config(text=round(candidate.score(), 2))

    if PLOT:
        time_up.plot_utility_preference()
        ratings_up.plot_utility_preference()
    bc = dm.select_best_candidate()
    bc_label_3.config(text=bc.name)
    

BACKGROUND_COLOR = "#1768AC"
PANEL_BACKGROUND_COLOR = "#EFEFEF"
BC_PANEL_BACKGROUND_COLOR = "#BBF2FD"
FONT = ("Calibri", 20)
FONT_COLOR = "#505050"
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

candidates_fields_list = []
for i in range(3):
    candidate_fields = dict()

    candidate_fields['option'] = Label(text=options[i], background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['option'].grid(row=0, column=2*i, columnspan=2)

    candidate_fields['time'] = Label(text="Time:     ", background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['time'].grid(row=1, column=2*i, sticky='e')
    candidate_fields['time_entry'] = Entry(width=ENTRY_WIDTH, font=FONT, fg=FONT_COLOR)
    candidate_fields['time_entry'].grid(row=1, column=2*i+1, sticky='w')
    candidate_fields['time_entry'].insert(0, default_values[i][0])

    candidate_fields['rating'] = Label(text="Rating:     ", background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['rating'].grid(row=2, column=2*i, sticky='e')
    candidate_fields['rating_entry'] = Entry(width=ENTRY_WIDTH, font=FONT, fg=FONT_COLOR)
    candidate_fields['rating_entry'].grid(row=2, column=2*i+1, sticky='w')
    candidate_fields['rating_entry'].insert(0, default_values[i][1])

    candidate_fields['price'] = Label(text="Price:     ", background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['price'].grid(row=3, column=2*i, sticky='e')
    candidate_fields['price_entry'] = Entry(width=ENTRY_WIDTH, font=FONT, fg=FONT_COLOR)
    candidate_fields['price_entry'].grid(row=3, column=2*i+1, sticky='w')
    candidate_fields['price_entry'].insert(0, default_values[i][2])

    candidate_fields['fuel'] = Label(text="Fuel:     ", background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['fuel'].grid(row=4, column=2*i, sticky='e')
    candidate_fields['fuel_entry'] = Entry(width=ENTRY_WIDTH, font=FONT, fg=FONT_COLOR)
    candidate_fields['fuel_entry'].grid(row=4, column=2*i+1, sticky='w')
    candidate_fields['fuel_entry'].insert(0, default_values[i][3])

    candidate_fields['score'] = Label(text="Score:     ", background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['score'].grid(row=5, column=2*i, sticky='e')
    candidate_fields['score_value'] = Label(text="0.0", background=PANEL_BACKGROUND_COLOR, font=FONT, fg=FONT_COLOR)
    candidate_fields['score_value'].grid(row=5, column=2*i+1, sticky='w')

    candidates_fields_list.append(candidate_fields)

bc_label_3 = Label(text="Best: -", background=BC_PANEL_BACKGROUND_COLOR, font=FONT_BOLD, fg=FONT_COLOR)
bc_label_3.grid(row=7, column=2,columnspan=2)

calculate_btn = Button(image=calculate_btn_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=select_best_candidate)
# calculate_btn = Button(text="Calculate", highlightthickness=0, borderwidth=0, command=select_best_candidate, font=FONT, fg=FONT_COLOR)
calculate_btn.grid(row=6, column=2, columnspan=2)

window.mainloop()