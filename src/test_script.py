from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MERNTests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)


    def test_add_to_cart(self):
        self.base_url = "http://localhost:3000"
        driver = self.driver
        driver.get(f"{self.base_url}/product/2") 
        print("Cart Test")
        
        # Verify product name
        product_name = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(
            product_name, 
            "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse", 
            "Product name should be 'Product 2'"
        )
        
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'ADD TO CART')]"))
        )
        
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
        time.sleep(1)  
        add_to_cart_button.click()
        time.sleep(2)  

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "nav-cart-count"), "1")
        )

        cart_count_element = driver.find_element(By.CLASS_NAME, "nav-cart-count")
        cart_count = cart_count_element.text
        print("This is the cart count:", cart_count)

        self.assertEqual(cart_count, "1", "Cart count should be updated to 1")


    def test_add_and_remove_item_from_cart(self):
        driver = self.driver
        print("Remove from Cart Test")
        
        driver.get("http://localhost:3000/product/1")
        time.sleep(2)  
        
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "addtocartbtn"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
        time.sleep(1)
        add_to_cart_button.click()
        time.sleep(2)  
        
        driver.get("http://localhost:3000/cart")
        time.sleep(2)
        
        product_name = driver.find_element(By.CLASS_NAME, "CartItemLists").text
        product_quantity_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cartitems-quantity"))
        )
        product_quantity = product_quantity_element.text

        self.assertTrue(product_name, "Product is not displayed in the cart.")
        self.assertEqual(product_quantity, "1", f"Expected quantity 1, but got {product_quantity}.")
        print("Item added to cart successfully and verified.")
        
        remove_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cartitems-remove-icon"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
        time.sleep(1)
        remove_button.click()
        time.sleep(5)  
        
        empty_cart_message_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "empty-cart"))
        )
        empty_cart_message = empty_cart_message_element.text

        self.assertIn("Hey, it feels so light!", empty_cart_message, "Cart is not empty after removing the item.")
        print("Item removed successfully and cart is verified as empty.")

    def test_contact_page_accessibility(self):
            driver = self.driver
            driver.get("http://localhost:3000/contact")
            time.sleep(2)  
            self.assertIn("Contact", driver.title, "Contact page is not accessible.")
            print("Contact page is accessible.")

    def test_login_signup_page_accessibility(self):
            driver = self.driver
            driver.get("http://localhost:3000/login")
            time.sleep(2)  
            self.assertIn("Login", driver.title, "Login/Signup page is not accessible.")
            print("Login/Signup page is accessible.")

    def test_cart_page_accessibility(self):
            driver = self.driver
            driver.get("http://localhost:3000/cart")
            time.sleep(2)  
            self.assertIn("Cart", driver.title, "Cart page is not accessible.")
            print("Cart page is accessible.")

    def test_about_page_accessibility(self):
            driver = self.driver
            driver.get("http://localhost:3000/about")
            time.sleep(2)  
            self.assertIn("About", driver.title, "About page is not accessible.")
            print("About page is accessible.")
    def test_product_page_accessibility(self):
            driver = self.driver
            driver.get("http://localhost:3000/product/1") 
            time.sleep(2)  
            self.assertIn("Product", driver.title, "Product page is not accessible.")
            print("Product page is accessible.")

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
