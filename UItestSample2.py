'''
<!DOCTYPE html>
<html>
<head>
    <title>Sum Calculator</title>
</head>
<body>
    <form id="sum-form">
        <input type="number" id="num1" name="num1">
        <input type="number" id="num2" name="num2">
        <button type="button" onclick="calculateSum()">Calculate</button>
    </form>
    <div id="result"></div>
    <script>
        function calculateSum() {
            var num1 = document.getElementById('num1').value;
            var num2 = document.getElementById('num2').value;
            var sum = parseInt(num1) + parseInt(num2);
            document.getElementById('result').innerText = 'Sum: ' + sum;
        }
    </script>
</body>
</html>

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def browser():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Quit the WebDriver
    driver.quit()

def test_sum_calculation(browser):
    # Open the web page
    browser.get('file:///path/to/your/templates/index.html')
    
    # Find the input elements and enter values
    num1 = browser.find_element(By.ID, 'num1')
    num1.send_keys('2')
    num2 = browser.find_element(By.ID, 'num2')
    num2.send_keys('3')
    
    # Click the Calculate button
    button = browser.find_element(By.XPATH, "//button[@onclick='calculateSum()']")
    button.click()
    
    # Check the result
    result = browser.find_element(By.ID, 'result')
    assert result.text == 'Sum: 5'
