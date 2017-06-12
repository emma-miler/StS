import sound #own

def data(input, input2):
  f = open(str(input), 'r')
  soundf = f.read()
  soundf = soundf.replace(",", "")
  soundf = soundf.replace("[", "")
  soundf = soundf.replace("]", "")
  soundf = soundf.split()
  for x in range(0, len(soundf)):
    sound.play(int(soundf[x]), int(input2))
  f.close()