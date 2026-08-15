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
        with open('agent_creations/' + filename + '.' + extension, 'w', encoding='utf-8') as file:
            file.write(content)
        return 'Success'
    except Exception as e:
        return 'Error: ' + str(e)