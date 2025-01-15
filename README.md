# certificacion

## Ejecutar el proyecto

- descargar archivo Alvaro_Navarrete_0075.zip
- crear un entorno virtual llamado "sistema"
- activar el entorno virtual ..\sistema\Scripts\activate
- instalar los siguientes modulos: Django y spycopg2

- descomprimir el archivo Alvaro_Navarrete_0075.zip
- crear la base de datos llamada "template" en postgres
- cargar el dump llamado datos.dump en la base de datos recien creada con la siguiente instruccion: 
- pg_restore -U <Usuario> -h <Host> -d template -F c -1 datos.dump
- entrar a la carpeta desde un terminal cd template-main
- configurar el archivo setting.py del sistema ubicada en certificacion/proyecto/setting.py

``` 
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'template',
    'USER': '<Tu usuario>',
    'PASSWORD': '<tu clave>',
    'HOST': '<tu host>', 
    'PORT': '5432',    
    }
}
```

- ejecutar el programa con el siguiente comando python manage.py runserver
- Los usuarios para ingresar al sistema estan escritos en el punto de mas abajo "Usuarios por rol"

## Usuarios por rol
- Rol : usuario / clave
- administrador : admin / admin

