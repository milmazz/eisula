<script type="text/javascript">

var nmat = 1;
var j = 0;

var materias = new Array();

{% for m in materias %} materias[j++] = "{{ m.nombre }}";
{% endfor %}

function obtenMateria (i) {
	if(i == 1){ return document.forms[0].materia1.value; }
	if(i == 2){ return document.forms[0].materia2.value; }
	if(i == 3){ return document.forms[0].materia3.value; }
	if(i == 4){ return document.forms[0].materia4.value; }
	if(i == 5){ return document.forms[0].materia5.value; }
	if(i == 6){ return document.forms[0].materia6.value; }
	if(i == 7){ return document.forms[0].materia7.value; }
	if(i == 8){ return document.forms[0].materia8.value; }
}

function nuevaMateria (add) {
	var x = document.getElementById("materias");
	var r = "<table align = 'center'>";	

	if (nmat == 8 && add != '0') return;

	if (add == '1') { nmat++; }

	if(add == '0'){ nmat--; }

	for (i=1 ; i <= nmat ; i++) {
		var name = "materia" + String(i);

		var v = "";

		if(i < nmat || add == '0') { v = obtenMateria(i); }

		r += "<tr><td>" + String(i) + ".";
		r += "<select name = '" + name + "'/>";
		for(k = 0 ; k < materias.length ; k++){
			r += "<option value='" + materias[k] + "'";
			if(materias[k] == v){ r += " selected = 'selected' " ;}
			r += "> " + materias[k] + " </option>";
		}
		r += "</select>";
		r += "</td>";

		if (i == nmat && nmat > 1) {
			r += "<td><input type = 'button' value = 'Remover &uacute;ltima ";
			r += "materia' onClick = \"nuevaMateria('0')\"/></td>";
		}

		r += "</tr>";
	}

	r += "<tr><td colspan = '2' align = 'center'>";

	r += "<input type = 'button' value = 'A&ntilde;adir otra ";
	r += "materia' onClick = \"nuevaMateria('1')\">";

	r += "</td></tr>";
	r += "</table>";

	x.innerHTML = r;
}
</script>