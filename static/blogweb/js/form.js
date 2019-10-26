jQuery(document).ready(function(){

	jQuery(document).on("submit",'form',function(){
		var data = jQuery(this).serialize();
		jQuery("button").hide();
		jQuery.ajax({
           url:jQuery(this).data('action'),
           type:'POST',
           data:data,
           dataType:'json',
           success:function(data){
           	jQuery("button").show();
           	alert(data.status)
           	jQuery("input,textarea").val("");
           	window.location='';
           },
           error:function(data){
           	alert(data)
           }
		});
	});

});