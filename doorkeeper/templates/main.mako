<%inherit file="base.html"/>

<%def name="display_system_setting()">
<div id="tab_system_setting">
</div>
</%def>

<%def name="display_user_profile()">
<div id="tab_profile">
</div>
</%def>

<%def name="display_user_management()">
<div id="tab_um">
</div>
</%def>

<%def name="display_key_management()">
<div id="tab_km">
</div>
</%def>

<%def name="generate_content_tabs()">
<div  id="content">
    <ul>
	<li><a href="#tab_km" class="tablabel"> ${_('Key Management')} </a></li>
	<li><a href="#tab_um" class="tablabel"> ${_('User Management')} </a></li>
	<li><a href="#tab_system_setting" class="tablabel"> ${_('System Setting')} </a></li>
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
YUI({ filter: 'raw' }).use("node-menunav",
	"yui", "tabview",
	"io-form", "json-parse",
	"datatable",
	function(Y) {

    var menu = Y.one("#side");
    menu.plug(Y.Plugin.NodeMenuNav);
    menu.get("ownerDocument").get("documentElement").removeClass("yui3-loading");

    //right tab panel
    var tabview = new Y.TabView({
	srcNode:'#content',
    });
    tabview.render();

    //tabview.item(2).set("selected", 1);
    tabview.selectChild(2);

    //operation table
    var system_setting_columns = [
	{ key: "desc", label: "description" },
	{ key: "oper", label: "operation" },
	{ key: "note", label: "note"},
    ];
    var system_setting_data = [
	{ desc: "${_('Generate system master key')}",
	  oper: "<button class='operation' action='gen_master_key'> Act </button>",
	  note: ""
	},
	{ desc: "${_('Start/Stop Key generation service')}",
	  oper: "<button class='operation' action='toggle_service_key_gen'> Act </button>",
	  note: ""
	},
	{ desc: "${_('Start/Stop Key registration service')}",
	  oper: "<button class='operation' action='toggle_service_key_reg'> Act </button>",
          note: ""
        },
	{ desc: "${_('Publish system public parameters')}",
	  oper: "<button class='operation' action='publish_sys_params'> Act </button>",
          note: ""
        },
	{ desc: "${_('Publish revokation key list')}",
	  oper: "<button class='operation' action='public_revok_list'> Act </button>",
          note: ""
        },
    ];

    var table = new Y.DataTable.Base({
	columnset: system_setting_columns,
	recordset: system_setting_data,
    }).render("#tab_system_setting");

    table.get("boundingBox").one("table").setStyle("width", "100%");

    Y.all("#tab_system_setting .operation").on("click", function(e) {
	//alert(e.target.getAttribute("action"));
	var cfg = {
	    method: "POST",
	    data: "action=" + e.target.getAttribute("action"),
	};
	var onSuccess = function(id, response, args) {
	    data = Y.JSON.parse(response.responseText);
	    if(data.status == "SUCCESS") {
		//alert("");
	    } else {
		//Y.config.win.location = "/main/index";
	    }
	};

	var onFailure = function(id, response, args) {
	    alert("sorry!");
	};

	Y.io("${h.url(controller='main', action='do')}", cfg);
	Y.on('io:success', onSuccess);
	Y.on('io:failure', onFailure);
    });

});

</script>

</%def>


