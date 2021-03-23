#!/usr/bin/env python3

from dotenv import load_dotenv
from pynonymizer.pynonymize import pynonymize
import os

load_dotenv()


pynonymize(input_path=os.getenv("DUMP_INPUT_FILE"),
            strategyfile_path=os.getenv("STRATEGY_FILE"),
            output_path=os.getenv("DUMP_OUTPUT_FILE"),
            db_user=os.getenv("DB_USER"),
            db_password=os.getenv("DB_PASSWORD"),
            db_type=os.getenv("DB_TYPE"),
            db_host=os.getenv("DB_HOST"),
            db_name=os.getenv("DB_NAME"),
            db_port=os.getenv("DB_PORT"),
            fake_locale=os.getenv("LOCALE"),
            verbose="true",
            start_at_step="RESTORE_DB"
            )
