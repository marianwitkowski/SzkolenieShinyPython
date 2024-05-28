from shiny import App, render, ui, reactive

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.style(
            """
            .error {
                color: red;
                font-weight: bold;
            }
            """
        )
    ),
    ui.h2("Kalkulator Zapotrzebowania Kalorycznego"),
    ui.input_numeric("age", "Wiek (lata)", value=25, min=10, step=1),
    ui.input_numeric("height", "Wzrost (cm)", value=170, min=140, max=220, step=1),
    ui.input_numeric("weight", "Waga (kg)", value=70, min=30, step=1),
    ui.input_radio_buttons("gender", "Płeć", {"male": "Mężczyzna", "female": "Kobieta"}),
    ui.input_select("activity_level", "Poziom aktywności",
                    {
                        "sedentary": "Siedzący (brak ćwiczeń)",
                        "lightly_active": "Lekko aktywny (lekki wysiłek/sport 1-3 dni w tygodniu)",
                        "moderately_active": "Umiarkowanie aktywny (umiarkowany wysiłek/sport 3-5 dni w tygodniu)",
                        "very_active": "Bardzo aktywny (intensywny wysiłek/sport 6-7 dni w tygodniu)",
                        "super_active": "Ekstremalnie aktywny (bardzo intensywny wysiłek/sport, praca fizyczna)"
                    }
                    ),
    ui.input_action_button("calculate", "Oblicz"),
    ui.output_text_verbatim("calories"),
    ui.div(ui.output_text("error_messages"), class_="error")
)

def server(input, output, session):

    def calculate_bmr(age, height, weight, gender):
        if gender == "male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr

    def calculate_calories(bmr, activity_level):
        activity_factors = {
            "sedentary": 1.2,
            "lightly_active": 1.375,
            "moderately_active": 1.55,
            "very_active": 1.725,
            "super_active": 1.9
        }
        return bmr * activity_factors[activity_level]

    @output
    @render.text
    @reactive.event(input.calculate)
    def calories():
        age = input.age()
        height = input.height()
        weight = input.weight()
        gender = input.gender()
        activity_level = input.activity_level()

        if not (age and height and weight and gender and activity_level):
            return ""

        bmr = calculate_bmr(age, height, weight, gender)
        daily_calories = calculate_calories(bmr, activity_level)

        return f"Twoje dzienne zapotrzebowanie kaloryczne wynosi: {daily_calories:.2f} kcal"

    @output
    @render.text
    @reactive.event(input.calculate)
    def error_messages():
        age = input.age()
        height = input.height()

        if age is None or height is None:
            return ""

        if age < 10 or age > 100:
            return "Wiek musi być między 10 a 100 lat."
        if height < 140 or height > 220:
            return "Wzrost musi być między 140 a 220 cm."
        return ""


# Tworzenie aplikacji
app = App(app_ui, server)

# Uruchamianie aplikacji
if __name__ == "__main__":
    app.run(port=8000)
