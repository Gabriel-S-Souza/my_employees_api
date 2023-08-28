import sqlalchemy
from data.database import metadata

employees_table = sqlalchemy.Table(
    "employees",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("personal_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("biometric", sqlalchemy.ARRAY(sqlalchemy.Float), nullable=False),
    sqlalchemy.Column("pic", sqlalchemy.ARRAY(sqlalchemy.Integer), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.String, nullable=False)
)