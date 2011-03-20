<%inherit file="base.html"/>

<%def name="body()">
<div class="yui3-g" style="height:40em;">
    <div class="yui3-u-1-5" >
	<div id="side" class="yui3-menu" role="menu">
	    <div class="yui3-menu-content">
		<ul class="first-of-type">
		    <li class="yui3-menuitem"><a class="yui3-menuitem-content">${_("System")}</a></li>
		    <li class="yui3-menuitem"><a class="yui3-menuitem-content">${_("User")}</a></li>
		    <li class="yui3-menuitem"><a class="yui3-menuitem-content">${_("Key")}</a></li>
		</ul>
	   </div>
	</div>
    </div>

    <div class="yui3-u-4-5">
	<div  id="content">
	    <ul>
		<li><a href="#tab_login" class="tablabel"> ${_('Login')} </a></li>
		<li><a href="#tab_register" class="tablabel"> ${_('Register')} </a></li>
	    </ul>

	    <div>
		<div id="tab_login">
		    <form id="loginform" action="main/auth" method="post">
			<div>
			    <label for="username">${_("Username/Email")} : &nbsp;</label>
			    <input id="username" name="username" type="text"/>
			</div>
			<div>
			    <label for="passwd">${_("Password")} : &nbsp;</label>
			    <input id="passwd" name="passwd" type="password"/>
			</div>
			<div class="submit">
			    <label for="submit">&nbsp;</label>
			    <button type="button" id="submit">${_("Submit")}</button>
			</div>
		    </form>
		</div>

		<div id="tab_register">
		    <form id="registerform" action="main/register" method="post">
			<div>
			    <label for="username">${_("Username")} : &nbsp;</label>
			    <input id="username" name="username" type="text"/>
			</div>
			<div>
			    <label for="passwd">${_("Password")} : &nbsp;</label>
			    <input id="passwd" name="passwd" type="password"/>
			</div>
			<div>
			    <label for="passwd2">${_("Repeat Password")} : &nbsp;</label>
			    <input id="passwd2" name="passwd" type="password"/>
			</div>
			<div>
			    <label for="email">${_("Email")} : &nbsp;</label>
			    <input id="email" name="email" type="text"/>
			</div>
			<div>
			    <label for="phone_mobile">${_("Mobile Phone")} : &nbsp;</label>
			    <input id="phone_mobile" name="phone_mobile" type="text"/>
			</div>
			<div>
			    <label for="phone_office">${_("Office Phone")} : &nbsp;</label>
			    <input id="phone_office" name="phone_office" type="text"/>
			</div>
			<div>
			    <label for="phone_home">${_("Home Phone")} : &nbsp;</label>
			    <input id="phone_home" name="phone_home" type="text"/>
			</div>
			<div>
			    <label for="org">${_("Organization")} : &nbsp;</label>
			    <input id="org" name="org" type="text"/>
			</div>
			<div>
			    <label for="title">${_("Title")} : &nbsp;</label>
			    <input id="title" name="title" type="text"/>
			</div>
			<div>
			    <label for="addr">${_("Address")} : &nbsp;</label>
			    <input id="addr" name="addr" type="text"/>
			</div>
		    
			<div class="submit">
			    <label for="submit">&nbsp;</label>
			    <button type="button" id="submit">${_("Submit")}</button>
			</div>
		    </form>
		</div>

	    </div>
        </div>
    </div>
</div>

<script src="/yui/3.3.0/yui/yui-min.js"> </script>
<script type="text/javascript">
//left menu
YUI({ filter: 'raw' }).use("node-menunav", function(Y) {
    var menu = Y.one("#side");
    menu.plug(Y.Plugin.NodeMenuNav);
    menu.get("ownerDocument").get("documentElement").removeClass("yui3-loading");
});

//right tab panel
YUI({ filter: 'raw' }).use("yui", "tabview", function(Y) {
    var tabview = new Y.TabView({srcNode:'#content'});
    tabview.render();
});   

//interact with server
YUI({filter: "raw"}).use("io-form", "json-parse", function(Y) {
    var onSuccess = function(id, response, args) {
	data = Y.JSON.parse(response.responseText);
	if(data.status == "failed") {
	    alert("failed");
	} else {
	    Y.config.win.location = "/main/index";
	}
    };

    var onFailure = function(id, response, args) {
	alert("sorry!");
    };

    var onClick = function(e) {
	var cfg = {
	    method: "POST",
	    form: {
		id: "loginform",
	    },
	};

        Y.io('/auth/login', cfg);
        Y.on('io:success', onSuccess, this);
        Y.on('io:failure', onFailure, this);
    };

    Y.on("click", onClick, "#submit", this, true);
}); 
</script>

</%def>


