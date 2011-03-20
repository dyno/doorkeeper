<%inherit file="base.html"/>

<%def name="display_system_setting()">
<div id="tab_setup">
    <form id="initform" method="post">
	## if not generic yet
	## if no master key
	${_("Generate system master key")}
	## what's this?
	${_("Public system public parameters")} 
	## toggle
	${_("Start/Stop Key generation service")}
	## expiration or registration?
	${_("Start/Stop Key expiration service")}
	${_("Publish Revocation key list")}
    </form>
</div>
</%def>

<%def name="display_user_profile()">
<div>
</div>
</%def>

<%def name="display_user_management()">
<div>
</div>
</%def>

<%def name="display_key_management()">
<div>
</div>
</%def>

<%def name="generate_content_tabs()">
<div  id="content">
    <ul>
	<li><a href="#tab_km" class="tablabel"> ${_('Key Management')} </a></li>
	<li><a href="#tab_um" class="tablabel"> ${_('User Management')} </a></li>
	<li><a href="#tab_system" class="tablabel"> ${_('System Setting')} </a></li>
	<li><a href="#tab_profile" class="tablabel"> ${_('User Profile')} </a></li>
    </ul>

    <div>
	${self.display_key_management()}
	${self.display_user_management()}
	${self.display_system_setting()}
	${self.display_user_profile()}
    </div>
</div>
</%def>

##-----------------------------------------------------------------------------
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
    ${self.generate_content_tabs()}
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


