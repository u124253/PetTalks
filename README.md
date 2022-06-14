PetTalks
========= 

PetTalks es una aplicacion que permite a los animales hablar.

Hacemos uso del repositorio de  Github smstools https://github.com/MTG/sms-tools
especificamente, usaremos las funciones que permiten realizar morphs 
(transformaciones) de audios.

El proyecto contara con grabaciones predefinidas y voces de animales escogidas 
de tal manera que el resultado que produzca PetTalks sea correcto. 

Para usarlo
----------
Instalar Python version 3.7.x y los siguientes modulos: ipython, numpy, matplotlib, scipy, y cython
  
  Para instalarlos, usar terminal o API
  
    3.1. En Ubuntu: <code>$ sudo apt-get install python-dev ipython python-numpy python-matplotlib python-scipy cython</code>
  
    3.2. En OSX: <code>$ pip install ipython numpy matplotlib scipy cython</code>
         Compilar las funciones de C siguientes: software/models/utilFunctions_C 
         y después usar: $ python compileModule.py build_ext --inplace

Requisitos mínimos
----------
8Gb Ram
CPU intel i3 o AMD Ryzen 3
Almacenamiento mínimo: 1 Gb


### Content
all the code is available in the software directory

### License

All the software is distributed with the Affero GPL license (http://www.gnu.org/licenses/agpl-3.0.en.html), the lecture slides are distributed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0) license (http://creativecommons.org/licenses/by-nc-sa/4.0/) and the sounds in this repository are released under Creative Commons Attribution 4.0 (CC BY 4.0) license (http://creativecommons.org/licenses/by/4.0/)
