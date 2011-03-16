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
		<li><a href="#tab_setup" class="tablabel"> ${_('System Initialization')} </a></li>
	    </ul>

	    <div>
		<div id="tab_setup">
		    <form id="initform" action="/setup/init" method="post">
			<div>
			    <label for="admin_passwd">${_("Administrator Password")} : &nbsp;</label>
			    <input id="admin_passwd" name="admin_passwd" type="text"/>
			</div>
			<div>
			    <label for="admin_passwd2">${_("Repeat Password")} : &nbsp;</label>
			    <input id="admin_passwd2" name="admin_passwd" type="text"/>
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

//ajax
YUI({filter: "raw"}).use("io-form", function(Y) {
    var onSuccess = function(id, response, args) {
	alert(response.responseText);
    };

    var onFailure = function(id, response, args) {
	alert("sorry!");
    };

    var onClick = function(e) {
	var cfg = {
	    method: "POST",
	    form: {
		id: "initform",
	    },
	};

        Y.io('/setup/init', cfg);
        Y.on('io:success', onSuccess, this);
        Y.on('io:failure', onFailure, this);
    };

    Y.on("click", onClick, "#submit", this, true);
}); 
</script>

</%def>


