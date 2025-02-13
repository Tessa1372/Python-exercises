
# Iterator problem

class NestedIterator:
    def __init__(self, nested_list):
        self.flattened = self._flatten(nested_list)
        self.index = 0

    def _flatten(self, nested_list):
        for sublist in nested_list:
            for item in sublist:
                yield item

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self.flattened)
            return value
        except StopIteration:
            raise StopIteration
nested_list = [[2, 4], [1, 6], [5]]
iterator = NestedIterator(nested_list)
for num in iterator:
    print(num)


# Context Manager problem

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()  


with FileHandler("anyfile.txt", "w") as file:
    file.write("Hello, this text is written using a context manager!")

print("File written successfully and closed automatically.")

