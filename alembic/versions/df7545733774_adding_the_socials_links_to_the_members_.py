"""adding the socials links to the members part

Revision ID: df7545733774
Revises: 46956f34547e
Create Date: 2025-06-05 16:49:50.876058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df7545733774'
down_revision: Union[str, None] = '46956f34547e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column("members", sa.Column("linkedin_link",sa.String(), nullable= True))
    op.add_column("members", sa.Column("twitter_link", sa.String(), nullable = True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
