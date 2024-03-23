import engine.classes
import time

services = []

for name in ["email"]:
    s = engine.classes.Service.from_config(name)
    s.start()
    services.append(s)


time.sleep(10)