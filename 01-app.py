from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny"),
    ui.input_slider("n", "Suwak", 0, 100, 50),
    ui.output_text("text")
)

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Tab 1",
            ui.h2("Tab 1 Content"),
            ui.input_slider("n1", "N1", 0, 100, 50)
        ),
        ui.nav_panel("Tab 2",
            ui.h2("Tab 2 Content"),
            ui.input_slider("n2", "N2", 0, 100, 50)
        )
    )
)

app_ui = ui.page_fluid(
    ui.panel_well(
        ui.h2("Well Panel"),
        ui.input_slider("n", "N", 0, 100, 50),
        ui.output_text("text")
    )
)

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.h2("Sidebar"),
            ui.input_slider("n", "N", 0, 100, 50)
        ),
        ui.panel_main(
            ui.h2("Main Panel"),
            ui.output_text("text")
        )
    )
)

app_ui = ui.page_fluid(
    ui.input_radio_buttons("show_panel", "Show Panel", {"yes": "Yes", "no": "No"}, selected="yes"),
    ui.panel_conditional(
        "input.show_panel == 'yes'",
        ui.panel_well(
            ui.h2("Conditional Panel"),
            ui.output_text("text")
        )
    )
)


def server(input, output, session):
    @output
    @render.text
    def text():
        return f"Wartość slidera to: {input.n()}"

app = App(app_ui, server)

if __name__ == "__main__":
    app.run(port=8001)

