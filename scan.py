from comment import *

def commentCheck(line):
    # the testable comment symbols
    commentIndicator = ['#', '//', '/*', '*'];
    # compare each symbol
    for symbol in commentIndicator:
        # exception of the single * (body comments)
        if(symbol in line or line[len(commentIndicator) - 1] == '*'):
            # do all the matching here
            # isSingleComment
            # hasTODO etc.
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
            # analyze the comments
            print("Total # of lines: ", lineCount(path));
            comments = (segregateComments(path));

# run code
fileScan();
