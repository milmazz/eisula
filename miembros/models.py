# vim: ts=4:sts=4:sw=4:ai:et:tw=78:nowrap
# -*- coding: latin-1 -*-
from django.db import models
from django.contrib.auth.models import User 

SEXO = (('M', 'Masculino'),
        ('F', 'Femenino'))

TIPO = (('MTS', 'MTS'),
        ('ATS', 'ATS'))

NACIONALIDAD = (
       ('bri', 'britanico'),
       ('ing', 'ingles'),
       ('gal', 'gales'),
       ('irl', 'irlandes'),
       ('irl', 'irlandes'),
       ('esc', 'escoces'),
       ('dan', 'danes'),
       ('fin', 'finlandes'),
       ('sue', 'sueco'),
       ('nor', 'noruego'),
       ('bel', 'belga'),
       ('fra', 'frances'),
       ('ale', 'aleman'),
       ('hol', 'holandes'),
       ('hu', 'hungaro'),
       ('ita', 'italiano'),
       ('lux', 'luxemburgues'),
       ('por', 'portugues'),
       ('esp', 'español'),
       ('sui', 'suizo'),
       ('aus', 'austriaco'),
       ('bos', 'bosnio'),
       ('ser', 'serbio/a'),
       ('bu', 'bulgaro'),
       ('cro', 'croata'),
       ('pol', 'polaco'),
       ('esl', 'eslovaco'),
       ('esl', 'esloveno'),
       ('gri', 'griego'),
       ('rus', 'ruso'),
       ('che', 'checo'),
       ('rum', 'rumano/ana'),
       ('tur', 'turco'),
       ('arg', 'argentino'),
       ('bol', 'boliviano'),
       ('bra', 'brasileño'),
       ('chi', 'chileno'),
       ('col', 'colombiano'),
       ('cos', 'costarricense'),
       ('cub', 'cubano'),
       ('ecu', 'ecuatoriano'),
       ('sal', 'salvadoreño'),
       ('gua', 'guatemalteco'),
       ('hai', 'haitiano'),
       ('hon', 'hondureño'),
       ('mex', 'mexicano'),
       ('nic', 'nicaragüense'),
       ('pan', 'panameño'),
       ('par', 'paraguayo'),
       ('per', 'peruano'),
       ('dom', 'dominicano'),
       ('uru', 'uruguayo'),
       ('ven', 'venezolano'),
       ('est', 'estadounidense'),
       ('can', 'canadiense'),
       ('ind', 'indio'),
       ('mal', 'malayo'),
       ('ind', 'indonesio'),
       ('chi', 'chino'),
       ('jap', 'japones'),
       ('tai', 'taiwanes/esa'),
       ('vie', 'vietnamita'),
       ('tai', 'tailandes'),
       ('sin', 'singapurense'),
       ('cor', 'coreano'),
       ('cam', 'camboyano'),
       ('aus', 'australiano'),
       ('neo', 'neozelandes'),
       ('nep', 'nepali'),
       ('fil', 'filipino'),)


class Miembro(models.Model):
    user = models.ForeignKey(User, unique=True, core=True)
    cedula = models.CharField(maxlength=10, unique=True, 
                              help_text='Ej. V012345678', db_index=True, 
                              verbose_name='cedula', blank=False)
    sexo = models.CharField(maxlength=1, choices=SEXO, blank=False)
    telef = models.PhoneNumberField(verbose_name='numero telefonico', 
                                     blank=False, help_text='Ej. 274-555-5555')
    direccion = models.CharField(verbose_name='direccion', maxlength=128, 
                                 blank=False)
    web = models.URLField(blank=True)
    tipo = models.CharField(maxlength=3, choices=TIPO, blank=False)
    
    # TODO horario?

    def __str__(self):
        return self.user.username

    class Admin:
        search_fields = ('user', 'cedula' )


class CV(models.Model):
    pertenece = models.ForeignKey(Miembro, db_index=True,
                                  edit_inline=models.TABULAR,
                                  core=True, unique=True, num_in_admin=1)
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento', 
                                        blank=True, null=True)
    nacionalidad = models.CharField(maxlength=3, blank=False, core=True,
                                    choices=NACIONALIDAD)
    categoria = models.CharField(maxlength=16, blank=True)
    resumen = models.TextField(verbose_name='resumen curricular', blank=True)
    

    def __str__(self):
        return str(self.pertenece)

    class Meta:
        verbose_name_plural = 'Curriculum'
        verbose_name = 'Curriculum'

    # TODO, eliminar el acceso por admin, deberia agregarse desde Miembro
    class Admin:
        pass

class Titulo(models.Model):
    pertenece = models.ForeignKey(Miembro, core=True, 
                                  edit_inline=models.TABULAR, 
                                  num_in_admin=3, db_index=True)
    grado = models.CharField(maxlength=32, blank=False, core=True) 
    donde = models.CharField(maxlength=128, blank=False, core=True)
    mencion = models.CharField(maxlength=128, verbose_name='mencion',
                               blank=True, core=True)

    def __str__(self):
        return self.grado

    # TODO, eliminar el acceso por admin, deberia agregarse desde Miembro
    class Admin:
        pass


class Publicacion(models.Model):
    autores = models.ManyToManyField(CV, filter_interface=models.HORIZONTAL)
    # TODO los articulos pueden tener autores que no pertenezcan a la escuela?
    nombre = models.CharField(maxlength=256, 
                              verbose_name='titulo de la publicacion',
                              blank=False)
    agno = models.CharField(maxlength=4, verbose_name='Año de publicacion', 
                            blank=False)
    lugar = models.CharField(maxlength=256, blank=False)
    resumen = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'publicaciones'

    class Admin:
        pass


class GrupoInvestigacion(models.Model):
    nombre = models.CharField(maxlength=128, unique=True, blank=False)
    codigo = models.CharField(maxlength=16, verbose_name='codigo', blank=False)
    descripcion = models.TextField(verbose_name='descipcion', blank=False)
    miembros = models.ManyToManyField(Miembro, related_name='miembrosg', 
                                      blank=False,
                                      filter_interface=models.HORIZONTAL)
    responsable = models.ForeignKey(Miembro, blank=False, unique=True)
    pcontacto = models.ForeignKey(Miembro, verbose_name='persona de contacto', 
                                  related_name='pcontactoa', unique=True)
    telef = models.PhoneNumberField(verbose_name='numero telefonico', 
                                     blank=False, help_text='Ej. 274-555-5555')
    direccion = models.CharField(verbose_name='direccion', maxlength=128, 
                                 blank=False)
    web = models.URLField(blank=True)
    departamento = models.ForeignKey('Departamento', blank=False)

    def __str__(self):
        return self.nombre

    class Admin:
        fields = ((None, {'fields': ('nombre', 'codigo', 'departamento',
                                     'responsable', 'pcontacto', 'telef', 
                                     'direccion','web', 'miembros', 
                                     'descripcion' )}),)
        list_display = ('codigo', 'nombre', 'responsable', 'pcontacto', 'telef')
        search_fields = ('nombre', 'codigo', 'responsable')
        list_filter = ('departamento',)
    class Meta:
        verbose_name_plural = "Grupos de Investigacion"


class Departamento(models.Model):
    nombre = models.CharField(maxlength=32, unique=True, blank=False)
    descripcion = models.TextField(verbose_name='descripcion', blank=False)
    jefe = models.ForeignKey(Miembro, verbose_name='jefe de departamento',
                                blank=False, unique=True)
    miembros = models.ManyToManyField(Miembro, blank=False,
                                      related_name='miembros',
                                      filter_interface=models.HORIZONTAL)
    telef = models.PhoneNumberField(verbose_name='numero telefonico', 
                                     blank=False, help_text='Ej. 274-555-5555')
    direccion = models.CharField(verbose_name='direccion', maxlength=128, 
                                 blank=False)
    web = models.URLField(blank=True, verify_exists=False)

    def __str__(self):
        return self.nombre

    class Admin:
        fields = ((None, {'fields': ('nombre', 'jefe', 'telef', 'direccion',
                                     'web', 'miembros', 'descripcion' )}),)
        list_display = ('nombre', 'jefe', 'telef')
       
