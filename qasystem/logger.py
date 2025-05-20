import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logpath = os.path.join(os.getcwd(), "logs")

os.makedirs(logpath, exist_ok=True)

LOG_FILE_PATH = os.path.join(logpath, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == '__main__':
    logging.info("Heren again I am testing")