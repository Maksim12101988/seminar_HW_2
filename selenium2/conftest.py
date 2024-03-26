import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Фикстура для загрузки данных из конфигурационного файла
@pytest.fixture(scope="session")
def testdata():
    with open('./testdata.yaml') as f:
        return yaml.safe_load(f)

# Фикстура для инициализации драйвера браузера
@pytest.fixture(scope="session")
def browser(testdata):
    browser_type = testdata['browser']
    if browser_type == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_type == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура для открытия веб-страницы
@pytest.fixture
def site(browser, testdata):
    address = testdata['address']
    browser.get(address)
    time.sleep(testdata['sleep_time'])
    return browser

# Фикстуры для локаторов элементов
@pytest.fixture
def x_selector1():
    return """//*[@id='login']/div[1]/label/input"""

@pytest.fixture
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture
def btn_selector():
    return "button"

@pytest.fixture
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

# Фикстура для ожидаемого текста ошибки
@pytest.fixture
def expected_error_text():
    return "401"

# Фикстуры для имени пользователя и пароля
@pytest.fixture
def username(testdata):
    return testdata['username']

@pytest.fixture
def password(testdata):
    return testdata['password']



# Фикстуры для элементов формы добавления поста
@pytest.fixture
def post_title_selector():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture
def submit_description_selector():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture
def post_content_selector():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture
def add_post_selector():
    return """//*[@id="create-item"]/div/div/div[4]/div/label/span/button"""







