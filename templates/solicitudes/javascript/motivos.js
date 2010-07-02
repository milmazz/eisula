<script type="text/javascript">
var nmot = 1;

function obtenMotivo (i) {
	if(i == 1){ return document.forms[0].motivo1.value; }
	if(i == 2){ return document.forms[0].motivo2.value; }
	if(i == 3){ return document.forms[0].motivo3.value; }
	if(i == 4){ return document.forms[0].motivo4.value; }
	if(i == 5){ return document.forms[0].motivo5.value; }
}

function nuevoMotivo (add) {
	var x = document.getElementById("motivos");
	var r = "<table align = 'center'>";	

	if (nmot == 5 && add != '0') return;

	if (add == '1') { nmot++; }

	if(add == '0'){ nmot--; }

	for (i=1 ; i <= nmot ; i++) {
		var name = "motivo" + String(i);

		var v = "";

		if(i < nmot || add == '0') { v = obtenMotivo(i); }	

		r += "<tr><td>" + String(i) + ".";
		r += "<input type = 'text' name = '" + name + "' ";
		r += "value = '" + v + "' size = '80'/></td>";
 		
	}

	r += "<tr><td colspan = '2' align = 'center'>";
	
	if (i - 1== nmot && nmot > 1) {
		r += "<input type = 'button' value = 'Remover &uacute;ltimo ";
		r += "motivo' onClick = \"nuevoMotivo('0')\"/>";
	}

	r += "<input type = 'button' value = 'A&ntilde;adir otro ";
		r += "motivo' onClick = \"nuevoMotivo('1')\">";

	r += "</td></tr>";
	r += "</table>";

	x.innerHTML = r;
}
</script>
