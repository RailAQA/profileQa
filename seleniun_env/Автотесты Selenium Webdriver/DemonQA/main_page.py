from base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPageLocators(BasePage):
   Elements_button_locator = (By.LINK_TEXT, 'Elements')
   forms_button_locator = (By.LINK_TEXT, 'Forms') 
   alers_button_locator = (By.LINK_TEXT, 'Alerts, Frame & Windows')
   widgets_button_locator = (By.LINK_TEXT, 'Widgets')
   interactions_button_locator = (By.LINK_TEXT, 'Interactions')
   book_button_locator = (By.LINK_TEXT, 'Book Store Application')

