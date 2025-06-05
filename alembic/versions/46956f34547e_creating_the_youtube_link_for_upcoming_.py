"""creating the youtube link for upcoming events

Revision ID: 46956f34547e
Revises: 77d9822aba4c
Create Date: 2025-06-05 14:50:20.925316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46956f34547e'
down_revision: Union[str, None] = '77d9822aba4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('upcoming_events', sa.Column('youtube_link', sa.String(), nullable = True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
