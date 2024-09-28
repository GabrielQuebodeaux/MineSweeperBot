from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class MineField:
    def __init__(self):
        self.mine_field = [["" for x in range(9)] for y in range(9)]
        self.mine_predictions = [[0 for x in range(9)] for y in range(9)]
        self.mines = []
        self.update_mine_field()
        self.update_mine_predictions()

    def update_mine_field(self):
        for i in range(9):
            for k in range(9):
                space = driver.find_element(By.ID, f"{i + 1}_{k + 1}")
                status = space.get_attribute("class")
                adjacent_mines = ""
                if "open" in status:
                    adjacent_mines = status[10:]
                self.mine_field[i][k] = adjacent_mines
        for mine in self.mines:
            self.mine_field[mine[0]][mine[1]] = "M"

    def update_mine_predictions(self):
        for i in range(9):
            for k in range(9):
                if self.mine_field[i][k] == "" or self.mine_field[i][k] == "0":
                    continue
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if i + x not in range(9) or k + y not in range(9):
                            continue
                        if self.mine_field[i + x][k + y] == "":
                            self.mine_predictions[i + x][k + y] += 1

    def find_mines(self):
        max = 0
        coords = None
        for i in range(9):
            for k in range(9):
                if self.mine_predictions[i][k] > max:
                    max = self.mine_predictions[i][k]
                    coords = (i, k)
                    self.mine_field[i][k] = "M"
        self.mines.append(coords)
        actions.context_click(driver.find_element(By.ID, f"{coords[0] + 1}_{coords[1] + 1}"))
        actions.perform()
        actions.reset_actions()

    def dig(self, square: tuple):
        element = driver.find_element(By.ID, f"{square[0] + 1, square[1] + 1}")
        element.click()


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://minesweeperonline.com/#beginner")
actions = ActionChains(driver)
element = driver.find_element(By.XPATH, '//*[@id="5_5"]')
element.click()
mine_field = MineField()    
mine_field.find_mines()
time.sleep(5)
driver.quit()
