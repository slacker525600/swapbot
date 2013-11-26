
	$(document).ready(function() {		
		$.getJSON( "items.json", function( data ) {
			console.log(data);
			console.log('=====================');
			  var items = [];
			  $.each( data, function( key, val ) {
			    items.push(key + "-" + val);			    
			  });
			  $( "body" ).data( "items", items );
		});
		
		for (var it in $( "body" ).data( "items")) {
			for(var i = 0; i < 4; i++)
			{
				var h = '<ul>';
				var x = 0;
				while (x < 7)
				{
					x++;
					h += '<li class="thumb"><img src="icon1.png" alt=""><span class="text">Jacket</span></a></li>';
				}
				h += '</ul>';
				$("#grid_selector").append(h);
			}
		}
		
		$("#grid_selector  li").each(function(index) {			
			$( this ).click(function() {
				console.log( index + ": " + $( this ).text() );				
				$('#details > ul').append('<li class="item">Item ' + index +'<img src="icon1.png"></li>').hide().show('slow');
			});
		});
	});

