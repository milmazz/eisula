<script type = "text/javascript">

/*Seleccion de exceso de unidades credito*/

max = 10;
S = String;

document.write("<select name = 'exceso'>");
for(i = 1 ; i <= max ; i++) {
	document.write("<option value='" + S(i) + "'>" + S(i) + "</option>");
}
document.write("</select>");

</script>