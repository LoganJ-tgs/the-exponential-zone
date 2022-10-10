from time import perf_counter
import plot_results
rangemin = 1
rangemax = 10000
testtimes = 10
base = 17

def expt(x, n):
  if n <=0:
    raise ValueError("less than zero")
  if n == 1:
    return x
  elif n % 2 == 0:
    result = expt(x, n//2)
    return result * result
  else:
    return x * expt(x, n-1)

def oldexpt(x, n):
  if n <=0:
    raise ValueError("less than zero")

  valofx = x
  for _ in range(n):
    valofx *= x
  return valofx


def runtest(func, exponent):
  mintime = 9999999999999
  for _ in range(testtimes): # run each test for the exponent
    recordedtime = perf_counter()
    func(base,exponent)
    elapsedtime = perf_counter() - recordedtime
    if mintime > elapsedtime:
      mintime = elapsedtime
      
  return mintime

def main():
  file = open("expt_data.csv", "w")
  file.write("exponent,min_runtime_new,min_runtime_old\n")
  for n in range(rangemin, rangemax + 1):
    expttime = runtest(expt, n)
    oldexpttime = runtest(oldexpt, n)
    string = "{},{},{}\n".format(n, expttime, oldexpttime)
    file.write(string)
    #print(string)
  file.close()
  plot_results.main()

if __name__ == "__main__":
  plot_results.main()
  print("yeah a print statement gonna type more filler for the hell of it this is a very long string it could even be the string of all time im not going to stop for a good while im still going see ma look at me go maybe i can get an english essay out of this so that i dont need to do the next one but this is gonna be long but probably not long enough this doesnt make any sense god help me alright im gonna stop.")
  #main()

def oldmain():
  tests = 10
  base = 9
  exponent = 10000
  averagetime = 0
  for _ in range(tests):
    recordedtime = perf_counter()
    expt(base,exponent)
    elapsedtime = perf_counter() - recordedtime
    averagetime += elapsedtime
  averagetime /= tests
  print("time to run new algorithm = {}".format(averagetime))

  averagetime2 = 0
  for _ in range(tests):
    recordedtime = perf_counter()
    oldexpt(base,exponent)
    elapsedtime = perf_counter() - recordedtime
    averagetime2 += elapsedtime
  averagetime2 /= tests
  print("time to run old algorithm = {}".format(averagetime2))


