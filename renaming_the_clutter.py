import os

fi=os.listdir("file")
i=1
for f in fi:
    if f.endswith(".png"):
        print(f)
        os.rename(f"pic/{f}","pic/{i}.png")
        i+=1