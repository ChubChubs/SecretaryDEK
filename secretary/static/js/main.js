/**
 * Created by gregory on 5/15/16.
 */

String.prototype.format = String.prototype.f = function(){
	var args = arguments;
	return this.replace(/\{(\d+)\}/g, function(m,n){
		return args[n] ? args[n] : m;
	});
};

function initDateFields() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD',
        locale: 'uk'
    });
}

function setClass(){
    var d = document.getElementsByClassName('select');
    for( var i in d){
        //console.log(d[i].id)
        if(d[i].id != null)
        {
            console.log(d[i].id);
            $("#{0}".format(d[i].id)).addClass("selectpicker")
        }
    }
    $("#{0}".format(document.getElementsByClassName('nullbooleanselect')[0].id)).addClass("selectpicker")
}

$(document).ready(function () {
    initDateFields();
    // Twitter select
    setClass();
    $("#id_reviewer").addClass("selectpicker")
});
