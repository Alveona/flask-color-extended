flask-color-extended
===========
[![PyPI version](https://badge.fury.io/py/flask-color-extended.svg)](https://badge.fury.io/py/flask-color-extended) 
![GitHub stars](https://img.shields.io/github/stars/Alveona/flask-color-extended?style=social)

![](https://sun1-20.userapi.com/X8npCMHPcnaRGJ9AZcYvRzWZVj_toj2WqBgsEQ/PsFp0JavpSU.jpg)

flask-color-extended is an extension for Flask that improves the built-in web server with colors when debugging.  
Differs from original library (https://github.com/Teemu/flask-color) by including current time and overall response time.

Installing
----------

You can install this using pip.

````$ pip install flask-color-extended````

How to use
----------

There's an example of use in sample.py. Add two lines to your code:

```python
# Import this extension
from flask_color_extended import color

# Initialize extension with your app.
color.init_app(app)
```

Flask configuration *DEBUG* must be True for this extension to function. You can override this by setting *COLOR_ALWAYS_ON* true.

Configuration
-------------

- *COLOR_ALWAYS_ON*: Force extension on even if not in DEBUG mode
- *COLOR_PATTERN_GRAY*: Regular expression that matches static file requests (these requests are marked with gray color)
- *COLOR_PATTERN_HIDE*: Hides (_fully_) requests that match this regular expression.
