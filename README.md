# Landing de la Biodiversidad de Boyacá y Cundinamarca

Este proyecto es una landing page para mostrar algunos aspectos relevandes de la biodiversidad de los departamentos de Boyacá y Cundinamarca, diseñada para presentar una interfaz moderna y llamativa, que pretende mostrar algunas especies de la biodiversidad de éstos departamentos, imágenes y descripcion de sus principales caracterísiticas, así como mapas interactivos con ejemplos de algunas especies, y una gráfica que muesta los municipios con mayor numero de especies vistas y reportadas. La landing page busca captar la atención de los visitantes y mtivarlos para que aporten en la conservación de la biodiversidad.

## Tech Stack

Para este proyecto se implementaron varias herramientas y tecnologías de desarrollo que permitieron construir una solución eficiente, dinámica y visualmente atractiva para la generación de gráficos en tiempo real desde una aplicación web.

![JavaScript](https://img.icons8.com/?size=40&id=PXTY4q2Sq2lG&format=png&color=000000)

![Python](https://img.icons8.com/?size=40&id=13441&format=png&color=000000)

![Flask](https://img.icons8.com/?size=40&id=ewGOClUtmFX4&format=png&color=000000)

![Pandas](https://img.icons8.com/?size=40&id=xSkewUSqtErH&format=png&color=000000)

![Pandas]()

### Python y algunos frameworks para el Backend

- **Python** fue el lenguaje principal utilizado para construir el backend, y mediante el uso de frameworks se creó el servidor, el routing del backend, la API con el método GET, se realizó la manipulación de los datos y la creación de gráficas. A continuación amplio la explicación del uso de los frameworks.

- **Flask**, un framework ligero y flexible de Python, se utilizó para crear el servidor web que actúa como API, y generar las rutas para acceder a la información y poder consumir la misma desde el frontend.

- **Pandas** es una librería especializada en el análisis y manipulación de datos en Python. En este proyecto, Pandas permitió gestionar y filtrar los datos de entrada, cargándolos en estructuras de datos (DataFrames) y preparando la información necesaria para crear gráficos de barras.

- **Matplotlib** es una librería de visualización en Python utilizada para crear gráficos detallados y personalizables. En este proyecto, Matplotlib se empleó para generar gráficos de barras, ajustando aspectos como el color, tamaño de las barras, etiquetas, cuadrículas y títulos. Los gráficos generados son luego guardados en un buffer y enviados al frontend como imágenes.

### HTML, CSS y JavaScript para el Frontend

- **HTML** se utilizó para estructurar la página web.

- **CSS** permitió estilizar y hacer atractiva la interfaz visual, personalizando la apariencia de los elementos y la disposición del contenido en pantalla.

- **JavaScript** se empleó para interactuar con el servidor Flask mediante peticiones HTTP, permitiendo obtener y mostrar los datos de biodiversidad de los departamentos de Boyacá y Cundinamarca, y mostrar los gráficos.
