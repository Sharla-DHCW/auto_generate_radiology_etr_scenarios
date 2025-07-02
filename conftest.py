import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture
def driver():
    # Set up Edge options (optional)
    edge_options = EdgeOptions()
    edge_options.add_argument("--start-maximized")  # Open browser in maximized mode
    # edge_options.add_argument("--headless")       # Uncomment to run in headless mode

    # Set up the Edge WebDriver service
    # Make sure msedgedriver.exe is in your PATH or provide the exact path here
    service = EdgeService()

    # Create Edge WebDriver instance
    driver = webdriver.Edge(service=service, options=edge_options)

    yield driver  # This is returned to the test function

    driver.quit()  # Cleanup after test