from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

worker = Table(
    "worker",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("surname", String),
)