from errors import ObjectError

# Format images
format_version = "1.0"
format_urls = ""
format_openImage = '<img version="%s" urls="%s" width="%d" height="%d">%s\n</img>'
format_rows = '\n\t<row id="%d">%s\n\t</row>'
format_columns = '\n\t\t<column id="%d">%s</column>'
format_newline = "\n"

def generate_tabs(total):
    format_tabs = ["\t" for _ in range(total)]
    return "".join(format_tabs)

# Check object target
def check_byte(value):
    if isinstance(value, bytes):
        return True
    else:
        raise ObjectError("bytes")

def check_string(value):
    if isinstance(value, str):
        return True
    else:
        raise ObjectError("string")
    
def check_integer(value):
    if isinstance(value, int):
        return True
    else:
        raise ObjectError("integer")

def check_list(value):
    if isinstance(value, list):
        return True
    else:
        raise ObjectError("lists")

def check_dict(value):
    if isinstance(value, dict):
        return True
    else:
        raise ObjectError("dictionary")