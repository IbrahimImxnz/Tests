
'''
<!-- sample_app/templates/login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>
</body>
</html>

'''

# tests/test_ui.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login():
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000/login')
    
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    
    username.send_keys('testuser')
    password.send_keys('password')
    password.send_keys(Keys.RETURN)
    
    assert 'Dashboard' in driver.title
    driver.quit()
