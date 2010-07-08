# EISULA #

**Sumario:** Prototipo *no oficial* para la Escuela de Ingeniería de Sistemas
de la [Universidad de Los Andes][] (EISULA).

## Historia ##

Este prototipo nace como un proyecto para la asignatura de *Sistemas
Computacionales* por allá en el 2007. Sin embargo, un día revisando en mis
respaldos me encontré este proyecto, uno con los cuales comencé a trabajar en
[Django][], he decidido retomarlo porque hasta ahora (2010) nuestra ilustre
escuela aún no cuenta con un portal que sirva como punto de encuentro entre
profesores y estudiantes de la Escuela de Ingeniería de Sistemas.

En el proyecto de la asignatura de *Sistemas Computacionales* participaron:

 * Ana Rangel <anita.rangel@gmail.com>
 * Laudin Molina <laudin.molina@gmail.com>
 * Nelson Grimaldos <coca.cola.adicto@gmail.com>
 * Mario Rincón Nigro <mario.rincon.nigro@gmail.com>
 * César Arismendi <cesararismendi@gmail.com>
 * Milton Mazzarri <milmazz@gmail.com>

Actualmente el proyecto EISULA está siendo reescrito para adaptarse a las
nuevas versiones del *framework* de desarrollo Web [Django][], además, espero
ampliar y mejorar las funcionalidades que se ofrecían en el proyecto original.
Seguramente en esta etapa de *desarrollo* se presenten errores y fallos, es por
ello que le recomiendo reportar los errores que encuentre a través de:

http://github.com/milmazz/eisula/issues

## Modo Desarrollo ##

Si usted desea probar la aplicación en modo desarrollo solo debe tener en
cuenta lo siguiente:

### Dependencias ###

    # aptitude install git-core python-setuptools
    # easy_install pip
    # pip install django
    $ git clone http://github.com/milmazz/eisula.git
    $ cd eisula
    $ python manage.py syncdb
    $ python manage.py runserver

## Modo Producción ##
 
Si usted desea colocar esta aplicación en producción se le recomienda trabajar
con Apache, WSGI, nginx.

### Dependencias ###

La lista de paquetes a instalar en Debian GNU/Linux es la siguiente:

    # aptitude install python-setuptools \
                   libapache2-mod-wsgi \
                   python-psycopg2 \
                   postgresql \
                   python-markdown \
                   git-core
    # easy_install pip
    # pip install django

Para la creación de la base de datos, si desea usar PostgreSQL (recomendado),
debe ejecutar los siguientes pasos:

    # createuser -SDRPE eisula_user
    # createdb --encoding=UNICODE -O eisula_user eisula_db

### Creación del proyecto ###

    # mkdir -p /srv/www
    # cd /srv/www
    # git clone http://github.com/milmazz/eisula.git
    # cd eisula

Seguidamente debe ajustar los parámetros expuestos en el fichero `settings.py`,
puede hacerlo con su editor de preferencia.

    # vim settings.py

Finalmente sincronice el proyecto con la base de datos.

    # python manage.py syncdb

### Ajustes de ficheros estáticos ###

    # cd /srv/www/eisula/media
    # ln -s /usr/lib/python2.5/site-packages/Django-1.2.1-py2.5.egg/django/contrib/admin/media admin

**NOTA:** Asegúrese que el enlace simbólico realmente existe.

### Configuración de Apache ###

    <VirtualHost *:80>
    ServerAdmin webmaster@example.com
    ServerName example.com
    ErrorLog /var/log/apache2/error.log
    LogLevel warn
    CustomLog /var/log/apache2/access.log combined
    ServerSignature Off

    WSGIScriptAlias / /srv/www/eisula/django.wsgi


        Alias /media "/srv/www/eisula/media"
        <Location "/media">
            SetHandler None
        </Location>

        <LocationMatch "(?i)\.(jpg|png|gif|ico|txt|pdf|css|jpeg)$">
            SetHandler None
        </LocationMatch>
    </VirtualHost>

Finalmente reinicie el Servidor Web Apache:

    # /etc/init.d/apache2 restart

[Django]: http://djangoproject.com
[Universidad de Los Andes]: http://ula.ve
