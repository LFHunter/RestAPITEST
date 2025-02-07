
from Baselib.logger_manager import setup_logger
from AAPITest_Proj import TwitchPage
from AAPITest_Proj.config import driver_setting, log_config
import datetime
import time

class TestTwitch:
    now = datetime.datetime.now()
    logger = setup_logger(log_config, loggername="twitch_logger")

    @classmethod
    def setup_class(cls):
        cls.logger.info("Initial Test")
        cls.wda = WebDriverManager(driver_setting)
        cls.driver = cls.wda.driver
        cls.testpage = TwitchPage(cls.driver, cls.logger)
        cls.logger.info(f"generate TwitchPage")

    @classmethod
    def teardown_class(cls):
        time.sleep(10)
        cls.wda.close_driver()
        cls.logger.info("End Test")

    def setup_method(self, method):
        self.logger.info(f"----starting {method.__name__} execution----")

    def teardown_method(self, method):
        self.logger.info(f"----end {method.__name__} execution----")


    def test_go_to_twitch(self):
        self.testpage.get_twitch_page()

    def test_click_search_icon(self):
        self.testpage.click_browse_icon()

    def test_input_message_in_search_bar(self):
        self.testpage.input_text_in_searchbar(msg="StarCraft II")
        self.testpage.send_enter()

    def test_scroll_down_2_times(self):
        for _ in range(2):
            self.testpage.scroll_down(movepixels=800,wait_time=0)
        time.sleep(2)

    def test_select_one_streamer(self):
        self.testpage.accept_modal()
        self.testpage.click_streamer_in_top(1)

    def test_check_and_take_photo_the_streamer_page(self):
        self.testpage.wait_streamer_page_is_ready(timeout=20)
        self.testpage.take_screenshot("StarCraftII_streamer.png")







