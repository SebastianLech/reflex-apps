import json
import re
import reflex as rx 

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