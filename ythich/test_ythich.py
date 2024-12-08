import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestYthich():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Thêm thời gian chờ ngầm định
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_ythich(self):
        self.driver.get("https://nxbkimdong.com.vn/")
        self.driver.set_window_size(974, 969)

        # Chờ và nhấp vào sản phẩm đầu tiên
        item_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "1062054763"))
        )
        item_element.click()
        time.sleep(1)  # Chờ 1 giây để trang tải hoàn chỉnh

        # Thêm sản phẩm vào danh sách yêu thích
        add_to_wishlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_add > .fa"))
        )
        add_to_wishlist.click()
        time.sleep(1)  # Chờ 1 giây để thao tác được thực hiện

        # Nhấp vào sản phẩm tiếp theo
        next_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "1061896912"))
        )
        next_item.click()
        time.sleep(1)

        # Thêm sản phẩm thứ hai vào danh sách yêu thích
        add_to_wishlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_add > .fa"))
        )
        add_to_wishlist.click()
        time.sleep(1)

        # Nhấp vào sản phẩm thứ ba
        next_item_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "1061896735"))
        )
        next_item_2.click()
        time.sleep(1)

        # Thêm sản phẩm thứ ba vào danh sách yêu thích
        add_to_wishlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_add > .fa"))
        )
        add_to_wishlist.click()
        time.sleep(1)

        # Cuộn đến sản phẩm tiếp theo và nhấp
        try:
            item_to_scroll = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".ft-content .grid:nth-child(1)"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", item_to_scroll)
            item_to_scroll.click()
            time.sleep(1)  # Chờ 1 giây để thao tác thực hiện
        except Exception as e:
            print(f"Lỗi khi thao tác với phần tử: {e}")
            self.driver.save_screenshot("error_screenshot.png")
            raise
