import json
import re
import reflex as rx 

from ..ui.base import base_page
from ..components.add_user_form_field import form_field


class AddUserState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    def handle_submit(self, form_data: dict):
        self.form_data = form_data

        self.user_name = form_data.get('name')
        self.user_weight = form_data.get('weight')
        self.user_height = form_data.get('height')


        print(
            json.dumps(
                self.form_data,
                indent=4
            )
        )

    @rx.var
    def username_empty(self) -> bool:
        pass

    # @rx.var
    # def invalid_email(self) -> bool:
    #     return not re.match(
    #         r"[^@]+@[^@]+.[^@]+", self.user_entered_email
    #     )

def add_user_button() -> rx.Component():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon('plus', size=20),
                rx.text('Add User')
            )
        ),
        rx.dialog.content(
            rx.dialog.title('Add User'),
            rx.dialog.description('Add yourself'),
            rx.form.root(
                # form fields
                rx.vstack(
                    
                    # name
                    form_field(
                        'Name',
                        'Your Name',
                        'text',
                        'name',
                        'user',
                        pattern='seb'
                    ),

                    # height
                    form_field(
                        'height',
                        """6'4" """,
                        'number',
                        'height',
                        'user'
                    ),

                    # weight
                    form_field(
                        'Weight',
                        '185lbs',
                        'number',
                        'weight',
                        'weight'
                    ),

                    # email
                    form_field(
                        'email',
                        'email@address.com',
                        'email',
                        'email',
                        'mail'
                    ),
                ),

                # dialog close buttons
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            'Cancel',
                            color_scheme='gray',
                            variant='soft'
                        )
                    ),
                    rx.form.submit(
                        rx.dialog.close(
                            rx.button(
                                'save'
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
                reset_on_submit=True
            )
        )
    )

def user_table() -> rx.Component:
    pass

# @rx.page(route='/about')
def users_page() -> rx.Component:
    add_user = add_user_button()

    return base_page(add_user)




