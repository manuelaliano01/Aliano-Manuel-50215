Proyecto: Inventario interno para almacén

Autor: Juan Manuel Aliano
Fecha: 27/03/2024
Versión: 1.0

Objetivo:

El objetivo del proyecto es llevar un control de stock de los distintos productos que tiene el inventario de nuestra tienda modelo. En este trabajo, podremos buscar, agregar o eliminar los artículos que deseemos a partir de un registro de usuario. 

Consideraciones:
Librerias con sus versiones utlizadas: 

- asgiref    3.7.2
- Django     5.0.2
- pillow     10.2.0
- pip        24.0
- setuptools 69.0.3
- sqlparse   0.4.4
- tzdata     2024.1

Modelos usuados:

- Almacén: En este modelo contamos con un campo de texto (CharField) que registra el nombre del producto. Un campo decimal (DecimalField) que registra el precio del producto. Un campo entero (IntegerField) que registra la cantidad disponible del producto en el inventario.

- Bebidas: En este modelo contamos con un campo de texto (CharField) que registra el nombre del producto. Un campo decimal (DecimalField) que registra el precio del producto. Un campo entero (IntegerField) que registra la cantidad disponible del producto en el inventario.

- Verduras: En este modelo contamos con un campo de texto (CharField) que registra el nombre del producto. Un campo decimal (DecimalField) que registra el precio del producto. Un campo entero (DecimalField) que registra la cantidad disponible del producto en el inventario.

- Frutas: En este modelo contamos con un campo de texto (CharField) que registra el nombre del producto. Un campo decimal (DecimalField) que registra el precio del producto. Un campo entero (DecimalField) que registra la cantidad disponible del producto en el inventario.

NOTA |  En los primeros dos casos al tratarse de productos que se venden por unidad, registré su cantidad a partir de enteros. En los casos de la fruta y la verdura, me resultó más atinado contabilizar su cantidad con valores numéricos decimales ya que puede venderse, en algunos casos, menos de un kilo.

- Avatar: En este modelo la clase Avatar representa un avatar asociado a un usuario. Contiene un campo de imagen para la imagen del avatar y una clave externa que se relaciona con el modelo de usuario de Django.




