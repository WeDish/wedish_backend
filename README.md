# wedish_backend

cities_light norint išsiimti šalis komanda:

```
python manage.py loaddata ../countries.json
```

## Weasyprint requires GTK libraries
In case of Windows you can download them [from here](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe).

-------------------------------------------
Graph models su pygraphviz
norint gauti modelį reikalinga komanda:

```
python manage.py graph_models -a -g -o my_project_visualized.png
```

Gali būti kad Windows naudotojai turės problemų Visual C/C++, tuomet skaitome https://pygraphviz.github.io/documentation/stable/install.html#windows-install ar http://www.graphviz.org/  

------------------------------------------------ 
