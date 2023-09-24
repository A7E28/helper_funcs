def escape_markdown(text, entity_types=None):
    if text is None:
        return
    
    markdown_v2_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    escaped_text = ''
    
    for char in text:
        if char in markdown_v2_chars and (entity_types is None or char not in get_entity_chars(entity_types)):
            escaped_text += '\\' + char
        else:
            escaped_text += char
    
    return escaped_text

def get_entity_chars(entity_types):
    entity_chars = {
        'bold': ['*'],
        'italic': ['_'],
        'underline': ['_'],
        'strikethrough': ['~'],
        'code': ['`'],
        'link': ['[', ']', '(', ')']
    }
    
    chars = []
    for entity_type in entity_types:
        chars.extend(entity_chars.get(entity_type, []))
    
    return chars
