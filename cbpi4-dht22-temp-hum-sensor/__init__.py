
# -*- coding: utf-8 -*-
import logging
import asyncio
from cbpi.api import *
import adafruit_dht
import time

logger = logging.getLogger(__name__)


@parameters([Property.Select(label="cpioPin", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], description="GPIO Pin connected to DHT22 data port"),
    Property.Select(label="Type", options = ["Humidity","Temperature"],description = "Select sensor type"),
    Property.Select(label="Interval", options=[1,5,10,30,60], description="Interval in Seconds")])


class CpbiDht22(CBPiSensor):

    def __init__(self, cbpi, id, props):
        super(CpbiDht22, self).__init__(cbpi, id, props)
        self.value = 0
        self.temp = 0
        self.humidity = 0

        self.cpioPin = int(self.props.get("cpioPin",17))
        self.Type = int(self.props.get("Type","Temperature"))
        self.Interval = int(self.props.get("Interval",5))
        
    async def run(self):

        dhtDevice = adafruit_dht.DHT22(self.cpioPin, use_pulseio=False)
        while self.running == True:
            try:
                temp = dhtDevice.temperature
                humidity = dhtDevice.humidity
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                logger.info(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.dhtDevice.exit()
                logger.error(error.args[0])
                raise error

            if self.Type == "Temperature":
                self.value = temp
            else:
                self.value = humidity

            self.log_data(self.value)
            self.push_update(self.value)

            await asyncio.sleep(self.Interval)
        
        self.dhtDevice.exit()
    
    def get_state(self):
        return dict(value=self.value)


def setup(cbpi):
    cbpi.plugin.register("DHT22_Sensor", CpbiDht22)
    pass