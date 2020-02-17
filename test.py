
with open("saves\\tom.txt", 'r') as source:
    with open("saves2\\tom.txt", 'w') as target:
        for x in source:
            if x.find("上一章") != -1:
                index = x.find("上一章")
                index1 = x.find("\"/shu")
                index2 = x.find("\" title")
                #index3 = x.find("上一章")
                x = x[:index1] + "\"2.html" +x[index2:]
                print(index, index1, index2)
                print(x)

            elif x.find("下一章") != -1:
                index = x.find("下一章")
                index1 = x.find("\"/shu")
                index2 = x.find("\" title")
                # index3 = x.find("上一章")
                x = x[:index1] + "\"2.html" + x[index2:]
                print(index, index1, index2)
                print(x)
            target.write(x)