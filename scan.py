from comment import *

# (global) comment symbols to test for
commentSymbols = ['#', '//', '/*', '*/', '*'];

<<<<<<< HEAD
# (global) a check for whether the file is python
isPython = False;

def commentCount(comments, lines, numLines):
    # declaration to check for file
    global isPython;
=======
def commentCount(comments, lines, numLines):
    isPython = False;
>>>>>>> 7fd2464d64df67db968ef16bc2262d5ffbbcf61e
    # counters for each property
    hasTODO = 0;
    singleComments = 0;
    blockComments = 0;
    blockLine = 0;
    # iterate through comments
    prevComment = None;
<<<<<<< HEAD
    temp_counter = 0;
=======
>>>>>>> 7fd2464d64df67db968ef16bc2262d5ffbbcf61e
    for comment in comments:
        # determine whether it is python or not
        if(isPython is False and comment.isPython):
            isPython = True;
        # increment depending on properties
<<<<<<< HEAD
        if comment.hasTODO is not False :
            hasTODO += 1;
        # we can determine if comment is part of a block based on the following:
        # 1. if a previous comment exists and is not inline
        # 2. both previous and current comments are back-to-back and
        # 3. both are single comments
        if (prevComment is not None and prevComment.isBlockLine is False and
        (prevComment.index == comment.index - 1) and comment.isSingleComment and prevComment.isSingleComment):
            blockComments += wasCounted(prevComment) + wasCounted(comment);
        # is a single one line comment
        if comment.isSingleComment: singleComments += 1;
        # is a block line (inline) comment
        if comment.isBlockLine is not False : blockLine += 1;
        # store previous comment
        prevComment = comment;
    return singleComments, blockComments, blockLine, hasTODO

def wasCounted(comment):
    # if the comment hasnt been counted as being a block
    if comment.wasCounted is False:
        # modify and send value
        comment.wasCounted = True;
        return 1;
    return 0;
=======
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
>>>>>>> 7fd2464d64df67db968ef16bc2262d5ffbbcf61e

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
    # (with as the file stream is unmanaged
    # and cleans up even if exceptions are thrown)
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
<<<<<<< HEAD
            # get global file type
            global isPython;
            # modify calculation depending on file type
            if(isPython is False): numBlockComments = numComments - numSingleComments;
            else: numSingleComments -=numBlockComments;
            # display results
            print("Total # of single line comments:", numSingleComments);
            print("Total # of comment lines within block comments:", numBlockComments);
=======
            print("Total # of single line comments:", numSingleComments - numBlockComments);
            print("Total # of comment lines within block comments:", numComments - numSingleComments + numBlockComments);
>>>>>>> 7fd2464d64df67db968ef16bc2262d5ffbbcf61e
            print("Total # of block line comments:", numBlockLine);
            print("Total # of TODO's: ", numTODO);

# run code
fileScan();
