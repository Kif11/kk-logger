# Python Logger

Small and simple logger to use in your Python projects.

You can install it as a git submodule for yor repository like this:
```bash
git submodule add https://github.com/Kif11/kk-logger modules/logger
touch modules/__init__.py
```

In Python script:
```python
from modules.logger import Logger
log = Logger()

log.info('Hello I your logger!')
```

You can specify options like this:
```python
from modules.logger import Logger
log = Logger(name='MyApp', log_time=True)

log.info('Hello I your logger!')
log.debug('Debug information: ', '"this is debug info body"')
```
