def create_file(filename:str, extension:str, content:str) -> str:
    """"Create a file in the project"""
    """"
    Args:
    filename: Filename WITHOUT extension
    extension: The file extension
    content: The content to be written in the file

    Returns:
    'Success' if created with success, 'Error: ...' if not
    """
    if extension != 'py':
        return 'Error: Only python files can be created'
    if filename.__contains__('.'):
        filename = filename.split('.')[0]
    
    try:
        with open(filename + '.' + extension, 'w', encoding='utf-8') as file:
            file.write(content)
        return 'Success'
    except Exception as e:
        return 'Error: ' + str(e)


def read_file(filename:str, extension:str) -> str:
    """"Read the content of a file"""
    """"
    Args:
    filename: Filename WITHOUT extension
    extension: The file extension

    Returns:
    String of the content of file or Error
    """
    if extension != 'py':
        return 'Error: Only python files can be read'
    if filename.__contains__('.'):
        filename = filename.split('.')[0]

    try:
        with open(filename + '.' + extension, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return 'Error: ' + str(e)