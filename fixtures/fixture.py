from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def browser_chrome(context, timeout=30):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome('/Users/cizquierdo/PycharmProjects/BBDExample/chromedriver')
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()