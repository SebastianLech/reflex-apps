import json
import re
import reflex as rx 

from ..ui.base import base_page
from ..components.add_user_form_field import form_field


def parse_username(username) -> str:
    return re.sub(r"[,.;@#?!&$%^*()_0-9+-=]+\ *", "", username).lower().replace(' ', '-')


def parse_height(height) -> int:
    """
    entered_height is of the form 5'10"
    """
    try:
        feet, inches, *rest = re.split("[\'\"]", height)
        return int(feet) * 12 + int(inches or 0) # convert to inches
    except ValueError:
        return height

class AddUserState(rx.State):
    form_data: dict = {}

    user_entered_username: str
    user_entered_height: str
    user_entered_weight: int

    username: str
    height: str
    weight: int

    name_not_allowed_list: list[str] = ["aaa", "bbb", 'john']

    @rx.var
    def name_is_empty(self) -> bool:
        return not self.user_entered_username.strip()

    @rx.var
    def parsed_username(self) -> str:
        return parse_username(self.user_entered_username)

    @rx.var
    def parsed_height(self) -> int:
        """
        entered_height is of the form 5'10"
        """
        return parse_height(self.user_entered_height)
        
    @rx.var
    def valid_height(self) -> bool:
        return not re.match(
            r'^\d\'\d{,2}\"$', self.user_entered_height
        )

    @rx.var
    def input_invalid(self) -> bool:
        return self.name_is_empty or self.valid_height

    def clear_user_entered_data(self, value: bool):
        self.user_entered_username = ''
        self.user_entered_height = ''

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        validated_data = {}
        for k,v in form_data.items():
            if v == '' or v is None:
                continue
            validated_data[k] = v
        validated_data['username'] = parse_username(validated_data['username'])
        validated_data['height'] = parse_height(validated_data['height'])

        print(
            json.dumps(
                self.form_data,
                indent=4
            )
        )

        print(
            json.dumps(
                validated_data,
                indent=4
            )
        )

        self.username = ''
        self.height = ''
        self.user_entered_height = ''
        self.user_entered_username = ''



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
def user_table() -> rx.Component:
    pass

# @rx.page(route='/about')
def users_page() -> rx.Component:
    add_user = add_user_button()

    return base_page(add_user)




