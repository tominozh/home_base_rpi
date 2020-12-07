from ..common.exceptions import ValidationError
from dicttoxml import dicttoxml
from ..common import constants
import re, logging, xmltodict, json
from decimal import Decimal


def clean_data(value):
    if value is None:
        return None

    for entity, replacement in constants.REPLACEMENTS:
        value = value.replace(entity, replacement)
    # value = value.replace(u'\xa0', '')

    value = re.sub('\t', '', value)
    value = re.sub('\n', '', value)
    value = re.sub('\r', '', value)
    value = re.sub(' +', ' ', value)
    value = value.strip()

    return value


def is_empty(str):
    if str is None or str == '':
        return True
    else:
        return False


def get_parameter(request, name, required=False):
    value = request.args.get(name)

    if value is None:
        if request.json is not None:
            reg = request.json.get(name)

    if value is None and required:
        raise ValidationError('Missing %s' % name)
    else:
        value = clean_data(value)
        return value


def dict_to_xml(dict_data, custom_root=None, root=True):
    if dict_data is None:
        raise ValidationError('Missing dict data')
    xml = dicttoxml(dict_data, custom_root=custom_root, attr_type=False, root=root)
    return xml


def json_to_xml(json_data, custom_root=None, root=True):
    if json_data is None:
        raise ValidationError('Missing json data')
    return dict_to_xml(dict(json_data), custom_root, root)


def xml_to_dict(xml):
    if xml is None:
        raise ValidationError('Missing xml data')
    json_str = json.dumps(xmltodict.parse(xml))
    return json.loads(json_str)


# both 3.00 and 3.03 are true, but 3 is false
def is_float(value):
    try:
        x = float(value)
        if '.' in str(value):
            return True
        else:
            return False
    except ValueError:
        type(value)
        return False


# 3.00 will return false, 3.01 will be true
def is_decimal(value):
    if is_float(value):
        return (Decimal(value) % 1 != 0)
    else:
        return False


def is_int(value):
    try:
        x = int(value)
        return True
    except ValueError:
        return False


# this method will remove everything except digits.
# It also removes dot, so pls be careful. e.g    3.8aaabbbccc -> 38
def keep_only_digits(value):
    if value is None:
        return value
    return re.sub(r"\D", "", value)


def get_first_digit_index(value):
    m = re.search("\d", value)
    if m:
        return m.start()
    else:
        return None


def match_regex(regex, value):
    m = re.match(regex, value)
    if m:
        return True
    else:
        return False


def replace_str(from_str, to_str, str):
    return str.replace(from_str, to_str)


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

