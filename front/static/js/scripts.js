
function makeid()
{var text="";var possible="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";for(var i=0;i<15;i++)
text+=possible.charAt(Math.floor(Math.random()*possible.length));return text;}

$(document).ready(function(){
$(".alert").addClass("in").fadeOut(4500);

/* swap open/close side menu icons */
$('[data-toggle=collapse]').click(function(){
  	// toggle icon
  	$(this).find("i").toggleClass("glyphicon-chevron-right glyphicon-chevron-down");
});

        //Esto se podria hacer con un call generico, poner los attr family y action
        //dentro del tag

        ws = new WebSocket("ws://"+host+":"+port+"/ws/"+makeid());

        $('.ws_trigger').click(function(){

			var data = {'family' : $(this).attr('family'), 'action' : $(this).attr('action')}
			ws.send(JSON.stringify(data));
        });

/*		$('#subirVolumen').click(function(){
			//alert('sube');
			var data = {'family' : 'audio', 'action' : 'volumeUp'}
			ws.send(JSON.stringify(data));

		});

		$('#bajarVolumen').click(function(){
			//alert('baja');
			var data = {'family' : 'audio', 'action' : 'volumeDown'}
			ws.send(JSON.stringify(data));
		});

        $('#brightnessUp').click(function(){
			//alert('sube');
			var data = {'family' : 'video', 'action' : 'brightnessUp'}
			ws.send(JSON.stringify(data));

		});

		$('#brightnessDown').click(function(){
			//alert('baja');
			var data = {'family' : 'video', 'action' : 'brightnessDown'}
			ws.send(JSON.stringify(data));
		});

		$('#changeWindow').click(function(){
			//alert('baja');
			var data = {'family' : 'keyboard', 'action' : 'changeWindow'}
			ws.send(JSON.stringify(data));
		});

        $('#changeFocus').click(function(){
			//alert('baja');
			var data = {'family' : 'keyboard', 'action' : 'changeFocus'}
			ws.send(JSON.stringify(data));
		});

*/
    var key = ''
    $('#entry').keyup(function keyUpdHandler(event){

    }).keydown(function( event ) {

    alert(event.which);
      if ( event.which == 13 ) {
        key = 'enterKey';
        event.preventDefault();
      }else if ( event.which == 8 ){
        key = 'backSpace';
      }else if (event.which == 32 ){
       key = 'spaceKey';
      }else{
        var aux = $('#entry');
        var len = aux.val().length;
        key= aux.val().substring(len-1,len);
        console.log('pressed '+event.which);
      }

      var data = {'family' : 'key_pressed', 'action' : key}
      if(key != ''){
        ws.send(JSON.stringify(data));
      }

    });

      var options = {};



});



