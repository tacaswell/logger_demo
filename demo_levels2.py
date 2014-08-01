from __future__ import (division, print_function, unicode_literals,
                        absolute_import)

import logger_demo
import logging

# make handler + formatter
h = logging.StreamHandler()
form = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# attach the formatter to the handler
h.setFormatter(form)
# attach the handler to the logger
logger_demo.logger.addHandler(h)


# make second handler + formatter
h2 = logging.StreamHandler()
form2 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - h2')
# attach the formatter to the handler
h2.setFormatter(form2)
# attach the second handler to the logger
logger_demo.logger.addHandler(h2)


for lvl in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
    print(" -- " * 5 + "now set to {:^10}".format(lvl) + " -- " * 5)
    h2.setLevel(lvl)
    logger_demo.logger.debug('foo')
    logger_demo.logger.info('foo')
    logger_demo.logger.warning('foo')
    logger_demo.logger.error('foo')
    logger_demo.logger.critical('foo')
