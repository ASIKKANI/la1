import pandas as pd
from tkinter import filedialog,Tk
from PIL import Image
from PIL import ImageDraw
import tabulate
import os
r=Tk()
r.withdraw()
print("choose the csv file")
file_path=filedialog.askopenfilename()
df=pd.read_csv(file_path)
print("the csv file opened from path",file_path)
print("please choose the directory to save the image")
w=filedialog.askdirectory()
try:
    for i in range(df.size-1):
        img = Image.new('RGB', (1000, 150),(255,255,255))#image size
        d = ImageDraw.Draw(img)
        #tabular = tabulate.tabulate(df.iloc[i].fillna("ab")[1:], headers = 'keys', tablefmt = "grid")
        d.text((10, 10),"KURINJI SENIOR SECNDY SCHOOL    "+"\n"+str(df.iloc[i].fillna("ab")[1:]), fill=(0, 0, 0))#text position
        f1=df.loc[i,"NAME"]
        img.save(f"{w}//{f1}.png")
except KeyError:
    print(f"the images stored Sucessfully at {w}")
except IndexError:
    print(f"the images stored Sucessfully at {w}")
    pass