# Way number 1, no lambda use & made myself

def getOSuffix(n):
  suffixList = ["th","st", "nd", "rd", "th", "th", "th", "th", "th", "th"]
  return str(n) + suffixList[n % 10]
  
  # Way number 2, uses lambda. Found on SO https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
  
  import math
  ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
