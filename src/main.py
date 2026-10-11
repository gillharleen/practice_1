import logging
import os
from pathlib import Path
import ingestor
import analytics
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / os.getenv("LOG_FILE", "expense_ingest.log"),
    format="%(asctime)s %(levelname)s [%(filename)s]: %(message)s",
    filemode="a",
)
logging.getLogger().setLevel(os.getenv("LOG_LEVEL", "WARNING"))


if __name__ == "__main__":
    ingestor.ingest_csv(PROJECT_ROOT / "src" / "input_files")
    print("Done. Check the logs folder.")
    analytics.show_analytics()
    print("Done. Analystics done.")