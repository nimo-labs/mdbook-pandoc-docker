#!/bin/python3
import subprocess
import os


def includeFile(filename, destination_file):
    srcFile = open(filename, 'r')
    lines = srcFile.readlines()
    srcFile.close()
    destination_file.write("\n\n")
    for line in lines:
        if '%' == line[0]:
            includeFile(line[1:-1], destination_file)
        else:
            destination_file.write(line)

intermediateFileName = "./output.inter.md"
masterFileName = "/book/report.md"
outputFileName = "./output.pdf"
templateFileName = "/book/template/template.latex"
generalOptions = "--wrap=preserve"

masterFile = open(masterFileName, mode = 'r', encoding = 'utf-8-sig')
lines = masterFile.readlines()
masterFile.close()

destination_file = open(intermediateFileName, 'w')

for line in lines:
    if '%' == line[0]:
        includeFile(line[1:-1], destination_file)
    else:
        destination_file.write(line)
destination_file.close()

subprocess.run(["pandoc", generalOptions, "--listings", "--template", templateFileName, intermediateFileName, "-o", outputFileName])
os.remove(intermediateFileName)
