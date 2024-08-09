import json
import re
import reflex as rx 

from ..ui.base import base_page
from .state import AddUserState
from ..models import UserModel

def add_user_button() -> rx.Component():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon('plus', size=20),
                rx.text('Add User'),
            )
        ),
        rx.dialog.content(
            rx.dialog.title('Add User'),
            rx.form.root(
                # form fields
                rx.vstack(
                    # name
                    rx.form.field(
                        rx.flex(
                            rx.hstack(
                                rx.icon('user', size=16, stroke_width=1.5),
                                rx.form.label('Name'),
                                align="center",
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.flex(
                                    rx.form.control(
                                        rx.input(
                                            placeholder='Enter your name here',
                                            on_change=AddUserState.set_user_entered_username,
                                            name='username',
                                            # default_value='Your Name'
                                        ),
                                        as_child=True,
                                        width='100%',
                                    ),
                                    rx.cond(
                                        AddUserState.name_is_empty,
                                        rx.form.message(
                                            'Name cannot be left blank',
                                            color='var(--red-11)'
                                        )
                                    ),
                                    direction='column',
                                    spacing='1'
                                ),
                                rx.text(
                                    f'{AddUserState.parsed_username}',
                                    width='60%',
                                    align='right'
                                ),
                                align='center',
                                spacing='2',
                            ),
                            direction="column",
                            spacing="1",
                            width='100%',
                        ),
                        name='username',
                        width="100%",
                    ),
                    # height
                    rx.form.field(
                        rx.flex(
                            rx.hstack(
                                rx.icon('ruler', size=16, stroke_width=1.5),
                                rx.form.label('Height'),
                                align="center",
                                spacing="2",
                            ),
                            rx.hstack(
                                rx.flex(
                                    rx.form.control(
                                        rx.input(
                                            placeholder='Enter your height here',
                                            on_change=AddUserState.set_user_entered_height, 
                                            name='height',
                                            default_value=''
                                        ),
                                        as_child=True,
                                        width='100%',
                                    ),
                                    rx.cond(
                                        AddUserState.valid_height,
                                        rx.form.message(
                                            'e.g. 5\'10\"',
                                            color='var(--red-11)'
                                        )
                                    ),
                                    direction='column',
                                    spacing='1'
                                ),
                                rx.text(
                                    f'{AddUserState.parsed_height}in',
                                    width='60%',
                                    align='right'
                                ),
                                align='center',
                                spacing='2',
                            ),
                            direction="column",
                            spacing="1",
                            width='100%',
                        ),
                        name='height',
                        width="100%",
                    ),
                ),

                # dialog close buttons
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            'Cancel',
                            color_scheme='gray',
                            variant='soft'
                        ),
                        as_child=True,
                    ),
                    rx.form.submit(
                        rx.dialog.close(
                            rx.button(
                                'save',
                                disabled=AddUserState.input_invalid,
                                type='submit'
                            )
                        ),
                        as_child=True,
                    ),
                    padding_top='2em',
                    spacing='3',
                    mt='4',
                    justify='end'
                ),
                on_submit=AddUserState.handle_submit,
                reset_on_submit=True,
            )
        ),
        on_open_change=AddUserState.clear_user_entered_data
    )

def show_customer(user: UserModel):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.username),
        rx.table.cell(user.height),
        rx.table.cell(user.created_at),
    )

def loading_data_table_example() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Height (in)"),
                rx.table.column_header_cell("Timestamp"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                AddUserState.users, show_customer
            )
        ),
        on_mount=AddUserState.load_entries,
        width="100%",
    )

# @rx.page(route='/about')
def users_page() -> rx.Component:
    add_user = add_user_button()
    user_table = loading_data_table_example()

    return base_page(add_user, user_table)