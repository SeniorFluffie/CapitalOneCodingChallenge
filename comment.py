class Comment:
    # constructor
    def __init__(self, text):
        # set text
        self.text = text;
        # find initial property states
        self.hasTODO = self.hasTODO();
        self.isSingleComment = self.isSingleComment();
        self.isBlockLine = self.isBlockLine();

    # determines if "TODO" is in the comment
    def hasTODO(self):
        return ("TODO" in self.text);

    # checks if single line
    def isSingleComment(self):
        # TODO: Check for single comments
        return False;

    # checks if part of comment block
    def isBlockLine(self):
        # TODO: Check for block line comments
        return False;
