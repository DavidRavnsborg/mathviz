from mathviz.var_type import VarType
from mathviz.animate_string_expression import MathExpressionScene
from manim.utils.file_ops import open_file as open_media_file
from nicegui import ui
from nicegui.events import ValueChangeEventArguments, GenericEventArguments
from string import ascii_lowercase
from sympy.parsing.sympy_parser import parse_expr
from uuid import uuid4


# Data type creation


def independent_var_row(default_value):
    # with ui.row():
    #     ui_var = ui.select(var_chars, value=default_value)  # , on_change=show)
    return {
        "id": str(uuid4()),
        "type": VarType.Independent,
        "symbol": default_value,
        "expression": "",  # f"{default_value}={default_value}",
        "domain": [-10, 10, 1],
    }


def function_row(default_value):
    # with ui.row():
    #     ui_var = ui.select(var_chars, value=default_value)  # , on_change=show)
    #     ui_input = ui.input("Function")
    return {
        "id": str(uuid4()),
        "type": VarType.Dependent,
        "symbol": default_value,
        "expression": "x^2 + 1",
        "range": [-10, 10, 1],
    }


# Event handlers


def submit(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    # ui.notify(f"{name}: {input1.value}")
    ui.notify("Analyzing math expression...")
    scene = MathExpressionScene(
        input_expressions=var_rows
        # (
        #     {"symbol": "t", "expression": "t=t", "domain": [-10, 10, 1]},
        #     {
        #         "symbol": ui_var1.value,
        #         "expression": ui_input1.value,
        #         "range": [-10, 10, 1],
        #     },
        #     # {"symbol": "y", "expression": "t**2 - 1"},
        # )
    )
    ui.notify("Rendering MP4 file...")
    scene.render()
    # open_media_file(scene.renderer.file_writer.movie_file_path)
    # TODO: Make movie_path a dictionary, and the rightside movie pane tabbed.
    app.storage.user["movie_path"] = str(scene.renderer.file_writer.movie_file_path)


def change_symbol(e: GenericEventArguments) -> None:
    for row in var_rows:
        if row["id"] == e.args["id"]:
            row["symbol"] = e.args["symbol"]
            break


def change_expression(e: GenericEventArguments) -> None:
    for row in var_rows:
        if row["id"] == e.args["id"]:
            row["expression"] = e.args["expression"]
            break


def get_unused_var_char(var_rows):
    for char in var_char_defaults:
        for row in var_rows:
            if char == row["symbol"]:
                continue
            return char
    for char in var_chars:
        for row in var_rows:
            if char == row["symbol"]:
                continue
            return char


var_chars = ["θ"] + list(ascii_lowercase)
var_char_defaults = ("x", "y", "z")
columns = [
    {"name": "symbol", "label": "Symbol", "field": "symbol"},
    {"name": "expression", "label": "Expression", "field": "expression"},
]
var_rows = []
var_rows.append(independent_var_row("x"))
var_rows.append(function_row("y"))


# DOM


@ui.page("/")
async def index():
    ui.label("Hello Mathviz!")
    with ui.splitter() as splitter:
        splitter = splitter.classes("w-full")
        with splitter.before:
            table = ui.table(columns=columns, rows=var_rows).classes("w-full")
            table.add_slot(
                "body-cell-symbol",
                r'''
                <q-td key="symbol" :props="props">
                    <q-select
                        v-model="props.row.symbol"
                        :options="'''
                + str(var_chars)
                + r""""
                        @update:model-value="() => $parent.$emit('change_symbol', props.row)"
                    />
                </q-td>
            """,
            )
            table.on("change_symbol", change_symbol)
            table.add_slot(
                "body-cell-expression",
                r"""
                <q-td key="expression" :props="props">
                    <q-input
                        v-model="props.row.expression"
                        @update:model-value="() => $parent.$emit('change_expression', props.row)"
                    />
                </q-td>
            """,
            )
            table.on("change_expression", change_expression)
            ui.button(
                "+",
                on_click=lambda: var_rows.append(
                    function_row(default_value=get_unused_var_char(var_rows))
                ),
            )
            ui.button(
                "debug",
                on_click=lambda: (
                    print(var_rows),
                    ui.notify(app.storage.user.get("movie_path")),
                ),
            )
            ui.button("Render animation", on_click=submit)
        with splitter.after:
            video = ui.video(
                "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"
            ).bind_source_from(app.storage.user, "movie_path")
            video.on("ended", lambda _: ui.notify("Video playback completed"))


ui.run(storage_secret="foobar")
