from comment import *

# (global) comment symbols to test for
commentSymbols = ['#', '//', '/*', '*/', '*'];

def commentCount(comments, lines, numLines):
    isPython = False;
    # counters for each property
    hasTODO = 0;
    singleComments = 0;
    blockComments = 0;
    blockLine = 0;
    # iterate through comments
    prevComment = None;
    for comment in comments:
        # increment depending on properties
        if comment.hasTODO is not False : hasTODO += 1;
        if comment.isSingleComment is not False : singleComments += 1;
        # if both previous and current line are single line comments, they are blocks
        if (prevComment is not None and (prevComment.index == comment.index - 1) and
        comment.isSingleComment and prevComment.isSingleComment):
            if(prevComment.index is 0 or prevComment.index is numLines - 1): blockComments += 1;
            blockComments += 1;
        # is a block line (inline) comment
        if comment.isBlockLine is not False : blockLine += 1;
        # add extra counter if python
        if comment.isHash and not isPython:
            singleComments -= 1;
            isPython = True;
        # set temp variable
        prevComment = comment;

    # extra value
    singleComments += 1;
    return singleComments, blockComments, blockLine, hasTODO

def commentCheck(line):
    # compare each symbol
    for symbol in commentSymbols:
        # exception of the single * (body comments)
        if(symbol in line or line[0] == len(commentSymbols) - 1):
            return True;
    return False;

# analyze and split up comments
def segregateComments(filename):
    comments = [];
    fileLines = [];
    # iterate through file
    with open(filename) as lines:
        # keep track of file index
        for counter, line in enumerate(lines):
            # if a comment, add to the list
            if commentCheck(line) is not False : comments.append(Comment(line, counter));
            fileLines.append(line);
    return comments, fileLines;

# finds the number of lines in the file
def lineCount(filename):
    # iterate through lines in the file
    # (with as the file stream is unmanaged)
    # (and cleans up even if exceptions are thrown)
    with open(filename) as lines:
        # enumerates through lines, incrementing counter each time
        for counter, line in enumerate(lines):
            # do nothing
            pass;
        return counter + 1;

# checks if file should be read
def checkFile(filename):
    # ignore hidden files or no extensions
    if('.' not in filename or filename[1] == '.'):
        return False;
    return True;

# main method (scans file)
def fileScan():
    # get filename
    try:
        path = input("Please enter a file path: ");
    # handle interrupt
    except KeyboardInterrupt:
        exit();
    # check file
    if(checkFile(path)):
        # if valid, open it
        try:
            file = open(path, "r");
        # if incorrect path
        except IOError:
            # notify and re-ask
            print("Could not read file: ", path);
            fileScan();
        else:
            # calculate line count
            numLines = lineCount(path);
            print("Total # of lines: ", numLines);
            # split comments from other code
            comments, lines = (segregateComments(path));
            numComments = len(comments);
            print("Total # of comment lines: ", numComments);
            # intialize counters for TODO, single line comment,
            # and block comment checks
            numSingleComments = numBlockComments = numTODO = 0;
            numSingleComments, numBlockComments, numBlockLine, numTODO = commentCount(comments, lines, numLines);
            print("Total # of single line comments:", numSingleComments - numBlockComments);
            print("Total # of comment lines within block comments:", numComments - numSingleComments + numBlockComments);
            print("Total # of block line comments:", numBlockLine);
            print("Total # of TODO's: ", numTODO);

# run code
fileScan();
