YUI.add("node-base",function(c){var j=".",e="nodeName",n="nodeType",b="ownerDocument",m="tagName",d="_yuid",i={},p=Array.prototype.slice,f=c.DOM,k=function(r){var q=(r.nodeType!==9)?r.uniqueID:r[d];if(q&&k._instances[q]&&k._instances[q]._node!==r){r[d]=null;}q=q||c.stamp(r);if(!q){q=c.guid();}this[d]=q;this._node=r;this._stateProxy=r;c.EventTarget.call(this,{emitFacade:true});if(this._initPlugins){this._initPlugins();}this.SHOW_TRANSITION=k.SHOW_TRANSITION;this.HIDE_TRANSITION=k.HIDE_TRANSITION;},o=function(r){var q=null;if(r){q=(typeof r=="string")?function(s){return c.Selector.test(s,r);}:function(s){return r(c.one(s));};}return q;};k.NAME="node";k.re_aria=/^(?:role$|aria-)/;k.SHOW_TRANSITION="fadeIn";k.HIDE_TRANSITION="fadeOut";k.DOM_EVENTS={abort:1,beforeunload:1,blur:1,change:1,click:1,close:1,command:1,contextmenu:1,dblclick:1,DOMMouseScroll:1,drag:1,dragstart:1,dragenter:1,dragover:1,dragleave:1,dragend:1,drop:1,error:1,focus:1,key:1,keydown:1,keypress:1,keyup:1,load:1,message:1,mousedown:1,mouseenter:1,mouseleave:1,mousemove:1,mousemultiwheel:1,mouseout:1,mouseover:1,mouseup:1,mousewheel:1,orientationchange:1,reset:1,resize:1,select:1,selectstart:1,submit:1,scroll:1,textInput:1,unload:1};c.mix(k.DOM_EVENTS,c.Env.evt.plugins);k._instances={};k.getDOMNode=function(q){if(q){return(q.nodeType)?q:q._node||null;}return null;};k.scrubVal=function(r,q){if(r){if(typeof r=="object"||typeof r=="function"){if(n in r||f.isWindow(r)){r=c.one(r);}else{if((r.item&&!r._nodes)||(r[0]&&r[0][n])){r=c.all(r);}}}}else{if(typeof r==="undefined"){r=q;}else{if(r===null){r=null;}}}return r;};k.addMethod=function(q,s,r){if(q&&s&&typeof s=="function"){k.prototype[q]=function(){var u=p.call(arguments),v=this,t;if(u[0]&&c.instanceOf(u[0],k)){u[0]=u[0]._node;}if(u[1]&&c.instanceOf(u[1],k)){u[1]=u[1]._node;}u.unshift(v._node);t=s.apply(v,u);if(t){t=k.scrubVal(t,v);}(typeof t!="undefined")||(t=v);return t;};}else{}};k.importMethod=function(s,q,r){if(typeof q=="string"){r=r||q;k.addMethod(r,s[q],s);}else{c.Array.each(q,function(t){k.importMethod(s,t);});}};k.one=function(t){var q=null,s,r;if(t){if(typeof t=="string"){if(t.indexOf("doc")===0){t=c.config.doc;}else{if(t.indexOf("win")===0){t=c.config.win;}else{t=c.Selector.query(t,null,true);}}if(!t){return null;}}else{if(c.instanceOf(t,k)){return t;}}if(t.nodeType||c.DOM.isWindow(t)){r=(t.uniqueID&&t.nodeType!==9)?t.uniqueID:t._yuid;q=k._instances[r];s=q?q._node:null;if(!q||(s&&t!==s)){q=new k(t);k._instances[q[d]]=q;}}}return q;};k.create=function(q,r){if(r&&r._node){r=r._node;}return c.one(f.create(q,r));};k.ATTRS={text:{getter:function(){return f.getText(this._node);},setter:function(q){f.setText(this._node,q);return q;}},"for":{getter:function(){return f.getAttribute(this._node,"for");},setter:function(q){f.setAttribute(this._node,"for",q);return q;}},"options":{getter:function(){return this._node.getElementsByTagName("option");}},"children":{getter:function(){var t=this._node,s=t.children,u,r,q;if(!s){u=t.childNodes;s=[];for(r=0,q=u.length;r<q;++r){if(u[r][m]){s[s.length]=u[r];}}}return c.all(s);}},value:{getter:function(){return f.getValue(this._node);},setter:function(q){f.setValue(this._node,q);return q;}}};k.DEFAULT_SETTER=function(q,s){var r=this._stateProxy,t;if(q.indexOf(j)>-1){t=q;q=q.split(j);c.Object.setValue(r,q,s);}else{if(typeof r[q]!="undefined"){r[q]=s;}}return s;};k.DEFAULT_GETTER=function(q){var r=this._stateProxy,s;if(q.indexOf&&q.indexOf(j)>-1){s=c.Object.getValue(r,q.split(j));}else{if(typeof r[q]!="undefined"){s=r[q];}}return s;};c.mix(k,c.EventTarget,false,null,1);c.mix(k.prototype,{toString:function(){var t=this[d]+": not bound to a node",s=this._node,q,u,r;if(s){q=s.attributes;u=(q&&q.id)?s.getAttribute("id"):null;r=(q&&q.className)?s.getAttribute("className"):null;t=s[e];if(u){t+="#"+u;}if(r){t+="."+r.replace(" ",".");}t+=" "+this[d];}return t;},get:function(q){var r;if(this._getAttr){r=this._getAttr(q);}else{r=this._get(q);}if(r){r=k.scrubVal(r,this);}else{if(r===null){r=null;}}return r;},_get:function(q){var r=k.ATTRS[q],s;if(r&&r.getter){s=r.getter.call(this);}else{if(k.re_aria.test(q)){s=this._node.getAttribute(q,2);}else{s=k.DEFAULT_GETTER.apply(this,arguments);}}return s;},set:function(q,s){var r=k.ATTRS[q];if(this._setAttr){this._setAttr.apply(this,arguments);}else{if(r&&r.setter){r.setter.call(this,s,q);}else{if(k.re_aria.test(q)){this._node.setAttribute(q,s);}else{k.DEFAULT_SETTER.apply(this,arguments);}}}return this;},setAttrs:function(q){if(this._setAttrs){this._setAttrs(q);}else{c.Object.each(q,function(r,s){this.set(s,r);},this);}return this;},getAttrs:function(r){var q={};if(this._getAttrs){this._getAttrs(r);}else{c.Array.each(r,function(s,t){q[s]=this.get(s);},this);}return q;},create:k.create,compareTo:function(q){var r=this._node;if(c.instanceOf(q,k)){q=q._node;}return r===q;},inDoc:function(r){var q=this._node;r=(r)?r._node||r:q[b];if(r.documentElement){return f.contains(r.documentElement,q);}},getById:function(s){var r=this._node,q=f.byId(s,r[b]);if(q&&f.contains(r,q)){q=c.one(q);}else{q=null;}return q;},ancestor:function(q,r){return c.one(f.ancestor(this._node,o(q),r));},ancestors:function(q,r){return c.all(f.ancestors(this._node,o(q),r));},previous:function(r,q){return c.one(f.elementByAxis(this._node,"previousSibling",o(r),q));},next:function(r,q){return c.one(f.elementByAxis(this._node,"nextSibling",o(r),q));},siblings:function(q){return c.all(f.siblings(this._node,o(q)));},one:function(q){return c.one(c.Selector.query(q,this._node,true));},all:function(q){var r=c.all(c.Selector.query(q,this._node));r._query=q;r._queryRoot=this._node;return r;},test:function(q){return c.Selector.test(this._node,q);},remove:function(q){var r=this._node;if(r&&r.parentNode){r.parentNode.removeChild(r);}if(q){this.destroy();}return this;},replace:function(q){var r=this._node;if(typeof q=="string"){q=k.create(q);}r.parentNode.replaceChild(k.getDOMNode(q),r);return this;},replaceChild:function(r,q){if(typeof r=="string"){r=f.create(r);}return c.one(this._node.replaceChild(k.getDOMNode(r),k.getDOMNode(q)));
},appendChild:function(q){return k.scrubVal(this._insert(q));},insertBefore:function(r,q){return c.Node.scrubVal(this._insert(r,q));},purge:function(r,q){c.Event.purgeElement(this._node,r,q);return this;},destroy:function(q){this.purge();if(this.unplug){this.unplug();}this.clearData();if(q){this.all("*").destroy();}this._node=null;this._stateProxy=null;delete k._instances[this[d]];},invoke:function(x,r,q,w,v,u){var t=this._node,s;if(r&&c.instanceOf(r,k)){r=r._node;}if(q&&c.instanceOf(q,k)){q=q._node;}s=t[x](r,q,w,v,u);return k.scrubVal(s,this);},insert:function(r,q){this._insert(r,q);return this;},_insert:function(t,r){var s=this._node,q=null;if(typeof r=="number"){r=this._node.childNodes[r];}else{if(r&&r._node){r=r._node;}}if(t&&typeof t!="string"){t=t._node||t._nodes||t;}q=f.addHTML(s,t,r);return q;},prepend:function(q){return this.insert(q,0);},append:function(q){return this.insert(q,null);},appendTo:function(q){c.one(q).append(this);return this;},setContent:function(q){this._insert(q,"replace");return this;},getContent:function(q){return this.get("innerHTML");},swap:c.config.doc.documentElement.swapNode?function(q){this._node.swapNode(k.getDOMNode(q));}:function(q){q=k.getDOMNode(q);var s=this._node,r=q.parentNode,t=q.nextSibling;if(t===s){r.insertBefore(s,q);}else{if(q===s.nextSibling){r.insertBefore(q,s);}else{s.parentNode.replaceChild(q,s);f.addHTML(r,s,t);}}return this;},getData:function(r){var q;this._data=this._data||{};if(arguments.length){q=this._data[r];}else{q=this._data;}return q;},setData:function(q,r){this._data=this._data||{};if(arguments.length>1){this._data[q]=r;}else{this._data=q;}return this;},clearData:function(q){if("_data" in this){if(q){delete this._data[q];}else{delete this._data;}}return this;},hasMethod:function(r){var q=this._node;return !!(q&&r in q&&typeof q[r]!="unknown"&&(typeof q[r]=="function"||String(q[r]).indexOf("function")===1));},SHOW_TRANSITION:null,HIDE_TRANSITION:null,show:function(q){q=arguments[arguments.length-1];this.toggleView(true,q);return this;},_show:function(){this.setStyle("display","");},_isHidden:function(){return c.DOM.getStyle(this._node,"display")==="none";},toggleView:function(q,r){this._toggleView.apply(this,arguments);},_toggleView:function(q,r){r=arguments[arguments.length-1];if(typeof q!="boolean"){q=(this._isHidden())?1:0;}if(q){this._show();}else{this._hide();}if(typeof r=="function"){r.call(this);}return this;},hide:function(q){q=arguments[arguments.length-1];this.toggleView(false,q);return this;},_hide:function(){this.setStyle("display","none");},isFragment:function(){return(this.get("nodeType")===11);},empty:function(q){this.get("childNodes").remove(q);return this;}},true);c.Node=k;c.one=c.Node.one;var a=function(q){var r=[];if(typeof q==="string"){this._query=q;q=c.Selector.query(q);}else{if(q.nodeType||f.isWindow(q)){q=[q];}else{if(c.instanceOf(q,c.Node)){q=[q._node];}else{if(c.instanceOf(q[0],c.Node)){c.Array.each(q,function(s){if(s._node){r.push(s._node);}});q=r;}else{q=c.Array(q,0,true);}}}}this._nodes=q;};a.NAME="NodeList";a.getDOMNodes=function(q){return(q&&q._nodes)?q._nodes:q;};a.each=function(q,t,s){var r=q._nodes;if(r&&r.length){c.Array.each(r,t,s||q);}else{}};a.addMethod=function(q,s,r){if(q&&s){a.prototype[q]=function(){var u=[],t=arguments;c.Array.each(this._nodes,function(z){var y=(z.uniqueID&&z.nodeType!==9)?"uniqueID":"_yuid",w=c.Node._instances[z[y]],x,v;if(!w){w=a._getTempNode(z);}x=r||w;v=s.apply(x,t);if(v!==undefined&&v!==w){u[u.length]=v;}});return u.length?u:this;};}else{}};a.importMethod=function(s,q,r){if(typeof q==="string"){r=r||q;a.addMethod(q,s[q]);}else{c.Array.each(q,function(t){a.importMethod(s,t);});}};a._getTempNode=function(r){var q=a._tempNode;if(!q){q=c.Node.create("<div></div>");a._tempNode=q;}q._node=r;q._stateProxy=r;return q;};c.mix(a.prototype,{item:function(q){return c.one((this._nodes||[])[q]);},each:function(s,r){var q=this;c.Array.each(this._nodes,function(u,t){u=c.one(u);return s.call(r||u,u,t,q);});return q;},batch:function(r,q){var s=this;c.Array.each(this._nodes,function(v,u){var t=c.Node._instances[v[d]];if(!t){t=a._getTempNode(v);}return r.call(q||t,t,u,s);});return s;},some:function(s,r){var q=this;return c.Array.some(this._nodes,function(u,t){u=c.one(u);r=r||u;return s.call(r,u,t,q);});},toFrag:function(){return c.one(c.DOM._nl2frag(this._nodes));},indexOf:function(q){return c.Array.indexOf(this._nodes,c.Node.getDOMNode(q));},filter:function(q){return c.all(c.Selector.filter(this._nodes,q));},modulus:function(t,s){s=s||0;var q=[];a.each(this,function(u,r){if(r%t===s){q.push(u);}});return c.all(q);},odd:function(){return this.modulus(2,1);},even:function(){return this.modulus(2);},destructor:function(){},refresh:function(){var t,r=this._nodes,s=this._query,q=this._queryRoot;if(s){if(!q){if(r&&r[0]&&r[0].ownerDocument){q=r[0].ownerDocument;}}this._nodes=c.Selector.query(s,q);}return this;},_prepEvtArgs:function(t,s,r){var q=c.Array(arguments,0,true);if(q.length<2){q[2]=this._nodes;}else{q.splice(2,0,this._nodes);}q[3]=r||this;return q;},on:function(s,r,q){return c.on.apply(c,this._prepEvtArgs.apply(this,arguments));},once:function(s,r,q){return c.once.apply(c,this._prepEvtArgs.apply(this,arguments));},after:function(s,r,q){return c.after.apply(c,this._prepEvtArgs.apply(this,arguments));},size:function(){return this._nodes.length;},isEmpty:function(){return this._nodes.length<1;},toString:function(){var t="",s=this[d]+": not bound to any nodes",q=this._nodes,r;if(q&&q[0]){r=q[0];t+=r[e];if(r.id){t+="#"+r.id;}if(r.className){t+="."+r.className.replace(" ",".");}if(q.length>1){t+="...["+q.length+" items]";}}return t||s;}},true);a.importMethod(c.Node.prototype,["append","destroy","detach","detachAll","empty","insert","prepend","remove","set","setContent","show","hide","toggleView"]);a.prototype.get=function(r){var u=[],t=this._nodes,s=false,v=a._getTempNode,q,w;if(t[0]){q=c.Node._instances[t[0]._yuid]||v(t[0]);w=q._get(r);if(w&&w.nodeType){s=true;}}c.Array.each(t,function(x){q=c.Node._instances[x._yuid];
if(!q){q=v(x);}w=q._get(r);if(!s){w=c.Node.scrubVal(w,q);}u.push(w);});return(s)?c.all(u):u;};c.NodeList=a;c.all=function(q){return new a(q);};c.Node.all=c.all;c.Array.each(["removeChild","hasChildNodes","cloneNode","hasAttribute","removeAttribute","scrollIntoView","getElementsByTagName","focus","blur","submit","reset","select","createCaption"],function(q){c.Node.prototype[q]=function(u,s,r){var t=this.invoke(q,u,s,r);return t;};});c.Node.importMethod(c.DOM,["contains","setAttribute","getAttribute","wrap","unwrap","generateID"]);c.NodeList.importMethod(c.Node.prototype,["getAttribute","setAttribute","removeAttribute","unwrap","wrap","generateID"]);(function(r){var q=["hasClass","addClass","removeClass","replaceClass","toggleClass"];r.Node.importMethod(r.DOM,q);r.NodeList.importMethod(r.Node.prototype,q);})(c);if(!c.config.doc.documentElement.hasAttribute){c.Node.prototype.hasAttribute=function(q){if(q==="value"){if(this.get("value")!==""){return true;}}return !!(this._node.attributes[q]&&this._node.attributes[q].specified);};}c.Node.prototype.focus=function(){try{this._node.focus();}catch(q){}return this;};c.Node.ATTRS.type={setter:function(r){if(r==="hidden"){try{this._node.type="hidden";}catch(q){this.setStyle("display","none");this._inputType="hidden";}}else{try{this._node.type=r;}catch(q){}}return r;},getter:function(){return this._inputType||this._node.type;},_bypassProxy:true};if(c.config.doc.createElement("form").elements.nodeType){c.Node.ATTRS.elements={getter:function(){return this.all("input, textarea, button, select");}};}c.mix(c.Node.ATTRS,{offsetHeight:{setter:function(q){c.DOM.setHeight(this._node,q);return q;},getter:function(){return this._node.offsetHeight;}},offsetWidth:{setter:function(q){c.DOM.setWidth(this._node,q);return q;},getter:function(){return this._node.offsetWidth;}}});c.mix(c.Node.prototype,{sizeTo:function(q,r){var s;if(arguments.length<2){s=c.one(q);q=s.get("offsetWidth");r=s.get("offsetHeight");}this.setAttrs({offsetWidth:q,offsetHeight:r});}});var l=c.NodeList,h=Array.prototype,g=["concat","pop","push","shift","slice","splice","unshift"];c.Array.each(g,function(q){l.prototype[q]=function(){var s=[],t=0,r;while(typeof(r=arguments[t++])!="undefined"){s.push(r._node||r._nodes||r);}return c.Node.scrubVal(h[q].apply(this._nodes,s));};});},"@VERSION@",{requires:["dom-base","selector-css2","event-base"]});