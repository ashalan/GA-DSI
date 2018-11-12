import logging
logging.basicConfig(filename='test.log', level=logging.INFO)
log = logging.getLogger(__name__)

log.debug('Very granular logging message, useful for debugging.')
log.info('Simple update on normal execution, e.g. "Processing record {} of {}"'.format(10,100))
log.warning('Youve seen these in sklearn, warning about methods being deprecated')
log.error('Logs an error message')
log.critical('Well this is an issue')
