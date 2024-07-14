"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from test_app.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from test_app.pages.tools import tools
from test_app.pages.team import team
from test_app.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
