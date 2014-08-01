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

for lvl in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
    logger_demo.logger.setLevel(lvl)
    for lvl2 in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
        print("\n" + " -- " * 2 + "{:^50}".format(
            "logger set to {} handler set to {}".format(lvl, lvl2)) + " -- " * 2)
        h.setLevel(lvl2)
        logger_demo.logger.debug('foo')
        logger_demo.logger.info('foo')
        logger_demo.logger.warning('foo')
        logger_demo.logger.error('foo')
        logger_demo.logger.critical('foo')
