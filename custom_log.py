def log(tag="", message=""):
    with open("logs.txt", "w+") as log:
        log.write(f"{tag}: {message}\n")