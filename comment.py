class Comment:
    # comment symbols to test for
    singleSymbols = ['//', '#'];
    blockSymbols = ['/*', '//', '#', "'''"];
    # constructor
    def __init__(self, text, index):
        # set text
        self.text = text.strip();
        # set line number
        self.index = index;
        # checks if it is a python comment
        self.isPython = self.isPython();
        # find initial property states
        self.hasTODO = self.hasTODO();
        self.isSingleComment = self.isSingleComment();
        self.isBlockLine = self.isBlockLine();
        # checks if it was counted as a block comment
        self.wasCounted = False;

    # for determining file type
    def isPython(self):
        return '#' in self.text[0];

    # determines if "TODO" is in the comment
    def hasTODO(self):
        return ("TODO" in self.text);

    # checks if single line
    def isSingleComment(self):
        # compares each symbol
        for symbol in self.singleSymbols:
            # if contained, single comment occurs
            if symbol in self.text is not False : return True;
        return False;

    # checks if part of comment block
    def isBlockLine(self):
        for symbol in self.blockSymbols:
            # if the comment is single line and contains the symbol, but not at the start OR
            # contains both open and closing block characters (/* and */) but neither at the start
            # e.g. print("test") /* inline comment */
            if (symbol in self.text[1:] and (self.isSingleComment
            or (self.blockSymbols[0] in self.text[1:] and self.blockSymbols[0][::-1] in self.text[1:]))) : return True;
        return False;
