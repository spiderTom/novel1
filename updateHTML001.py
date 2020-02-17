# -*- coding: utf-8 -*-
import os
import string
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

folderName = "saves//"

if os.path.exists(folderName):
    pass
else:
    print("ERROR: the saves folder is not exist!!!")

targetString = []
prefix = "<dd class=\"clear\"><a href=\""
#/shu/114408/46824749.html
midfix = ".html\">"
postfix = "</a></dd>"
for i in range(1526):
    targetString.append(prefix + str(i + 2) + midfix + str(i + 1) + postfix)




with open ("saves\index.html",'r') as source:
    with open("saves2\index1.html",'w') as target:
        for x in source:
            if x.find("11111") != -1 :
                x = targetString
                for item in targetString:
                    target.write(item)
            else:
                target.write(x)

for i in range(1526):
    with open("saves\\" + str(i+2) + ".html", 'r') as source:
        with open("saves2\\" + str(i+2) + ".html", 'w') as target:
            for x in source:
                if x.find("上一章") != -1:
                    index1 = x.find("\"/shu")
                    index2 = x.find("\" title")
                    # index3 = x.find("上一章")
                    x = x[:index1] + "\"" + str(i + 1) + ".html" + x[index2:]
                elif x.find("下一章") != -1:
                    index1 = x.find("\"/shu")
                    index2 = x.find("\" title")
                    # index3 = x.find("上一章")
                    x = x[:index1] + "\"" + str(i + 3) + ".html" + x[index2:]
                target.write(x)



