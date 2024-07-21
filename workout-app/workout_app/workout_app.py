"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page

from . import pages, navigation


class State(rx.State):
    """The app state."""

    ...






def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.badge('asdfasf', height="10vh")

    )


app = rx.App()

app.add_page(
    index
)

app.add_page(
    pages.users_page,
    route=navigation.routes.USERS_ROUTE
    )

app.add_page(
    pages.about_page,
    route=navigation.routes.ABOUT_ROUTE
    )
