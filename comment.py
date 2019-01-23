class Comment:
    def __init__(self, text):
        self.text = text;
        self.hasTODO = self.hasTODO();
        self.isSingleComment = self.isSingleComment();
        self.isBlockLine = self.isBlockLine();

    # if not in a block, must be a single comment
    isSingleComment = None;
    #
    isBlockLine = None;

    def hasTODO(self):
        return ("TODO" in self.text);

    def isSingleComment(self):
        return ("TODO" in self.text);

    def isBlockLine(self):
        return ("TODO" in self.text);
