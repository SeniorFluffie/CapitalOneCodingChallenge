class Comment:
    # comment symbols to test for
    singleSymbols = ['#', '//'];
    blockSymbols = ['/*'];
    # constructor
    def __init__(self, text):
        # set text
        self.text = text.strip();
        # find initial property states
        self.hasTODO = self.hasTODO();
        self.isSingleComment = self.isSingleComment();
        self.isBlockLine = self.isBlockLine();

    # determines if "TODO" is in the comment
    def hasTODO(self):
        return ("TODO" in self.text);

    # checks if single line
    def isSingleComment(self):
        for symbol in self.singleSymbols:
            if symbol in self.text is not False : return True;
        return False;

    # checks if part of comment block
    def isBlockLine(self):
        for symbol in self.singleSymbols:
            if self.text.startswith(symbol) is True : return False;
        return True;
