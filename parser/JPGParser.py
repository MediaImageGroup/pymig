from PIL import Image
from common import convert2rgb

class JPGParser(object):
    def __init__(self) -> None:
        super().__init__()
        self.image = None

    def convert2RGB(self, img):
        pass

    def parseRGB(self, path):
        self.image = Image.open(path)
        if self.image is None:
            raise ValueError("Tidak dapat membaca gambar")
        else:
            width, height = self.image.size
            self.data = {}
            self.data["width"] = width
            self.data["height"] = height
            rows = []
            rgb_value = self.image.convert("RGB")
            for y in range(1, height, 1):
                data = {}
                data["row"] = y
                pixels = []
                for x in range(1, width, 1):
                    pixels.append(rgb_value.getpixel((x, y)))
                data["pixels"] = pixels
                rows.append(data)
            self.data["data"] = rows
            return self.data