$('.apireq').click( function(){

  $.ajax({
            url : "http://127.0.0.1:8000/api/persona/",
            datatype: "json",
            success: function(data){
                    $('#id').text( data[0].id);
                    $('#nombre').text( data[0].nombre);
                    $('#rut').text( data[0].rut);
                    $('#mail').text( data[0].mail);
                    $('#passwd').text( data[0].passwd);
                    $('#img_persona').text( data[0].img_persona);
            }   



  });

});
