###  Tale - A python logging framework
A simple, easy to use logging framework that builds on top of the built-in logger module.

### Installation
``` bash
pip install tale
```

### Usage
``` python
import tale

logger = tale.Tale("<my_software_name>", "<my_software_version>", "<log_cfg_path>").logger
logger.debug("test - debug")
logger.info("test - info")
logger.warning("test - warning")
logger.error("test - error")
logger.critical("test - critical")
```
