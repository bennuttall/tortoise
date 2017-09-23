from gpiozero import TimeOfDay, Energenie
from datetime import time
from signal import pause

daytime = TimeOfDay(time(8), time(18))
lamp = Energenie(1)

lamp.source = daytime.values
lamp.source_delay = 60

pause()
