from mathviz.hashing import input_expression_hash
from mathviz.var_type import VarType
from mathviz.animate_string_expression import MathExpressionScene
from nicegui import app, ui
from nicegui.events import ValueChangeEventArguments, GenericEventArguments
from string import ascii_lowercase
from uuid import uuid4


# Data type creation


def independent_var_row(default_value):
    return {
        "id": str(uuid4()),
        "type": VarType.Independent,
        "symbol": default_value,
        "expression": "",  # f"{default_value}={default_value}",
        "domain": [-10, 10, 1],
    }


def function_row(default_value):
    return {
        "id": str(uuid4()),
        "type": VarType.Dependent,
        "symbol": default_value,
        "expression": "x^2 + 1",
        "range": [-10, 10, 1],
    }


# Event handlers


async def submit(event: ValueChangeEventArguments):
    emit_notification("Analyzing math expression...")
    input_expressions = var_rows
    uid = input_expression_hash(input_expressions)
    scene = MathExpressionScene(input_expressions=input_expressions, uid=uid)
    emit_notification("Rendering MP4 file...")
    scene.render()
    emit_notification("Playing MP4 file.")
    # open_media_file(scene.renderer.file_writer.movie_file_path)
    app.storage.general["animations"][uid] = {
        "path": str(scene.renderer.file_writer.movie_file_path),
        "input_expressions": input_expressions,
    }
    app.storage.user["animation_active"] = uid


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


def emit_notification(message: str):
    print(message)
    ui.notify(message)


# Initial conditions


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
    if app.storage.general.get("animations") is None:
        app.storage.general["animations"] = {}
    with ui.splitter() as splitter:
        splitter = splitter.classes("w-full")
        with splitter.before:
            interactive_panel()
        with splitter.after:
            video_panel()


def interactive_panel():
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


def video_panel():
    animations = app.storage.general.get("animations")
    if len(animations) == 0:
        ui.label("No cached animations to display.").tailwind(
            "flex",
            # Vertical centering
            "h-screen",
            "items-center",
            # Horizontal centering
            "justify-center",
            "w-1/2",
        )
        return

    uid = app.storage.user["animation_active"]
    if uid is None:
        active_animation = list(app.storage.general["animations"].values())[0]
    else:
        active_animation = animations[uid]

    video = ui.video(active_animation["path"]).bind_source_from(
        app.storage.user, "animation_path_active"
    )
    video.on("ended", lambda _: emit_notification("Video playback completed"))


@ui.page("/animations")
async def animations():
    animations = app.storage.general.get("animations")
    ui.label(
        f"{len(animations)} animations"
        if animations is not None
        else "`animations` is not initialized."
    )
    ui.label(str(animations) if animations is not None else "No `animations` stored.")


@ui.page("/animation_active")
async def animation_active():
    animation_active = app.storage.user.get("animation_active")
    ui.label(
        animation_active
        if animation_active is not None
        else "No `animation_active` associated with this user/cookie."
    )


ui.run(storage_secret="foobar")
