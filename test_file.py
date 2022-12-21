import file as SUT

def test_divideFunc_valid():
  assert SUT.divideFunc(5,2) == 2.5
  
def test_divideFunc_divideByZero():
  assert SUT.divideFunc(5,0) == 0
