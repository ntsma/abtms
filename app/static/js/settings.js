var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $("#btnChangePI").click(function(event) {
    var name = $("#name").val();
    var email = $("#email").val();

    $.ajax({
      url: URL + "/abtms/users/",
      type: "POST",
      data: {"email": email, "name": name},
      success: function(data) {
        console.log("Atualização realizada com sucesso.");
        window.location.replace("/abtms/modules/");
      },
      error: function(data) {
        console.log("Houve um problema ao atualizar informações pessoais.");
        window.location.replace("/abtms/settings/");
      }
    });
  });

  $("#btnChangePassword").click(function(event) {
    var password = $("#password").val();
    var email = $("#email").val();

    $.ajax({
      url: URL + "/abtms/password/",
      type: "POST",
      data: {"email": email, "password": password},
      success: function(data) {
        console.log("Atualização realizada com sucesso.");
        window.location.replace("/abtms/modules/");
      },
      error: function(data) {
        console.log("Houve um problema ao atualizar informações pessoais.");
        window.location.replace("/abtms/settings/");
      }
    });
  });
});
