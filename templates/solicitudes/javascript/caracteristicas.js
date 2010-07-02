<script type="text/javascript">
var nmot = 1;

function obtenCaracteristica (i) {
	if(i == 1){ return document.forms[0].carac1.value; }
	if(i == 2){ return document.forms[0].carac2.value; }
	if(i == 3){ return document.forms[0].carac3.value; }
	if(i == 4){ return document.forms[0].carac4.value; }
	if(i == 5){ return document.forms[0].carac5.value; }
}

function nuevaCaracteristica (add) {
	var x = document.getElementById("caracteristicas");
	var r = "<table align = 'center'>";	

	if (nmot == 5 && add != '0') return;

	if (add == '1') { nmot++; }

	if(add == '0'){ nmot--; }

	for (i=1 ; i <= nmot ; i++) {
		var name = "carac" + String(i);

		var v = "";

		if(i < nmot || add == '0') { v = obtenCaracteristica(i); }

		r += "<tr><td>" + String(i) + ".";
		r += "<input type = 'text' name = '" + name + "' ";
		r += "value = '" + v + "' size = '80'/></td>";
 		
		if (i == nmot && nmot > 1) {
			r += "<td><input type = 'button' value = 'Remover ";
			r += "caracter&iacute;stica' onClick = \"nuevaCaracteristica('0')\"/></td>";
		}
		r += "</tr>";
	}

	r += "<tr><td colspan = '2' align = 'center'>";

	r += "<input type = 'button' value = 'A&ntilde;adir ";
		r += "caracter&iacute;stica' onClick = \"nuevaCaracteristica('1')\">";

	r += "</td></tr>";
	r += "</table>";

	x.innerHTML = r;
}
</script>