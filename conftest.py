import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
	
def pytest_addoption(parser):
	# задаем опцию для запуска "язык": ru, fr и тд.
	parser.addoption('--language', action='store', default="en", help="Say language name to select")
	
@pytest.fixture(scope="function")
def browser(request):

	# считываем язык
	user_language = request.config.getoption("language")
	option = Options()
	option.add_experimental_option('prefs', {'intl.accept_languages':user_language})
	browser = webdriver.Chrome(options=option)
	
	yield browser
	# закрытие браузера после работы