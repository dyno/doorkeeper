YUI.add("dd-plugin",function(b){var a=function(c){c.node=((b.Widget&&c.host instanceof b.Widget)?c.host.get("boundingBox"):c.host);a.superclass.constructor.call(this,c);};a.NAME="dd-plugin";a.NS="dd";b.extend(a,b.DD.Drag);b.namespace("Plugin");b.Plugin.Drag=a;},"@VERSION@",{requires:["dd-drag"],optional:["dd-constrain","dd-proxy"],skinnable:false});