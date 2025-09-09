import pytest
from unittest.mock import patch, MagicMock
from DemoQADriver import DemoQADriver

@pytest.fixture
def driver():
    """Create a DemoQADriver instance for testing"""
    return DemoQADriver(install=False)  # Don't install chromedriver during tests

@pytest.fixture
def mock_driver():
    """Create a DemoQADriver with mocked selenium"""
    with patch('DemoQADriver.demoqa_driver.SELENIUM') as mock_selenium:
        mock_selenium.create_webdriver.return_value = "session_1"
        mock_selenium.go_to.return_value = None
        mock_selenium.click_element.side_effect = Exception("Element not found")
        mock_selenium.close_browser.return_value = None
        yield DemoQADriver(install=False)

# Integration tests (require actual browser)
def test_open_browser(driver):
    """Test opening a browser session"""
    session_id = driver.open_browser(alias="test_session")
    assert session_id is not None
    # Clean up
    driver.close_browser()

def test_open_browser_with_alias(driver):
    """Test opening a browser with a specific alias"""
    alias = "my_test_session"
    session_id = driver.open_browser(alias=alias)
    # SeleniumLibrary assigns numerical IDs, so we just check it's not None
    assert session_id is not None
    # Clean up
    driver.close_browser()

def test_open_browser_headless(driver):
    """Test opening a browser in headless mode"""
    session_id = driver.open_browser(headless=True)
    assert session_id is not None
    # Clean up
    driver.close_browser()

def test_navigate_to_page(driver):
    """Test navigating to a page"""
    # First open browser
    driver.open_browser()
    # Navigate to default page
    driver.navigate_to_page()
    # Navigate to specific URL
    driver.navigate_to_page("https://demoqa.com/elements")
    # Clean up
    driver.close_browser()

def test_close_browser(driver):
    """Test closing browser session"""
    # Open browser first
    driver.open_browser()
    # Close should not raise an exception
    driver.close_browser()

# Unit tests with mocked selenium (don't require browser)
def test_open_browser_mock(mock_driver):
    """Test open browser with mocked selenium"""
    session_id = mock_driver.open_browser(alias="test_session")
    assert session_id == "session_1"

def test_open_browser_headless_mock(mock_driver):
    """Test open browser headless with mocked selenium"""
    session_id = mock_driver.open_browser(headless=True)
    assert session_id == "session_1"

def test_navigate_to_page_mock(mock_driver):
    """Test navigate to page with mocked selenium"""
    # Should not raise exception
    mock_driver.navigate_to_page("https://demoqa.com/")

def test_navigate_to_page_default_url_mock(mock_driver):
    """Test navigate to page with default URL"""
    # Should not raise exception
    mock_driver.navigate_to_page()

def test_close_browser_mock(mock_driver):
    """Test close browser with mocked selenium"""
    # Should not raise exception
    mock_driver.close_browser()