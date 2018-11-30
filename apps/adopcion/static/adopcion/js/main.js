var btn = document.getElementById("btn")
var container = document.getElementById("content_ex")
var url = 'http://127.0.0.1:8000/api/persona/'

$.ajax({
  method: 'GET',
  url: url,
  success: function(data){
      console.log(data)
      console.log("success")
  },
  error: function(error_data){
      console.log("error")
  }

})

btn.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open("GET",url);
    ourRequest.onload = function(){
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData);
    }
    ourRequest.send();
})

function renderHTML(data){
    var container = document.getElementById("content_ex")
    var htmlString = "";

    for(i=0; i< data.length; i++){
        htmlString = "<p> su mail es : " + data[i].pk + "</p>";
    }
    container.insertAdjacentHTML('beforeend',htmlString);
}
