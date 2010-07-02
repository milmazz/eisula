<script type = "text/javascript">

S = String;

document.write("<select name = 'porcentaje'");
for(i = 1 ; i <= 9 ; i++) {
	document.write("<option value = '" + S(i * 10) + "'> " + S(i * 10) + "</option>");
}
document.write("</select> %");

</script>