#!/bin/python3
import subprocess
import os

intermediateFileName = "./output.inter.md"
masterFileName = "/book/report.md"
outputFileName = "./output.pdf"
templateFileName = "/book/template/template.latex"

masterFile = open(masterFileName, mode = 'r', encoding = 'utf-8-sig')
lines = masterFile.readlines()
masterFile.close()

content = ""

for line in lines:
    if '%' == line[0]:
        srcFile = open(line[1:-1], 'r')
        content = content + "\n\n" +srcFile.read()
        srcFile.close()
    else:
        content = content + line
destination_file = open(intermediateFileName, 'w')
destination_file.write(content)
destination_file.close()

subprocess.run(["pandoc", "--listings", "--template", templateFileName, intermediateFileName, "-o", outputFileName])
os.remove(intermediateFileName)
