from comment import *

def commentCheck(line):
    commentIndicator = ['#', '//', '/*', '*'];
    for symbol in commentIndicator:
        if(symbol in line or line[1] == '*'):
            # do all the matching here
            # isSingleComment
            # hasTODO etc.
            return True;
    return False;

def segregateComments(filename):
    comments = [];
    with open(filename) as lines:
        for line in lines:
            if commentCheck(line) is not False : comments.append(Comment(line));
    return comments;

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

def checkFile(filename):
    # ignore hidden files or no extensions
    if('.' not in filename or filename[1] == '.'):
        return False;
    return True;

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
            print("Total # of lines: ", lineCount(path));
            comments = (segregateComments(path));

fileScan();
