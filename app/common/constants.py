__author__ = 'tomas'

WEATHER_PRESSURE="presure"
WEATHER_TEMP="temperature"
WEATHER_HUMIDITY="humidity"
WEATHER_TIME="time"

RED = "RED"
BLUE = "BLUE"
GREEN = "GREEN"
DHT11_temp = "DTH11_temperature"
DHT11_humidity = "DTH11_humidity"

VALUE_OFF = "off"
VALUE_ON = "on"

GPIO_PIN_21 = 21
GPIO_PIN_22 = 22
GPIO_PIN_20 = 20


ERROR_TYPE_BAD_REQUEST = 'Bad request'
ERROR_TYPE_UNAUTHORIZED = 'Unauthorized'
ERROR_TYPE_FORBIDDEN = 'Forbidden'
ERROR_TYPE_HTTP = 'HTTP error'
ERROR_TYPE_TIMEOUT = 'Request timeout'
ERROR_TYPE_NOT_FOUND = 'Not found'
ERROR_TYPE_PROCESSING = 'Processing error'
ERROR_TYPE_NO_RESPONSE = 'No response'
HTTP_CODE_401 = 401
HTTP_CODE_403 = 403
HTTP_CODE_404 = 404
HTTP_CODE_408 = 408
HTTP_CODE_500 = 500
VIN_LENGTH = 17
XML_ROOT_TAG='root'
REPLACEMENTS = [
    ("&quot;", "\""),
    ("&apos;", "'"),
    ("&amp;", "&"),
    ("&lt;", "<"),
    ("&gt;", ">"),
    ("&laquo;", "<<"),
    ("&raquo;", ">>"),
    ("&#039;", "'"),
    ("&#8220;", "\""),
    ("&#8221;", "\""),
    ("&#8216;", "\'"),
    ("&#8217;", "\'"),
    ("&#9632;", ""),
    ("&#8226;", "-"),
    (u'\xa0', '')
]
MINETYPE_TEXT_XML = 'text/xml'