from nicegui import events, ui

columns = [
    {"name": "name", "label": "Name", "field": "name"},
    {"name": "age", "label": "Age", "field": "age"},
]
rows = [
    {"id": 0, "name": "Alice", "age": 18},
    {"id": 1, "name": "Bob", "age": 21},
    {"id": 2, "name": "Carol"},
]
name_options = ["Alice", "Bob", "Carol"]


def rename(e: events.GenericEventArguments) -> None:
    for row in rows:
        if row["id"] == e.args["id"]:
            row["name"] = e.args["name"]
    ui.notify(f"Table.rows is now: {table.rows}")


table = ui.table(columns=columns, rows=rows).classes("w-full")
table.add_slot(
    "body-cell-name",
    r'''
    <q-td key="name" :props="props">
        <q-input
            v-model="props.row.name"
            :options="'''
    + str(name_options)
    + r""""
            @update:model-value="() => $parent.$emit('rename', props.row)"
        />
    </q-td>
""",
)
table.on("rename", rename)

ui.run()
