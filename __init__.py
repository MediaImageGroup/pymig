"""
Copyright (c) Billal Fauzan 2021 <billal.xcode]@gmail.com>
"""

import sys
import json
import time
import threading
from parser.JPGParser import JPGParser
from crypto.ZLib import compress
from errors import (DataError, FileError)
from utils import (format_columns, format_openImage, format_rows,
                    generate_tabs, format_version, format_urls,
                    check_byte, check_string)

class Encoder:
    def __init__(self, data):
        self.data = data
        self.outputs = ""
        self.rows_data = ""
        self.columns_data = ""

    def reset(self):
        " Reset memory in variable "
        self.outputs = ""
        self.rows_data = ""
        self.columns_data = ""

    def rgbdata(self, value):
        """
        Convert RGB to custom data
        
        @value      RGB value
        """
        outs = ""
        length = len(value)
        for x in range(0, int(length)):
            outs += str(value[x])
            if x != (length - 1):
                outs += ","
            
        outs = "RGB:" + outs
        return outs

    def calculateTime(self, ctime):
        """
        Process converting to new format

        @ctime      Current Time
        """
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
        width = self.data["width"] # image with
        height = self.data["height"] # image height
        data = self.data["data"] # data pixel
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

    def save(self, filename, data=None, encrypt=True):
        """
        @filename   output file (recomended)
        @data       data converted
        @encrypt    encrypt data to zlib (recomended to make small filesize)
        """
        mode = "w" # default mode "w", "wb" to write byte
        if encrypt:
            if data is None:
                data = self.convert() # if data is null then automate get data
            data = compress(data.encode())

        if data is None or len(data) == 0 or len(str(data)) == 0:
            data = self.convert()
            if data == "":
                raise DataError("Data is null")
        if check_byte(data):
            mode = "wb" # change mode to byte mode
        elif check_string(data):
            mode = "w" # change mode to string mode
        else:
            raise DataError("Invalid data")
        
        with open(filename, mode=mode) as f:
            f.write(data)
            f.close()

class Main:
    def __init__(self, argv):
        self.filename = argv[1]
        self.jpgparser = JPGParser() 

    def read(self):
        self.rgbpixels = self.jpgparser.parseRGB(self.filename) # Parser RGB from JPG per pixels
        return Encoder(self.rgbpixels)

if __name__ == "__main__":
    main = Main(sys.argv)
    reader = main.read()
    data = reader.convert()
    reader.save("imgs/results.mig", data, encrypt=True)