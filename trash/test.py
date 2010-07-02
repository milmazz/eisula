from materias import *
from postgrado import *
from prelacion import *

Lengua = subject()
Lengua.set_name("Lengua")
Lengua.set_tced("V16306912")
Lengua.display()

pgcomp = postgrado()
pgcomp.dpto = 12
pgcomp.display()

prel = prelacion()
prel.set_prelador(10)
prel.set_prelada(11)
prel.display()