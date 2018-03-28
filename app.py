from flask import (Flask, request, jsonify)
import aiml                
app = Flask(__name__)
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

html_page = """<!DOCTYPE HTML>
<html>
<head>
<title>MVSRBOT</title>
<script>
function reset()
{
sessionStorage.setItem("loca",1);
}
    function loadXMLDoc()
    {
 	var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {          
                    var response = JSON.parse(req.responseText)
		    var data=document.getElementById('scname').value;
                    var output = response.username
		    document.getElementById('scname').value="";
		    var stor=sessionStorage.getItem("loca");
                    if(stor==1)
			{
			sessionStorage.setItem("loca",3);
			document.getElementById('one').innerHTML=data;
			document.getElementById('two').innerHTML=output;
			document.getElementById('three').innerHTML="";
			document.getElementById('four').innerHTML="";
			document.getElementById('five').innerHTML="";
			document.getElementById('six').innerHTML="";
			document.getElementById('seven').innerHTML="";
			document.getElementById('eight').innerHTML="";
			document.getElementById('nine').innerHTML="";
			document.getElementById('ten').innerHTML="";
			document.getElementById('eleven').innerHTML="";
			document.getElementById('tweleve').innerHTML="";
			document.getElementById('thirteen').innerHTML="";
			document.getElementById('fourteen').innerHTML="";
			document.getElementById('fifteen').innerHTML="";
			document.getElementById('sixteen').innerHTML="";
			document.getElementById('seventeen').innerHTML="";
			document.getElementById('eighteen').innerHTML="";
			document.getElementById('ninteen').innerHTML="";
			document.getElementById('twenty').innerHTML="";
			document.getElementById('twentyone').innerHTML="";
			document.getElementById('twentytwo').innerHTML="";
			document.getElementById('twentythree').innerHTML="";
			document.getElementById('twentyfour').innerHTML="";
			document.getElementById('twentyfive').innerHTML="";
			document.getElementById('twentysix').innerHTML="";
			document.getElementById('twentyseven').innerHTML="";
			document.getElementById('twentyeight').innerHTML="";
			document.getElementById('twentynine').innerHTML="";
			document.getElementById('thirty').innerHTML="";
			}	
		else if(stor==3)
			{
			sessionStorage.setItem("loca",5);
document.getElementById('three').innerHTML=data;
document.getElementById('four').innerHTML=output;
}
else if(stor==5)
{
sessionStorage.setItem("loca",7);
document.getElementById('five').innerHTML=data;
document.getElementById('six').innerHTML=output;
}
else if(stor==7)
{
sessionStorage.setItem("loca",9);
document.getElementById('seven').innerHTML=data;
document.getElementById('eight').innerHTML=output;
}
else if(stor==9)
{
sessionStorage.setItem("loca",11);
document.getElementById('nine').innerHTML=data;
document.getElementById('ten').innerHTML=output;
}
else if(stor==11)
{
sessionStorage.setItem("loca",13);
document.getElementById('eleven').innerHTML=data;
document.getElementById('tweleve').innerHTML=output;
}

else if(stor==13)
{
sessionStorage.setItem("loca",15);
document.getElementById('thirteen').innerHTML=data;
document.getElementById('fourteen').innerHTML=output;
}

else if(stor==15)
{
sessionStorage.setItem("loca",17);
document.getElementById('fifteen').innerHTML=data;
document.getElementById('sixteen').innerHTML=output;
}

else if(stor==17)
{
sessionStorage.setItem("loca",19);
document.getElementById('seventeen').innerHTML=data;
document.getElementById('eighteen').innerHTML=output;
}

else if(stor==19)
{
sessionStorage.setItem("loca",21);
document.getElementById('ninteen').innerHTML=data;
document.getElementById('twenty').innerHTML=output;
}

else if(stor==21)
{
sessionStorage.setItem("loca",23);
document.getElementById('twentyone').innerHTML=data;
document.getElementById('twentytwo').innerHTML=output;
}

else if(stor==23)
{
sessionStorage.setItem("loca",25);
document.getElementById('twentythree').innerHTML=data;
document.getElementById('twentyfour').innerHTML=output;
}

else if(stor==25)
{
sessionStorage.setItem("loca",27);
document.getElementById('twentyfive').innerHTML=data;
document.getElementById('twentysix').innerHTML=output;
}
else if(stor==27)
{
sessionStorage.setItem("loca",29);
document.getElementById('twentyseven').innerHTML=data;
document.getElementById('twentyeight').innerHTML=output;
}

else if(stor==29)
{
sessionStorage.setItem("loca",1);
document.getElementById('twentynine').innerHTML=data;
document.getElementById('thirty').innerHTML=output;
}
var elem = document.getElementById('mainDiv');
 	 elem.scrollTop = elem.scrollHeight;

         }
            }
        }
    
        req.open('POST', '/ajax')
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var un = document.getElementById('scname').value
        var sec = document.getElementById('secret').value
        var postVars = 'username='+un+'&secret='+sec
        req.send(postVars)
        return false
    }
</script>
</head>
<body onload="reset()" align=center>
<div style="padding-left:10px;padding-right:10px;width:500px;height:430px;
overflow:scroll;overflow-x:hidden" id="mainDiv">

<div style="text-align:right" id="one"></div>
<div style="text-align:left" id="two"></div>
<div style="text-align:right" id="three"></div>
<div style="text-align:left" id="four"></div>
<div style="text-align:right" id="five"></div>
<div style="text-align:left" id="six"></div>
<div style="text-align:right" id="seven"></div>
<div style="text-align:left" id="eight"></div>
<div style="text-align:right" id="nine"></div>
<div style="text-align:left" id="ten"></div>

<div style="text-align:right" id="eleven"></div>
<div style="text-align:left" id="tweleve"></div>
<div style="text-align:right" id="thirteen"></div>
<div style="text-align:left" id="fourteen"></div>
<div style="text-align:right" id="fifteen"></div>
<div style="text-align:left" id="sixteen"></div>
<div style="text-align:right" id="seventeen"></div>
<div style="text-align:left" id="eighteen"></div>
<div style="text-align:right" id="ninteen"></div>
<div style="text-align:left" id="twenty"></div>

<div style="text-align:right" id="twentyone"></div>
<div style="text-align:left" id="twentytwo"></div>
<div style="text-align:right" id="twentythree"></div>
<div style="text-align:left" id="twentyfour"></div>
<div style="text-align:right" id="twentyfive"></div>
<div style="text-align:left" id="twentysix"></div>
<div style="text-align:right" id="twentyseven"></div>
<div style="text-align:left" id="twentyeight"></div>
<div style="text-align:right" id="twentynine"></div>
<div style="text-align:left" id="thirty"></div>
</div> 
</body>
<form method="POST" onsubmit="return loadXMLDoc()">
<input type="text" name="scname" id="scname" 
style="width:200px;font-size:16px;height:30px;
padding-left:8px" autofocus required>
<input type="hidden" name="secret" id="secret" value="shhh">
<input type="submit" value=">" style="font-size:18px;width:50px;height:30px" onclick="return loadXMLDoc()"/>
</form>
</html>"""

@app.route('/')
def index():
    return html_page
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    user = request.form['username']
    username=kernel.respond(user)

    return jsonify(username=username)
    
    
if __name__ == "__main__":
    app.run(debug = True)