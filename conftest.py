import logging
import os
from datetime import datetime

# from Backend_Frontend_Project.frontend.login_page import LoggedUser

logger = logging.getLogger(__name__)


def pytest_configure(config):
    # Creates the 'reports' folder if it does not exist.
    os.makedirs("reports", exist_ok=True)

    # Generates the timestamp (ex: 2026-09-22_10-57-54)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Defines the path for the dynamic report.
    report_path = f"reports/tests_report_{timestamp}.html"

    # Dynamically injects the --html option into the pytest configuration.
    config.option.htmlpath = report_path
    config.option.self_contained_html = True    # resources are included. Do not depends on external files.


# def pytest_sessionstart(session):
#     logger.info(f"Report path: {session.config.option.htmlpath}")
