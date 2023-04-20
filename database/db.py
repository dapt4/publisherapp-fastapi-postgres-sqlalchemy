from sqlalchemy import create_engine
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

DATABASE_URL = os.environ.get("ENV_DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

