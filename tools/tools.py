def create_file(filename:str, content:str) -> int:
    """"Create a file in the project"""
    """"
    Args:
    filename: Filename WITH extension
    content: The content to be written in the file

    Returns:
    0 if created with success, 1 if not
    """
    try:
        with open('agent_creations/' + filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception:
        return False