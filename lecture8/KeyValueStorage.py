class KeyValueStorage(dict):
    def __init__(self, file_name):
        super().__init__()
        with open(file_name) as f:
            content = f.readlines()
        self.name: str = [line.split("=")[1].strip() for line in content if line.split("=")[0].__eq__("name")][0]
        self.last_name: str = [line.split("=")[1].strip() for line in content if line.split("=")[0].__eq__("last_name")][0]
        self.song: str = [line.split("=")[1].strip() for line in content if line.split("=")[0].__eq__("song")][0]
        self.power: int = int([line.split("=")[1].strip() for line in content if line.split("=")[0].__eq__("power")][0])

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


storage = KeyValueStorage("path_to_file.txt")


print(storage.name)
print(storage.last_name)
print(storage['song'])
print(storage['power'])


def ddd():
    with open("path_to_file.txt") as f:
        return f.readlines()


ff = ddd()
# print(ff)
