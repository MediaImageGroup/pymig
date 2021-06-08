class ObjectError(Exception):
    def __init__(self, o):
        print (f"Terjadi kesalahan pada objek: {o}")

class DataError(Exception):
    pass

class FileError(Exception):
    pass