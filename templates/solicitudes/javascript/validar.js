<script type = "text/javascript">
function validar (formulario) {
	if(enBlanco(document.forms[0].nombre.value)) {
		alert("Introduzca su nombre");
		return false;
	}
	if(enBlanco(document.forms[0].cedula.value)) {
		alert("Introduzca su cédula");
		return false;
	}
	if(!cedula(document.forms[0].cedula.value)) {
		alert("Introduzca solo dígitos en el campo CI de estudiante");
		return false;
	}

	if(formulario == "prorroga") {
		if(enBlanco(document.forms[0].tutor.value)) {
			alert("Introduzca el nombre del tutor del proyecto");
			return false;
		}
		if(enBlanco(document.forms[0].titulo.value)) {
			alert("Introduzca el título del proyecto");
			return false;
		}	
	}

	/*Mosca con la variable nmot*/

	for(var i = 1 ; i <= nmot ; i++){
		if(enBlanco(obtenMotivo(i))) {
		        alert("Introduzca el motivo de solicitud " + String(i));
			return false;	
		}
	}

	return true;		
}

function enBlanco (s) {
	var c = 0;

	if(s == "") { return true; }

	for(var i = 0 ; i < s.length ; i++) {
		if(s.charAt(i) == ' ') { c++; }
	}

	if(c == s.length) { return true; }

	return false;
}

function cedula(c) {
	for(var i = 0 ; i < c.length ; i++) {
		if(c.charAt(i) < '0' || c.charAt(i) > '9') {
			return false;
		}
	}

	return true;
}
</script>