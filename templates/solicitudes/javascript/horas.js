<script type = "text/javascript">

/*Seleccion de horas de colision*/

max = 4;
S = String;

document.write("<select name = 'horas'>");
for(i = 1 ; i <= max ; i++) {
	document.write("<option value='" + S(i) + "'>" + S(i) + "</option>");
}
document.write("</select>");

</script>