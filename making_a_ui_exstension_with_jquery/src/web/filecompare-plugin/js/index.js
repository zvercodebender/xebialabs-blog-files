
var auth = "";
//*************************************************************
//*  Toggle Input Forms
function toggleForms( divName ) {
    $('#results').hide();
    if( divName == 'diff2repo' ) {
       $('#diff2repo').show();
       $('#diff2hosts').hide();
       getDeployedApplicationList();
    } else {
       $('#diff2repo').hide();
       $('#diff2hosts').show();
    }
}

//*************************************************************
//*  Init Input Forms
function initForms() {
   $('#diff2repo').hide();
   $('#diff2hosts').hide();
   $('#results').hide();
   toggleForms( 'diff2repo' );
   getDeployedApplicationList();
}

//*************************************************************
//*  Compare file on servers to repo
function compare2repo() {
   deployed = $( "#deployed" ).val();
   alert( "deployed ID = " + deployed );
   var REQUEST="/api/extension/filecompare/compare/to/repo";
   //REQUEST="/api/extension/test/cis";
   $.ajax({
      url: REQUEST,
      type: "GET",
      dataType: "text",
      async: false,
      data: { root: "Environments" },
      beforeSend: function(req) {
         req.setRequestHeader('Authorization', auth );
      },
      success: function( response, status, xmlData ) {
         xml = response;
         alert( xml );
      },
      error: function( xhr, textStatus, errorThrown ) {
           console.log("xhr = " + xhr + "\ntextStatus = " + textStatus + "\nerrorThrown = " + errorThrown );
       }
   });
   $('#results').html( "" );
}
//*************************************************************
//   Get DeployedApplication List
function getDeployedApplicationList() {
    console.log('getDeployedApplicationList-> START');
    var response;
    var REQUEST="/deployit/repository/query?type=udm.DeployedApplication";
    $.ajax({
       url: REQUEST,
       type: "GET",
       dataType: "text",
       async: false,
       success: function( response, status, xmlData ) {
           xml = response;
           var response="<select id='deployed' name='deployed' onChange='compare2repo();'>";
           response = response + "<option selected value='none'>NONE</option>";
           $(xml).find('ci').each( function() {
                var obj = $(this).attr('ref');
                response = response + "<option value='" + obj + "'>" + obj + "</option>";
           });
           response = response + "</select>";
           $('#results').html( response );
           $('#results').show();
       },
       error: function( xhr, textStatus, errorThrown ) {
           console.log("xhr = " + xhr + "\ntextStatus = " + textStatus + "\nerrorThrown = " + errorThrown );
       }
    }); 
    console.log('getDeployedApplicationList-> DONE');
}

//*************************************************************
//*   INIT Function
$(document).ready( function() {
   auth = window.self.content.getAuthToken();
   initForms();
   console.log('Init JQuery');
});

