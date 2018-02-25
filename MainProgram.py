# from RaspberrySdk import RaspberrySdk
import logging, logging.config
import sched, time
from EmailUtil import email

class Main:
    logging.config.fileConfig("logging.ini")
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.trigger_gpio_pin = 7
        self.water_period_in_hour = 8
        self.water_time_in_min = 30
        # self.raspberry = RaspberrySdk()

    def finish_watering(self):
        email.email()

    def main(self):
        try:
            self.raspberry.low(self.trigger_gpio_pin)
            self.logger.info("Watering is started.")
            time.sleep(30 * 60)
            self.logger.info("Watering is finished.")
        except:
            self.logger.warning("Failed to start watering.")
        finally:
            self.raspberry.high(self.trigger_gpio_pin)
            self.finish_watering()

    if __name__ == "__main__":
        logging.info("Logging started")
        m = Main()
        m.finish_watering()
