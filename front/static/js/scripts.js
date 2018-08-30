
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

        ws = new WebSocket("ws://"+host+":"+port+"/remote-control/"+makeid());

        $('.ws_trigger').click(function(){

			var data = {'f' : $(this).attr('family'), 'a' : $(this).attr('action')}
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

    var key = '';
    var code;
    $('#entry').keyup(function keyUpdHandler(e){
//        code = code = e.keyCode || e.which;
//        alert(code);
    }).keydown(function( e ) {

      if ( e.which == 13 ) {
        key = 'enterKey';
//        this.val('');
        e.preventDefault();
      }else if ( e.which == 8 ){
        key = 'backSpace';
        e.preventDefault();
      }else if (e.which == 32 ){
       key = 'spaceKey';
       e.preventDefault();
      }else{
        var aux = $('#entry');
        var len = aux.val().length;
        key= aux.val().substring(len-1,len);
        console.log('pressed '+event.which);
      }

      var data = {'f' : 'k', 'a' : 'kp', 'value': key}
      if(key != ''){
        ws.send(JSON.stringify(data));
      }

    });

      var options = {};



});



function GetTrueKeyCode(e) {
        var evtobj = window.event ? event : e;
        var unicode = evtobj.charCode ? e.charCode : evtobj.keyCode;
        alert(unicode);
        alert(e.which);
}



