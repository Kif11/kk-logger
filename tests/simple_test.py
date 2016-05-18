from logger import Logger

log = Logger(name='STEST')

log.info('This is info message')
log.debug('This is debug message')
log.error('This is error message')
log.warning('This is warning message')
log.success('This is success message')

log.info('This', ' is ', 'multyarg info')


class SimpleObject(object):
    def __init__(self):
        self.msg = 'Hi I am an object'
    def __repr__(self):
        return self.msg

my_array = ['a1', 2, ]
log.info('This is and array: ', my_array)
log.debug('This is and array: ', my_array)
log.error('This is and array: ', my_array)
log.warning('This is and array: ', my_array)
log.success('This is and array: ', my_array)

log.info('Hi I an a dictionary: ', {'item1': 123, 'item2': 'apple'})

obj = SimpleObject()
log.info(obj)
log.debug(obj)
log.error(obj)
log.warning(obj)
log.success(obj)


class PureObject(object):
    def __init__(self):
        self.msg = 'Hi I am a pure object'
    def useless_function(self):
        # Doesn't return anithing
        pass
    def none_function(self):
        return None

po = PureObject()
log.info('PureObject: ', po, '!!!')
log.info('PureObject void func: ', po.useless_function(), '!!!')
log.info('PureObject none func: ', po.none_function(), '!!!')
