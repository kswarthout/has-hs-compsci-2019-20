class Kangaroo:

    def __init__(self, pouch_contents=None):
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = pouch_contents

    def put_in_pouch(self, item):
        if item not in self.pouch_contents:
            self.pouch_contents.append(item)

    def __str__(self):
        ret_str = 'Pouch Contents: '
        for item in self.pouch_contents:
            ret_str += '{ ' + str(item) + ' }'
        return ret_str

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)

print(kanga)
        
