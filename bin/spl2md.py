import os
import sys
import textwrap

def generateIndex( indexFile,  title,  url):

    if not os.path.exists(os.path.dirname(indexFile)):
        os.makedirs(os.path.dirname(indexFile))

    with open(indexFile, "a+") as f:
        f.write("<li><a href=\"" + url + "\">" + title + "</a></li>\n")

def nextUrl(url):
    return "<a class=\"button\" href=\"" + url + "\">"  + " > </a>"

def prevUrl(url):
    return "<a class=\"button\" href=\"" + url + "\">"  + " < </a>"

def writeButtons(f, prev, next):
    f.write("<div class=\"sampleNav\">")
    if len(prev) > 0:
        prevButton = prevUrl(prev)
        f.write(prevButton)

    if len(next) > 0:
        nextButton = nextUrl(next)
        f.write(nextButton + "\n")
    f.write("</div>\n\n")

def splToMd(splFile, mdFile, title, prev, next):

    with open(splFile, "r") as splF:
        content = splF.read()

    if not os.path.exists(os.path.dirname(mdFile)):
        os.makedirs(os.path.dirname(mdFile))

    with open(mdFile, "w+") as f:
        f.write("---\n")
        f.write("layout: samples\n")
        f.write("title: " + title + "\n")
        f.write("---\n\n")
        f.write("### " + title + "\n\n")

        writeButtons(f, prev, next)

        f.write("~~~~~~\n")
        f.write(content + "\n")
        f.write("~~~~~~\n\n")

        writeButtons(f, prev, next)

        print "Generated: " + mdFile

path = "/Users/chanskw/git/splexamples/SPL-Examples-For-Beginners"
outPath = "/Users/chanskw/git/streamsx.documentation/samples/spl-for-beginner"
spl = ".spl"
md = ".md"
index = os.path.join("/Users/chanskw/git/streamsx.documentation/_includes" + "/sampleIndex.html")
htmlPrefix = "/streamsx.documentation/samples/spl-for-beginner/"

if (os.path.exists(index)):
    os.remove(index)

indexList = []

for root, subdirs, files in os.walk(path):
    for oneFile in files:

        # for each file in the directories
        absPath = os.path.join(root, oneFile)
        relOutPath = os.path.relpath(absPath, path)

        splitted = relOutPath.split("/")

        # Find the sample name, sample name is the toolkit name of the sample
        sampleName = splitted[0]

        # Generate name of md file.  This file needs to be unique by namespace and composite name
        mdName = relOutPath.replace("/", "_")
        mdName = mdName.replace(".", "_")

        absOutPath = os.path.join(outPath, mdName + md)

        print absOutPath

        if absPath.endswith(spl):
            # HTML path must take md name
            htmlPath = htmlPrefix + mdName + "/"
            displayTitle = sampleName
            # Generate sampleIndex.html
            generateIndex(index, displayTitle, htmlPath)
            indexList.append(htmlPath)

i = 0
max = len(indexList)
print max

for root, subdirs, files in os.walk(path):
    for oneFile in files:

        # for each file in the directories
        absPath = os.path.join(root, oneFile)
        relOutPath = os.path.relpath(absPath, path)

        splitted = relOutPath.split("/")

        # Find the sample name, sample name is the toolkit name of the sample
        sampleName = splitted[0]

        # Generate name of md file.  This file needs to be unique by namespace and composite name
        mdName = relOutPath.replace("/", "_")
        mdName = mdName.replace(".", "_")

        absOutPath = os.path.join(outPath, mdName + md)

        if oneFile.endswith(spl):
            print i

            if i > 0:
                prev = indexList[i-1]
            else:
                prev=""

            if i < max-1:
                next = indexList[i+1]
            else:
                next=""

            # Generate the actual md file
            splToMd(absPath, absOutPath, sampleName, prev, next)

            i=i+1
