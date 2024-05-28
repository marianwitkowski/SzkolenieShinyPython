from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Home",
            ui.h2("Welcome to Shiny for Python!"),
            ui.input_slider("n", "N", 0, 100, 50),
            ui.output_text("text")
        ),
        ui.nav_panel("Analysis",
            ui.layout_sidebar(
                ui.panel_sidebar(
                    ui.h2("Sidebar"),
                    ui.input_slider("n_analysis", "N Analysis", 0, 100, 50)
                ),
                ui.panel_main(
                    ui.h2("Analysis Results"),
                    ui.output_text("analysis_text")
                )
            )
        )
    )
)

def server(input, output, session):
    @output
    @render.text
    def text():
        return f"N: {input.n()}"

    @output
    @render.text
    def analysis_text():
        return f"N Analysis: {input.n_analysis()}"

app = App(app_ui, server)

if __name__ == "__main__":
    import sys
    port = 8000  # domyślny port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(port=port)
