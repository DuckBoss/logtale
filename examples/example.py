import logtale.logtale as t


def main():
    logger = t.LogTale("example", "v0.0.1", "./example.toml").logger
    logger.debug("test - debug")
    logger.info("test - info")
    logger.warning("test - warning")
    logger.error("test - error")
    logger.critical("test - critical")

if __name__ == "__main__":
    main()