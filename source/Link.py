class Link:
    """
    Base Link implementation
    """

    def __init__(self, source=None, target=None):
        self.source = source
        self.target = target
        self.data = None

    def get_other(self, node):
        if node == self.source:
            return self.target
        elif node == self.target:
            return self.source
        else:
            # given node was not in this link
            return None


