import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))

print(round(.70 * 1.05, 2))
