$(document).ready(function()
	{
		$('.form-control').keydown(function(event)
		{
				if (event.which == 13)
				{
					getSuggestions();
				}
		});
		$('#submit').click(getSuggestions);
	});
	
function render_list(list)
{
   	var listLength = list.length;
   	var prettyStr = "";
   	alert("render_list here!");
   	if (listLength>0)
   	{
   	    alert("inside if now");
   		for (var i = 0; i<listLength; i++)
   		{
   	 		prettyStr += "<span onclick=\"getToChatroom('"+list[i][2]+"',\'"+list[i][0]+"\');\"> ";
   			prettyStr += list[i][0];
   			prettyStr += " - ";
   			prettyStr += parseFloat(list[i][1]).toFixed(2);
   			prettyStr += "</span>";
   			prettyStr += "\n";
        }
        alert("prettystring: \n" + prettyStr);
   	}
   	return prettyStr;
}

function getToChatroom(uid,title)
{
	$.getJSON(
		window.script_root + '/_add_user_to_chatroom',
		{
		 username: $('#username').val(),
		 uid: uid,
		 user_ip: myip
		},
		function(data){window.location.href = data.result;}
	);
};
  
function getSuggestions() 
{
  $.getJSON(window.script_root + '/_get_suggestions_',
  {
	input_text: $('#concept_text').val()
  }, 
  function(data) 
  {
	  $('#topicList').html(render_list(data.result));
  });
}
