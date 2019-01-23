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
        # find initial property states
        self.hasTODO = self.hasTODO();
        self.isSingleComment = self.isSingleComment();
        self.isBlockComment = self.isBlockComment();
        self.isBlockLine = self.isBlockLine();
        self.isHash = self.isHash();

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

    def isBlockComment(self):
        # if comment starts with a '#' symbol
        return self.text.startswith(self.blockSymbols[len(self.blockSymbols) - 1]);

    # checks if part of comment block
    def isBlockLine(self):
        for symbol in self.blockSymbols:
            # if the comment is not a hash comment, and is an inline comment
            if (symbol in self.text[1:]) : return True;
        return False;

    def isHash(self):
        return self.text[0] == '#';
