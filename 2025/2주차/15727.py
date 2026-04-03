L = int(input())
time = 0
while L == 0:
    if L - 5 > 0:
        L -= 5
        time += 1
    else:
      if L - 4 > 0:
        L -= 4
        time += 1
      else:
        if L - 3 > 0:
          L -= 3
          time += 1
        else:
          if L - 2 > 0:
            L -= 2
            time += 1
          else:
            if L - 1 > 0:
              L -= 1
              time += 1


print(time)