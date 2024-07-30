import sqlalchemy

import reflex as rx

from sqlmodel import Field
from datetime import datetime, timezone

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

class UserModel(rx.Model, table=True):
    username: str
    height: int
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )