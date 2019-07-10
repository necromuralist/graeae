class NestedDict:
    """builds nested dictionaries

    Args:
     separator: token to split the keys in the path-string
     dictionary: a starting dictionary
    """
    def __init__(self, separator: str="/", dictionary: dict=None) -> None:
        self.separator = separator
        self.dictionary = dictionary if dictionary else {}
        return
    
    def __getitem__(self, path: str):
        """Gets the item at the end of the path string

        Args:
         path: the keys separated by the separator
        """
        parent = self.dictionary
        keys = path.split(self.separator)
        for index, key in enumerate(keys):
            if type(parent) is dict:
                parent = parent[key]
            elif index == len(keys) -1:
                return parent
        if index == len(keys) - 1:
            return parent
        return parent[key]
    
    def __setitem__(self, path: str, value: object) -> None:
        """Sets the value to the end of the path

        Args:
         path: keys separated by the separator
         value: thing to set
        """
        keys = path.split(self.separator)
        parent = self.dictionary
        for key in keys[:-1]:
            if key in parent:
                parent = parent[key]
            else:
                parent[key] = {}
                parent = parent[key]
        parent[keys[-1]] = value
        return
