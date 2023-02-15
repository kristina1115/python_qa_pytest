from selenium.webdriver.common.by import By

class Common:
    class user_login:
        email_input = (By.ID, 'Email')
        password_input = (By.ID, 'Password')
        loggin_button = (By.CSS_SELECTOR, "[type = 'submit']")