# Express
from shiny.express import input, render, ui

with ui.sidebar():
    ui.input_text("txt_in", "Type something here:")

with ui.card():
    @render.code
    def result():
        return f"You entered '{input.txt_in()}'."

