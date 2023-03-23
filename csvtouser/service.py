import csv,os,datetime
from .models import UserInfo
from django.conf import settings

def someFunction(filepath):
    path = os.path.join(settings.LOCAL_FILE_DIR,'media' ,str(filepath.filepath))
    path = path.replace("\\", "/")
    file = open(path, "r")
    data = list(csv.DictReader(file, delimiter=","))
    filepath.status = 1
    filepath.save()
    file.close()
    for entry in data:
        try:
            date =datetime.datetime.strptime(entry['birthday'], '%m/%d/%Y')
            p = UserInfo.objects.create(name=entry['name'], birthday=date,gender =entry['gender'],email = entry['email'],street =entry['street'],city = entry['city'],state =entry['state'],zipcode=entry['zip'])
            continue
        except:
            print("some error")    
    print("done")