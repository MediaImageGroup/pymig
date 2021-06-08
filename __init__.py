"""
Copyright (c) Billal Fauzan 2021 <billal.xcode]@gmail.com>
"""

import sys
import json
import time
import threading
from parser.JPGParser import JPGParser
from utils import (format_columns, format_openImage, format_rows,
                    generate_tabs, format_version, format_urls)

class Encoder:
    def __init__(self, data):
        self.data = data
        self.outputs = ""
        self.rows_data = ""
        self.columns_data = ""

    def reset(self):
        # Reset memory in variable
        self.outputs = ""
        self.rows_data = ""
        self.columns_data = ""

    def rgbdata(self, value):
        outs = ""
        length = len(value)
        for x in range(0, int(length)):
            outs += str(value[x])
            if x != (length - 1):
                outs += ","
            
        outs = "RGB:" + outs
        return outs

    def calculateTime(self, ctime):
        totalTime = str(time.time() - ctime)
        spltsTime = totalTime.split(".")
        if len(spltsTime[0]) == 1:
            current = totalTime[:3]
        elif len(spltsTime[0]) == 2:
            current = totalTime[:4]
        elif len(spltsTime[0]) == 3:
            current = totalTime[:5]
        elif len(spltsTime[0]) == 4:
            current = totalTime[:6]
        print (f"\nTotal time: {current}s")

    def convert(self):
        ctime = time.time()
        width = self.data["width"]
        height = self.data["height"]
        data = self.data["data"]
        row_index = 0
        rows_data = ""
        for rows in data:
            column_index = 0
            column_data = ""
            for column in rows["pixels"]:
                column_index += 1
                print (f"\rConverting rows: {rows['row']} Column: {column_index}", end=" ")
                column_data += format_columns % (column_index, self.rgbdata(column))
            rows_data += format_rows % (rows["row"], column_data)
        self.outputs += format_openImage % (format_version, format_urls, width, height, rows_data)
        self.calculateTime(ctime)
        
        return self.outputs

    def save(self, filename, data=None):
        if data is None:
            data = self.convert()
        with open(filename, "w") as f:
            f.write(data)
            f.close()

class Main:
    def __init__(self, argv):
        self.filename = argv[1]
        self.jpgparser = JPGParser()

    def read(self):
        self.rgbpixels = self.jpgparser.parseRGB(self.filename)
        return Encoder(self.rgbpixels)

if __name__ == "__main__":
    main = Main(sys.argv)
    reader = main.read()
    data = reader.convert()
    reader.save("imgs/results.mig", data)