from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# Локаторы
elements_button_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[1]')
forms_button_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]') 
alers_button_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]')
widgets_button_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]')
interactions_button_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]')
book_button_locator = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]')

class MainPage(BasePage):
   def __init__(self, driver):
      super().__init__(driver)

   @property
   def element_main(self):
      return self.find(elements_button_locator)
   
   @property
   def forms_main(self):
      return self.find(forms_button_locator)
   
   @property
   def alerts_main(self):
      return self.find(alers_button_locator)
   
   @property
   def interactions_main(self):
      return self.find(interactions_button_locator)
   
   @property
   def widgets_main(self):
      return self.find(widgets_button_locator)
   
   @property
   def book_main(self):
      return self.find(book_button_locator)
   
   #def open(self):
     # self.driver.get('https://demoqa.com')

   def scroll_to_element_forms(self):
      self.scroll_to_element(forms_button_locator)
      

      
