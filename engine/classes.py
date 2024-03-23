import threading
import json
import engine.start_service
        

class Service:
    def __init__(self, config) -> None:
        self.config = config
        self.isRunning = False
        self.thread = None

        self.configure()

    @classmethod
    def from_config(cls, name):
        """Create a service from a configuration."""
        with open("services/{}/config.json".format(name), "r") as f:
            config = json.load(f)
        return cls(config)

    def configure(self):
        """Configure the service."""
        config = self.config
        
        # Gather information
        self.name = config["name"]
        self.port = config["port"]
        self.lang = config["lang"]
        self.pub_router = config["pub_router"]

        # assert
        assert self.lang in engine.start_service.lang, "Unsupported language"


    def start(self):
        """Start the service."""

        starter = engine.start_service.lang[self.lang]
        self.thread = threading.Thread(target=starter, args=(self.config,))

        # run the service
        self.isRunning = True
        self.thread.start()
