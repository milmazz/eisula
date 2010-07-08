# vim: ts=4:sts=4:sw=4:ai:et:tw=78:nowrap
# -*- coding: utf-8 -*-
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
    user = models.ForeignKey(User, unique=True)
    cedula = models.CharField(max_length=10, unique=True, 
                              help_text='Ej. V012345678', db_index=True, 
                              verbose_name='cedula', blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False)
    # TODO: Port PhoneNumberField to Django > 1.0
    #telef = models.PhoneNumberField(verbose_name='numero telefonico', 
    #                                 blank=False, help_text='Ej. 274-555-5555')
    direccion = models.CharField(verbose_name='direccion', max_length=128, 
                                 blank=False)
    web = models.URLField(blank=True)
    tipo = models.CharField(max_length=3, choices=TIPO, blank=False)
    
    # TODO horario?

    def __unicode__(self):
        return self.user.username


class CV(models.Model):
    pertenece = models.ForeignKey(Miembro, db_index=True,
                                  unique=True)
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento', 
                                        blank=True, null=True)
    nacionalidad = models.CharField(max_length=3, blank=False,
                                    choices=NACIONALIDAD)
    categoria = models.CharField(max_length=16, blank=True)
    resumen = models.TextField(verbose_name='resumen curricular', blank=True)
    
    def __unicode__(self):
        return self.pertenece #str(self.pertenece)

    class Meta:
        verbose_name_plural = 'Curriculum'
        verbose_name = 'Curriculum'


class Titulo(models.Model):
    pertenece = models.ForeignKey(Miembro, db_index=True)
    grado = models.CharField(max_length=32, blank=False) 
    donde = models.CharField(max_length=128, blank=False)
    mencion = models.CharField(max_length=128, verbose_name='mencion',
                               blank=True)

    def __unicode__(self):
        return self.grado


class Publicacion(models.Model):
    autores = models.ManyToManyField(CV)
    # TODO los articulos pueden tener autores que no pertenezcan a la escuela?
    nombre = models.CharField(max_length=256, 
                              verbose_name='titulo de la publicacion',
                              blank=False)
    agno = models.CharField(max_length=4, verbose_name='Año de publicacion', 
                            blank=False)
    lugar = models.CharField(max_length=256, blank=False)
    resumen = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'publicaciones'


class GrupoInvestigacion(models.Model):
    nombre = models.CharField(max_length=128, unique=True, blank=False)
    codigo = models.CharField(max_length=16, verbose_name='codigo', blank=False)
    descripcion = models.TextField(verbose_name='descripcion', blank=False)
    miembros = models.ManyToManyField(Miembro, related_name='miembrosg', 
                                      blank=False)
    responsable = models.ForeignKey(Miembro, blank=False, unique=True)
    pcontacto = models.ForeignKey(Miembro, verbose_name='persona de contacto', 
                                  related_name='pcontactoa', unique=True)
    # TODO: Port PhoneNumberField to Django > 1.0
    #telef = models.PhoneNumberField(verbose_name='numero telefonico', 
    #                                 blank=False, help_text='Ej. 274-555-5555')
    direccion = models.CharField(verbose_name='direccion', max_length=128, 
                                 blank=False)
    web = models.URLField(blank=True)
    departamento = models.ForeignKey('Departamento', blank=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Grupos de Investigacion"


class Departamento(models.Model):
    nombre = models.CharField(max_length=32, unique=True, blank=False)
    descripcion = models.TextField(verbose_name='descripcion', blank=False)
    jefe = models.ForeignKey(Miembro, verbose_name='jefe de departamento',
                                blank=False, unique=True)
    miembros = models.ManyToManyField(Miembro, blank=False,
                                      related_name='miembros')
    # TODO: Port PhoneNumberField to Django > 1.0
    #telef = models.PhoneNumberField(verbose_name='numero telefonico', 
    #                                 blank=False, help_text='Ej. 274-555-5555')
    direccion = models.CharField(verbose_name='direccion', max_length=128, 
                                 blank=False)
    web = models.URLField(blank=True, verify_exists=False)

    def __unicode__(self):
        return self.nombre

