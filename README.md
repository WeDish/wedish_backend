# wedish_backend

cities_light norint išsiimti šalis komanda:

```
python manage.py loaddata ../countries.json
```

## Weasyprint requires GTK libraries
In case of Windows you can download them [from here](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe).

## Graph models su pygraphviz
norint gauti modelį reikalinga komanda:

```
python manage.py graph_models -a -g -o my_project_visualized.png
```

Gali būti kad Windows naudotojai turės problemų Visual C/C++, tuomet skaitome https://pygraphviz.github.io/documentation/stable/install.html#windows-install ar http://www.graphviz.org/  

## Deployment'as su docker'iu
```
docker-compose build
docker-compose up -d
```
Išjungimas
```
docker-compose down
```

## Troubleshooting for project access on Windows, when project is launched via docker
```````````````````
1) Locate "hosts" file with file type "file" at "C:\Windows\System32\drivers\etc" location

2) Check "hosts" file properties, if needed uncheck "Read-only" checkbox

3) Edit file with Notepad/Wordpad or equivalent text editing software

4_a)At the end of opened "hosts" file add line "127.0.0.1   wedish.local" and save the file.
    If any administration rights messages pops up, confirm them
    Check "hosts" file type, if it changed from "Type" to "Text" go to file explorer "View" properties section and check "File name Extensions" option. The "hosts" file should have the "hosts.txt" extension. Rename "hosts" file by deleting ".txt" part. Confirm any warning messages. "hosts" file type should change to "Type"

4_b)If you have option to only save edited file as new file. Save it in new location
    "hosts" file type will be changed from "Type" to "Text", go to file explorer "View" properties section and check "File name Extensions" option
    The "hosts" file should have the "hosts.txt" extension
    Rename "hosts" file by deleting ".txt" part. Confirm any warning messages. "hosts" file type should change to "Type"
    Copy this new "hosts" file and paste it into "C:\Windows\System32\drivers\etc" location. Approve any warning messages

5) If "hosts" file successfully updated, got to file properties and check "Read-only" checkbox
6) Project can be launched via docker and accessed using and internet browser by inputting "http://wedish.local/"

## Stripe
```
Registruojam stripe sąsają.
www.stripe.com
```
Prisijungus, API keys surandame: 
https://dashboard.stripe.com/test/apikeys
```
Implementacija:
https://stripe.com/docs/checkout/quickstart