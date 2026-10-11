import csv
import logging
from pathlib import Path
from pydantic import ValidationError
import database
from model import Expense

logger = logging.getLogger(__name__)


def ingest_csv(folder_path):
    database.clear_expenses()

    for file in Path(folder_path).glob("*.csv"):
        valid_rows = []

        with file.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row_number, row in enumerate(reader, start=2):
                try:
                    valid_rows.append(Expense(**row))
                except ValidationError as error:
                    for problem in error.errors():
                        field = problem["loc"][0]
                        message = problem["msg"]
                        value = problem["input"]
                        logger.error(
                            f"File: {file.name} | Row: {row_number} | "
                            f"Field: {field} | Error: {message} | Value: {value!r}"
                        )

        if valid_rows:
            database.insert_data_to_db(valid_rows)
            logger.info(f"Saved {len(valid_rows)} valid rows from {file.name}")