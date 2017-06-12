import os #in
import filemanager #own

def export(input):
    try:
      os.remove("export.STSDATA")
    except:
        pass
    f = open("export.STSDATA", 'w+')
    f.write(str(input))
    f.close()
    filemanager.delete()