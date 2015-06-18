from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

company = Table('company', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('about', String),
)

department = Table('department', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('about', String),
)

document = Table('document', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('title', String),
    Column('description', String),
    Column('keywords', String),
    Column('body', String),
    Column('uploader_id', Integer),
    Column('department', String),
    Column('company', String),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String),
    Column('password', String),
    Column('authenticated', Boolean, default=ColumnDefault(False)),
    Column('department', String),
    Column('company', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    post_meta.tables['company'].create()
    post_meta.tables['department'].create()
    post_meta.tables['document'].create()
    post_meta.tables['user'].columns['company'].create()
    post_meta.tables['user'].columns['department'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    post_meta.tables['company'].drop()
    post_meta.tables['department'].drop()
    post_meta.tables['document'].drop()
    post_meta.tables['user'].columns['company'].drop()
    post_meta.tables['user'].columns['department'].drop()
