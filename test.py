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
                    document.getElementById('myDiv').innerHTML = response.username
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
<body align=center>
<h1>MVSRBOT</h1>
<form action="" method="POST">
<input type="text" name="scname" id="scname">
<input type="hidden" name="secret" id="secret" value="shhh">
<input type="button" value="Submit" onclick="return loadXMLDoc()">
</form>
<div id="myDiv"></div>
</body>
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