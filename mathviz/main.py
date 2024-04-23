from mathviz.animate_string_expression import MathExpressionScene
from manim.utils.file_ops import open_file as open_media_file
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from string import ascii_lowercase
from sympy.parsing.sympy_parser import parse_expr


def submit(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    # ui.notify(f"{name}: {input1.value}")
    ui.notify("Analyzing math expression.")
    scene = MathExpressionScene(
        input_expressions=(
            {"symbol": "t", "expression": "t=t", "domain": [-10, 10, 1]},
            {"symbol": "y", "expression": input1.value, "range": [-10, 10, 1]},
            # {"symbol": "y", "expression": "t**2 - 1"},
        )
    )
    ui.notify("Rendering MP4 file.")

    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)


ui.label("Hello Mathviz!")
with ui.row():
    var1 = ui.select(list(ascii_lowercase), value="y")  # , on_change=show)
    input1 = ui.input("Function 1")
ui.button("Button", on_click=submit)
ui.run()
