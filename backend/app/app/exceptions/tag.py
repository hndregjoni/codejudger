from typing import Union, List

class TagNotFoundException(Exception):
    """ A tag does not exist in the system """
    tag: Union[int, str]

    def __init__(self, tag: Union[int, str]):
        super().__init__(f"Tag {tag} not found")
        self.tag = tag