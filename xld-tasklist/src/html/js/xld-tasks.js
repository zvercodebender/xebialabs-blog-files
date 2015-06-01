//$.getScript("js/authentication.js");

var myUsername="";
var myPassword="";

function getFormData(dom_query) {
    var out = {};
    var s_data = $(dom_query).serializeArray();
    //transform into simple data/value object
    for(var i = 0; i<s_data.length; i++) {
        var record = s_data[i];
        out[record.name] = record.value;
    }
    return out;
}

function authenticate() {
    obj = getFormData('#loginForm');
    myUsername = obj.myUsername;
    myPassword = obj.myPassword;
    console.log( "Username: " + myUsername );
    console.log( "Password: " + myPassword );
    isOK = validateUser( myUsername, myPassword );
    if( isOK == 1 ) {
        $.mobile.changePage($("#home"),"slide");
        getAllTasks();
    }
    console.log( "isOK: " + isOK );
}

function validateUser( u, p ) {
  URL="/deployit/security/user/" + u;
  results = 0;
  $.ajax({
        type: "GET",
        url: URL,
        username: u,
        password: p,
        dataType: "xml",
        async: false,
        success: function ( data, status, jqXHR ) {
             results = 1;
        }
  });
  return results; 
}

function getAllTasks() {
  if( validateUser(myUsername, myPassword) == 1 ) {
  URL="/deployit/tasts/v2/current/all";
  $.ajax({
        type: "GET",
        url: "/deployit/tasks/v2/current/all",
        username: username,
        password: password,
        dataType: "json",
        async: false,
        success: function ( data, status, jqXHR ) {
             html="";
             for( i = 0; i < data.length; i++ ) {
                if( data[i].state != "XX EXECUTED" && data[i].state != "XX FAILED" ) {
                   html=html + "<div data-role=\"collapsible\" data-theme=\"a\">";
                   html=html + "<h4>" + data[i].state + " - ";
                   html=html + data[i].description + "</h4>";
                   var steps = data[i].block.steps;
                   for( j=0; j < steps.length; j++ ) {
                      html=html + "<div data-role=\"collapsible\" data-theme=\"b\"><h2>" + steps[j].state;
                      html=html + " - " + steps[j].description + "</h2>";
                      html=html + "<code>" + steps[j].log + "</code>";
                      html=html + "</div>";
                   }
                   html=html + "</div>";
                }
             }
             $("#taskList").html( html ).collapsibleset("refresh");
        }
  });
  } else {
        $.mobile.changePage($("#login"),"slide");
  }
}

