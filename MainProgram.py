from RaspberrySdk import RaspberrySdk
import logging, logging.config
import sched, time
from EmailUtil import email


class MainProgram:
    logging.config.fileConfig("logging.ini")
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.trigger_gpio_pin = 7
        self.water_period_in_hour = 8
        self.water_time_in_min = 1
        self.raspberry = RaspberrySdk()
        self.raspberry.output(self.trigger_gpio_pin)

    def finish_watering(self):
        email()

    def water(self):
        success = False;
        try:
            self.raspberry.low(self.trigger_gpio_pin)
            self.logger.info("Watering is started.")
            time.sleep(self.water_time_in_min * 60)
            success = True
        except:
            self.logger.warning("Failed to start watering.")
        finally:
            self.raspberry.high(self.trigger_gpio_pin)

        if success:
            self.logger.info("Watering is completed successfully.")
        else:
            self.logger.error("Failed to water.")

        self.finish_watering()

if __name__ == "__main__":
    m = MainProgram()
    m.water()
