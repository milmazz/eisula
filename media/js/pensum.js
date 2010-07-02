semestres = new Array(
	{% for sem in fetch_sem %}
		"{{sem.sem}}",
	{% endfor %}
		"--Seleccione--");
		
departamentos = new Array(
	{% for dpto in fetch_dpto %}
		"{{dpto.nombre}}",
	{% endfor %}
		"--Seleccione--");
	
function changeSel(){
	var optionArray;
	if(document.forms[0].filter[0].checked)
		optionArray = semestres;
	else if(document.forms[0].filter[1].checked)
		optionArray = departamentos;
	for(var i=0; i<optionArray.length; i++){
		var tochange = document.forms[0].filter_opt;
		tochange.options.length = 0;
		for(var j=0; j<optionArray.length; j++){
			var opt = optionArray[j];
			tochange.options[j] = new Option(opt,opt);
			if(opt=="--Seleccione--")
				tochange.options[j].selected=true
		}
	}
}


function not_selected(){
	if(document.forms[0].filter[2].checked){
		document.forms[0].filter_opt.value="";
		document.forms[0].filtro.value="all";
		return true;
	}
	if(document.forms[0].filter_opt.value=="--Seleccione--"){
		alert("Elija la opcion del filtro");
		return false;
	}
	if(document.forms[0].filter[0].checked)
		document.forms[0].filtro.value="semestre";
	else
		document.forms[0].filtro.value="departamento";
	return true;
}