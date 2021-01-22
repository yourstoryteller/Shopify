$(document).ready(function() {

    $("#confirm-checkout").click( function() {
        base_url = window.location.origin
        url = base_url + "/orders"

         setTimeout(function(){
            window.location.replace(url);
         }, 1000);
    });

});