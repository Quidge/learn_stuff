class HashTable():

  def __init__(self, size=1000):
    self.size = size
    self.table = [None] * size

  def hash(self, item):
    str_val = str(item)
    return len(str_val)

  def map_to_table(self, hash):
    pass


if __name__ == '__main__':
  ht1 = HashTable(size=5)
  print(ht1.hash(22))