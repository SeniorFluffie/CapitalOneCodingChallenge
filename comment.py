class Comment:
    # comment symbols to test for
    singleSymbols = ['#', '//'];
    blockSymbols = ['/*', '//', '#']
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
        # compares each symbol
        for symbol in self.singleSymbols:
            # if contained, single comment occurs
            if symbol in self.text is not False : return True;
        return False;

    # checks if part of comment block
    def isBlockLine(self):
        for symbol in self.blockSymbols:
            # as the text is stripped anyway, as long as the comment
            # is not at the start, it is considered a "block" comment
            if not self.text.startswith(symbol) and symbol in self.text[1:] : return True;
        return False;
