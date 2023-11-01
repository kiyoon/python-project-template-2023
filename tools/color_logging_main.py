from rich.traceback import install

install()

import logging
import os

from rich.logging import RichHandler

import zproject

logger = logging.getLogger(__name__)

log_path = "train.log"


def main():
    # Write main code here
    pass


if __name__ == "__main__":
    """
    Initialise with NOTSET level and null device, and add stream handler separately.
    This way, the root logging level is NOTSET (log all), and we can customise each handler's behaviour.
    If we set the level during the initialisation, it will affect to ALL streams,
    so the file stream cannot be more verbose (lower level) than the console stream.
    """
    logging.basicConfig(
        format="",
        level=logging.NOTSET,
        stream=open(os.devnull, "w"),
    )

    # If you want to suppress logs from other modules, set their level to WARNING or higher
    # logging.getLogger('slowfast.utils.checkpoint').setLevel(logging.WARNING)

    console_handler = RichHandler(
        level=logging.INFO,
        show_time=True,
        show_level=True,
        show_path=True,
    )
    console_format = logging.Formatter(
        fmt="%(name)s - %(message)s",
        datefmt="%m/%d %H:%M:%S",
    )
    console_handler.setFormatter(console_format)

    f_handler = logging.FileHandler(log_path)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter(
        fmt="%(asctime)s - %(name)s: %(lineno)4d - %(levelname)s - %(message)s",
        datefmt="%y/%m/%d %H:%M:%S",
    )
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(f_handler)

    try:
        logger.info(f"zproject {zproject.__version__}")
        main()
        logger.info("💖 Successfully completed!")
    except Exception:
        logger.exception("Exception occurred")
