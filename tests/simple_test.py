from logger import Logger

log = Logger(name='STEST')

log.info('This is info message')
log.debug('This is debug message')
log.error('This is error message')
log.warning('This is warning message')
log.success('This is success message')

log.info('This', ' is ', 'multyarg info')
