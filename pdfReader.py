# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:50:03 2017

@author: Asif
"""

import codecs
def ReadPdfFunc():
    with open("cv.txt") as pdfFile:
        for line in pdfFile:
            line = line.lower()
            if "cgpa" in line:
                print(line)
        pdfFile.close()


ReadPdfFunc()