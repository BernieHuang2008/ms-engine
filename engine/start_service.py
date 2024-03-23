def start_python3(config):
    """Start the python3 service."""
    path = "services/{}/{}".format(config["name"], config["entrypoint"])
    module = __import__(path)
    return module.start(config)

lang = {
    "python3": start_python3,
}