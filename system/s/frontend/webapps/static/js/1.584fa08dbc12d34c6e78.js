webpackJsonp([1],{"9wTo":function(t,e){},"E/Fu":function(t,e){},iOp2:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a={name:"Navbar",data:function(){return{msg:"navbar",pic:{src:n("iRaI")},activeNav:0,activeMenu:0,info:{menuTitle:"菜单"},topNav:[{id:0,name:"首页",to:"/"},{id:1,name:"赛事",to:"/"},{id:2,name:"活动",to:"/"},{id:3,name:"社区",to:"/"}],sidebar:[{id:0,name:"智能推荐",to:"/",icon:"icon-AIzhineng"},{id:1,name:"最新发布",to:"/",icon:"icon-rili"},{id:2,name:"最热活动",to:"/",icon:"icon-jiasu"},{id:3,name:"即将截止",to:"/",icon:"icon-baojing"}],banner:[]}},methods:{toLink:function(t){this.activeNav=t},changeMenu:function(t){this.activeMenu=t},handleScroll:function(){var t=pageYOffset||document.documentElement.scrollTop||document.body.scrollTop;t>250?this.isFixed=1:t<200&&(this.isFixed=0)},handleAnimate:function(){var t=pageYOffset||document.documentElement.scrollTop||document.body.scrollTop,e=document.documentElement.clientHeight,n=document.querySelectorAll(".animate");[].slice.call(n).forEach(function(n){if(t+e>n.offsetTop){var a=n.dataset.delay;a?setTimeout(function(){n.style.opacity=1,n.classList.add(n.dataset.ani)},a):(n.style.opacity=1,n.classList.add(n.dataset.ani))}else n.classList.remove(n.dataset.ani),n.style.opacity=0})}},mounted:function(){var t=this;this.$nextTick(function(){t.handleAnimate(),addEventListener("scroll",t.handleScroll),addEventListener("scroll",t.handleAnimate)})},destroyed:function(){removeEventListener("scroll",this.handleScroll),removeEventListener("scroll",this.handleAnimate)}},i={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"navbar"},[t._m(0),t._v(" "),n("div",{staticClass:"wrap"},[n("div",{staticClass:"topnav"},[t._m(1),t._v(" "),n("div",{staticClass:"topnav-link"},t._l(t.topNav,function(e){return n("div",{key:e.id,staticClass:"link-item",class:{"active-link-item":e.id===t.activeNav},attrs:{to:e.to},on:{click:function(n){return t.toLink(e.id)}}},[n("span",{staticClass:"animate",class:{"active-link-a":t.activeNav===e.id},attrs:{"data-ani":"fadeInDown"},on:{click:function(n){return t.toLink(e.id)}}},[t._v(t._s(e.name))])])}),0)]),t._v(" "),n("div",{staticClass:"main"},[n("div",{staticClass:"sidebar"},[n("span",{staticClass:"menu-title"},[t._v(t._s(t.info.menuTitle))]),t._v(" "),t._l(t.sidebar,function(e){return n("a",{key:e.id,staticClass:"animate sidebar-menu",class:[{"active-menu":e.id===t.activeMenu},e.icon],attrs:{"data-ani":"fadeInDown"},on:{click:function(n){return t.changeMenu(e.id)}}},[t._v(t._s(e.name))])})],2),t._v(" "),n("div",{staticClass:"content"},[n("router-view")],1)])])])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("div",{staticClass:"web-bg"})])},function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"topnav-button"},[e("div",{staticClass:"avatar"}),this._v(" "),e("input",{staticClass:"search-input",attrs:{type:"search",autocomplete:"off",placeholder:"检索一下"}})])}]};var s={name:"HomePage",data:function(){return{}},components:{Navbar:n("C7Lr")(a,i,!1,function(t){n("E/Fu")},"data-v-b0c7a2e6",null).exports}},c={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"home-page"},[e("navbar")],1)},staticRenderFns:[]};var o=n("C7Lr")(s,c,!1,function(t){n("9wTo")},"data-v-62de4cfe",null);e.default=o.exports},iRaI:function(t,e,n){t.exports=n.p+"static/img/banner_1.7519de5.png"}});
//# sourceMappingURL=1.584fa08dbc12d34c6e78.js.map