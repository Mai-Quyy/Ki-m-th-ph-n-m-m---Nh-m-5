import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBanchay():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_banchay(self):
        self.driver.get("https://nxbkimdong.com.vn/")
        self.driver.set_window_size(1936, 1056)

        # Click the menu button
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-bars:nth-child(1)"))
        )
        menu_button.click()
        time.sleep(1)  # Chờ 1 giây để đảm bảo menu xuất hiện

        # Hover and click the second menu item
        menu_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-child(2) span"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_item).perform()  # Hover over menu item
        time.sleep(1)  # Chờ 1 giây
        menu_item.click()

        # Wait for SortBy dropdown to be clickable
        sortby_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SortBy"))
        )
        sortby_dropdown.click()
        time.sleep(1)  # Chờ 1 giây để danh sách hiển thị

        # Select "Bán chạy nhất"
        sortby_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//option[. = 'Bán chạy nhất']"))
        )
        sortby_option.click()
        time.sleep(1)  # Chờ 1 giây để lựa chọn được xử lý

        # Click the category
        category_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "- Nhà trẻ, Mẫu giáo (0-5 tuổi)"))
        )
        category_link.click()
        time.sleep(1)  # Chờ 1 giây để chuyển trang
