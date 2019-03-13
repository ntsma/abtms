var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

function fillModalPF(cpf) {
  $(document).ready(function(event){
    $.ajax({
      url: URL + "/api/abtms/users/" + cpf + "/",
      type: "GET",
      success: function(member) {
        console.log(member);
        $("#name").val(member.name);
        $("#cpf").val(member.cpf);
        $("#type").val(member.type);
        $("#phone").val(member.phone);
        $("#situation").val(member.situation);
      }
    });
  });

}


function fillModalPJ(cnpj) {
  $(document).ready(function(event){
    $.ajax({
      url: URL + "/api/abtms/bussinesses/" + cnpj + "/",
      type: "GET",
      success: function(member) {
        console.log(member);
        $("#namepj").val(member.name);
        $("#cnpj").val(member.cnpj);
        $("#typepj").val(member.type);
        $("#phonepj").val(member.phone);
        $("#situationpj").val(member.situation);
      }
    });
  });

}
