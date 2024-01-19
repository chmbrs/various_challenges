from fastapi import FastAPI
from nicegui import ui

import backend


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/', title="Various challenges")
    def show():
        with ui.row():
            ui.label('VARIOUS CHALLENGES')

        with ui.row():
            ui.label('Write a python function that finds the duplicate items in any given array:')
        with ui.row():
            duplicated_items = ui.input('Array items (separated by comas). Ex: a,b,c,a')
            duplicated_items.props("size=50")
            ui.button('Find!', on_click=lambda: duplicates(duplicated_items.value)).props('clearable')

        with ui.row():
            ui.label('Write an async python function that writes every item in any given array with 1, 2, 4, 8, '
                     '… seconds apart:')
        with ui.row():
            delay_items = ui.input('Array items (separated by comas). Ex: x,y,z')
            delay_items.props("size=50")
            ui.button('Send!', on_click=lambda: progressive_delay_item_writer(delay_items.value)).props('clearable')

        with ui.row():
            ui.label('''Write an efficient method that tells us whether or not an input string brackets 
            { } ( ) [ ] opened and closed properly:''')
        with ui.row():
            brackets_input = ui.input('Ex: {(])}')
            ui.button('Check!', on_click=lambda: open_closed_brackets(str(brackets_input.value))).props('clearable')

    def duplicates(duplicated_items):
        duplicated_items_list = list(str(duplicated_items).split(','))
        result = backend.find_duplicated_items(duplicated_items_list)
        ui.notify(result)

    async def progressive_delay_item_writer(delay_items):
        delay_items_list = list(str(delay_items).split(','))
        result = await backend.progressive_delay_item_writer(delay_items_list)
        ui.notify(result)

    def open_closed_brackets(brackets_input):
        result = backend.closed_brackets_checker(brackets_input)
        ui.notify(result)

    ui.run_with(
        fastapi_app
    )
