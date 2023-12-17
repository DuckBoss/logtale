import logtale.logtale as tale
import logtale.filter as filter


def main():
    logtale = tale.LogTale("example", "0.0.1", "./example.toml")
    logger = logtale.logger.getChild(__name__)
    logger.addFilter(filter.LogFilter(prepend_text=__name__))

    logger.debug("test - debug")
    logger.info("test - info")
    logger.warning("test - warning")
    logger.error("test - error")
    logger.critical("test - critical")

if __name__ == "__main__":
    main()
