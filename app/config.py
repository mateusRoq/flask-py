import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/tasks'
    SQLALCHEMY_TRACK_MODIFICATIONS = False