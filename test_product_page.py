from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)   
    product_page.open()                     
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_book_name()
    product_page.should_be_book_price()

