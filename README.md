# Sportia - Aplicativo Web de Ventas en Línea de Artículos Deportivos

Sportia es una aplicación web desarrollada con Flask y Bootstrap que permite a los propietarios de tiendas de artículos deportivos vender sus productos en línea. Los propietarios pueden ingresar, editar, consultar y eliminar datos de productos a través de una cuenta de administrador. La aplicación también proporciona una experiencia de compra fácil y segura para los clientes.

## Desarrolladores

- Elkin Ramírez
- Carlos Solorzano
- Heider Orozco
- Camilo Baute
- Didier Padilla
- Kendy Alfaro

## Funcionalidades Principales

El proyecto Sportia tiene un backlog con las siguientes funcionalidades clave:

1. **Implementación del Backend con Flask:** Se ha desarrollado el backend de la aplicación utilizando el framework Flask para gestionar las rutas y la lógica de negocio.

2. **Conexión a la Base de Datos con MySQL:** Se establece una conexión a una base de datos MySQL para almacenar información sobre los productos, clientes y pedidos.

3. **Creación del Login:** Los usuarios pueden autenticarse en la aplicación utilizando un sistema de inicio de sesión.

4. **Diseño e Implementación de Bootstrap:**
   - Diseño de la página de inicio con una selección de productos destacados.
   - Diseño de la página del administrador para gestionar productos.
   - Diseño de una página de confirmación de compra exitosa.
   
5. **Manual de Usuario:** Se crea un manual de usuario que describe cómo usar la aplicación tanto para los propietarios como para los clientes.

6. **CRUD de Productos:** Los propietarios pueden realizar operaciones de Crear, Leer, Actualizar y Eliminar (CRUD) productos en su tienda en línea.

7. **Creación e Implementación del Carrito de Compras:** Los clientes pueden seleccionar productos y agregarlos a su carrito de compras. Luego, pueden proceder a la compra y recibir una confirmación de la compra exitosa.

## Uso de la Aplicación

### Propietario del Negocio

- Iniciar sesión en la aplicación como administrador.
- Gestionar productos: Agregar nuevos productos, actualizar detalles y eliminar productos existentes.

### Cliente

- Explorar los productos disponibles en la tienda.
- Agregar productos al carrito de compras.
- Proceder al pago y recibir una confirmación de compra exitosa.

## Configuración y Ejecución

Para ejecutar Sportia en tu entorno local, sigue estos pasos:

1. Asegúrate de tener Python y Flask instalados en tu sistema.

2. Clona el repositorio de Sportia desde GitHub.

    git clone https://github.com/tuusuario/sportia.git

3. Crea un entorno virtual y actívalo.

    python -m venv venv
    source venv/bin/activate # En Windows, utiliza "venv\Scripts\activate"

4. Instala las dependencias del proyecto.

    pip install -r requirements.txt

5. Configura la conexión a la base de datos MySQL en el archivo de configuración.

6. Ejecuta la aplicación.

    flask run

7. Abre un navegador web y accede a la aplicación en `http://localhost:5000`.

## Contribuciones

Si deseas contribuir al proyecto Sportia, no dudes en crear un fork del repositorio y enviar tus pull requests. ¡Esperamos que esta aplicación sea útil para ti y para los propietarios de tiendas de artículos deportivos!
