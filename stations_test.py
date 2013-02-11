import stations

shifted = [
    'abc',
    'bcd',
    'cde',
    'def',
    'efg',
    'fgh',
    'ghi',
    'hia',
    'iab'
]
def test_convert_back():
  solver = stations.Solver(shifted)
  for i in range(255):
    s = solver.alphabets.int_to_set(i)
    assert solver.alphabets.set_to_int(s) == i
