"""changed registrated_at column default

Revision ID: e861ff431012
Revises: bbfded8ef31d
Create Date: 2024-09-24 08:17:36.348847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e861ff431012'
down_revision: Union[str, None] = 'bbfded8ef31d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'users', 
        'registered_at',
        existing_type=sa.TIMESTAMP(timezone=True),
        server_default=sa.text('NOW()') 
    )

def downgrade() -> None:
    op.alter_column(
        'users', 
        'registered_at',
        existing_type=sa.TIMESTAMP(timezone=True),
        server_default=None
    )

