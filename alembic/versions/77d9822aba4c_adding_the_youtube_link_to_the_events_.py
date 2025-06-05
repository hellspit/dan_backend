"""adding the youtube link to the events and upcoming events as well changing their schemas and all

Revision ID: 77d9822aba4c
Revises: 
Create Date: 2025-06-04 17:13:36.330136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77d9822aba4c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('events', sa.Column('youtube_link', sa.String(), nullable= True))

     
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
