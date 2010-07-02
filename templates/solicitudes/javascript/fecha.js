<script type = "text/javascript">

/*Seleccion de horas de colision*/

meses = new Array("Enero", "Febrero", "Marzo", "Abril",
	"Mayo", "Junio", "Julio", "Agosto", "Septiembre",
	"Octubre", "Noviembre", "Diciembre");

d = new Date();
S = String

document.write("<select name = 'dia'>");
for(i = 1 ; i <= 31 ; i++) {
	document.write("<option value='" + S(i) + "'>" + S(i) + "</option>");
}
document.write("</select>");

document.write("<select name = 'mes'>");
for(i = 0 ; i < meses.length ; i++) {
	document.write("<option value='" + meses[i] + "'>" + meses[i] + "</option>");
}
document.write("</select>");

document.write("<select name = 'year'>");

for(i = parseInt(d.getFullYear()) ; i >= parseInt(d.getFullYear()) - 1 ; i--) {
	document.write("<option value='" + S(i) + "'>" + S(i) + "</option>");
}
document.write("</select>");
</script>