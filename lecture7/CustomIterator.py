import requests


class CustomIterator:
    def __init__(self):
        self.page = 1

    def __iter__(self):
        return self

    def __next__(self):
        make_dict = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page={self.page}").json()
        if not make_dict["Count"]:
            raise StopIteration
        else:
            self.page += 1
            return make_dict