<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<head>
<style type="text/css">
body {
  margin:0;
  padding:0;
}
</style>

<link type="text/css" rel="stylesheet" href="/yui/3.3.0/cssfonts/fonts-min.css">
<script type="text/javascript" src="/yui/3.3.0/yui/yui-min.js"></script>

<style id="yui3-style-overrides">
  #main #example-canvas .yui3-tabview .yui3-tab-selected a {
  color:white;
}
</style>
</head>

<body class="yui3-skin-sam">
<div id="panel">
    <ul>
        <li><a href="#login">Login</a></li>
        <li><a href="#register">Register</a></li>
    </ul>
    <div>
        <div id="login">
            <p>login content</p>
        </div>

        <div id="register">
            <p>register content</p>
        </div>
    </div>
</div>

<div id="loginDialog">
<div class="hd">Login</div>
  <div class="bd">
     <form method="POST" action="/login">
       <div class="smallTitle">Welcome to the Xxxxxx Management System.</div>
       <br/>
          <div class="smallText">
          <table cellpadding="0" cellspacing="0" border="0">
          <tr>
   <td style="width: 80px"><label for="username">Name:</label></td>
   <td><input type="text" name="username" class="textBox" /></td>
          </tr>
          <tr>
   <td><label for="password">Password:</label></td>
   <td><input type="password" name="password" class="textBox" /></td>
          </tr>
          <tr>
   <td colspan="2"><div id="loginError">Invalid login.</div></td>
          </tr>
          </table>
       </div>
    </form>
  </div>
</div>

</body>

<script type="text/javascript">
YUI({ filter: 'raw' }).use("yui", "tabview", function(Y) {
    var tabview = new Y.TabView({srcNode:'#panel'});
    tabview.render();
});

var handleLogin = function() {
   this.submit();
};
            
var handleLoginSuccess = function(o) {
    if (o.responseText == "success") {
       getListings();
    } else {
       Initialize(true);
    }
};

var handleLoginFailure = function(o) {
    alert("Submission failed: " + o.status);
};

// Instantiate the Dialog
var loginDialog = new YAHOO.widget.Dialog("loginDialog", 
{ 
    width : "340px",
    fixedcenter : true,
    visible : false, 
    constraintoviewport : true,
    draggable : true,
    buttons : [ { text:"Login", handler:handleLogin, isDefault:true }]
} );
       
loginDialog.callback = { success: handleLoginSuccess,
                         failure: handleLoginFailure };
			   
// Validate the entries in the form to require that both first and last name are entered
loginDialog.validate = function() {
    var data = this.getData();
    if (data.username == "" || data.password == "") {
	alert("Please enter a username and password.");
	return false;
    } else {
	return true;
    }
};

</script>

