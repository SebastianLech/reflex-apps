import reflex as rx


def form_field(
    label: str,
    placeholder: str,
    type: str,
    name: str,
    icon: str,
    default_value: str = "",
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.hstack(
                rx.icon(icon, size=16, stroke_width=1.5),
                rx.form.label(label),
                align="center",
                spacing="2",
            ),
            rx.hstack(
                rx.form.control(
                    rx.input(
                        placeholder=placeholder, type=type, default_value=default_value
                    ),
                    as_child=True,
                    width='40%',
                ),
                rx.text(
                    'some text',
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
        name=name,
        width="100%",
    )