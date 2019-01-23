from comment import *

def commentCount(comments):
    # counters for each property
    hasTODO = 0;
    singleComments = 0;
    blockLine = 0;
    # iterate through comments
    for comment in comments:
        # increment depending on properties
        if comment.hasTODO is not False : hasTODO += 1;
        if comment.isSingleComment is not False : singleComments += 1;
        if comment.isBlockLine is not False : blockLine += 1;
    return hasTODO, singleComments, blockLine

def commentCheck(line):
    # the testable comment symbols
    commentIndicator = ['#', '//', '/*', '*'];
    # compare each symbol
    for symbol in commentIndicator:
        # exception of the single * (body comments)
        if(symbol in line or line[0] == len(commentIndicator) - 1):
            return True;
    return False;

# analyze and split up comments
def segregateComments(filename):
    comments = [];
    # iterate through file
    with open(filename) as lines:
        for line in lines:
            # if a comment, add to the list
            if commentCheck(line) is not False : comments.append(Comment(line));
    return comments;

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
            print("Total # of lines: ", lineCount(path));
            # split comments from other code
            comments = (segregateComments(path));
            numComments = len(comments);
            print("Total # of comment lines: ", numComments);
            # intialize counters for TODO, single line comment,
            # and block comment checks
            numSingleComments = numBlockComments = numTODO = 0;
            numSingleComments, numBlockComments, numTODO = commentCount(comments);
            print("Total # of single line comments:", numSingleComments);
            print("Total # of comment lines within block comments:", numComments - numSingleComments);
            print("Total # of block line comments:", numBlockComments);
            print("Total # of TODO's: ", numTODO);


# run code
fileScan();
