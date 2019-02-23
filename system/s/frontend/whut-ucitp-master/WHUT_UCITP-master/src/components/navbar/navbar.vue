<template>
  <div class="navbar">
    <div>
      <div class="web-bg"></div>
    </div>
    <div class="wrap">
      <div class="topnav">
        <div class="topnav-button">
          <div class="avatar"></div>
          <input class="search-input" type="search" autocomplete="off" placeholder="检索一下">
        </div>
        <div class="topnav-link" >
          <div v-for="item in topNav" :key="item.id" :to="item.to" class="link-item"  :class="{'active-link-item': item.id===activeNav}" @click="toLink(item.id)"><span class="animate" :class="{'active-link-a': activeNav===item.id}" @click="toLink(item.id)" data-ani="fadeInDown">{{item.name}}</span></div>
        </div>
      </div>
      <div class="main">
        <div class="sidebar">
          <span class="menu-title">{{info.menuTitle}}</span>
          <a v-for="item in sidebar" :key="item.id" class="animate sidebar-menu" data-ani="fadeInDown" :class="[{'active-menu': item.id===activeMenu},item.icon]"  @click="changeMenu(item.id)">{{item.name}}</a>
        </div>
        <div class="content">
          <router-view/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
      msg: 'navbar',
      pic: {
        src: require('../../assets/images/banner_1.png')
      },
      activeNav: 0,
      activeMenu: 0,
      info: {
        menuTitle: '菜单'
      },
      topNav: [
        {
          id: 0,
          name: '首页',
          to: '/'
        },
        {
          id: 1,
          name: '赛事',
          to: '/'
        },
        {
          id: 2,
          name: '活动',
          to: '/'
        },
        {
          id: 3,
          name: '社区',
          to: '/'
        }
      ],
      sidebar: [
        {
          id: 0,
          name: '智能推荐',
          to: '/',
          icon: 'icon-AIzhineng'
        },
        {
          id: 1,
          name: '最新发布',
          to: '/',
          icon: 'icon-rili'
        },
        {
          id: 2,
          name: '最热活动',
          to: '/',
          icon: 'icon-jiasu'
        },
        {
          id: 3,
          name: '即将截止',
          to: '/',
          icon: 'icon-baojing'
        }
      ],
      banner: []
    }
  },
  methods: {
    toLink (index) {
      this.activeNav = index
    },
    changeMenu (index) {
      this.activeMenu = index
    },    
    handleScroll() {
      let top =
        pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      if (top > 250) {
        this.isFixed = 1;
      } else if (top < 200) {
        this.isFixed = 0;
      }
    },
    handleAnimate() {
      let top =
        pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      let vh = document.documentElement.clientHeight;
      let dom = document.querySelectorAll(".animate");
      [].slice.call(dom).forEach(v => {
        if (top + vh > v.offsetTop) {
          var delay = v.dataset.delay;
          if (delay) {
            setTimeout(() => {
              v.style.opacity = 1;
              v.classList.add(v.dataset.ani);
            }, delay);
          } else {
            v.style.opacity = 1;
            v.classList.add(v.dataset.ani);
          }
        } else {
          v.classList.remove(v.dataset.ani);
          v.style.opacity = 0;
        }
      });
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.handleAnimate(); //初始化第一次加载时在视口内就执行元素加载动画
      addEventListener("scroll", this.handleScroll);
      addEventListener("scroll", this.handleAnimate);
    });
  },
  destroyed() {
    removeEventListener("scroll", this.handleScroll); //避免影响其他页面
    removeEventListener("scroll", this.handleAnimate);
  }
};
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  @import "~assets/stylus/variable"
  .web-bg
    background-image $pic-background
    position fixed
    top 0
    left 0
    width 100%
    height 100%
    min-width 1000px
    z-index -10
    zoom 1
    background-color #fff
    background-repeat no-repeat
    background-size cover
    -webkit-background-size cover
    -o-background-size cover
    background-position center 0
  .wrap
    background $color-background
    width $wrap-width
    height $wrap-height
    position absolute
    left 0
    top 0
    right 0
    bottom 0
    margin auto
    border-radius $border-radius-b
    display flex
    flex-direction column
    overflow hidden
    .topnav
      width 100%
      height $topnav-height
      border-bottom $border-l
      display flex
      flex-direction row-reverse
      flex-shrink 0
      .topnav-button
        padding 30px 35px
        display flex
        flex-direction row-reverse
        .avatar
          height $topnav-button-height
          width $topnav-button-height
          background $color-gradient
          border-radius 50%
        .search-input
          background $color-theme
          border none
          width 330px
          height $topnav-button-height
          border-radius ($topnav-button-height/2)
          margin 0 100px
          text-indent 2rem
          color $color-text-xl
          font-family  $font
        input::-ms-input-placeholder
          text-indent 0
          color $color-text-xl
          text-align center
        input::-webkit-input-placeholder
          text-indent 0
          color $color-text-xl
          text-align center
    .topnav-link
      height 100%
      display flex
      flex-direction row
      .link-item
        display inline-block
        color $color-text
        padding 0 40px
        line-height $topnav-height
        font-size $font-size-large
        font-family $font-r
        height 100%
      .active-link-item
        color $color-theme-l
        background $color-background-l
        .active-link-a
          padding-bottom 8px
          position relative
        .active-link-a:after
          content ''
          position absolute
          left 12px
          top auto
          bottom 0
          right auto
          height 4px
          width 20px
          background-color $color-theme-l
          box-shadow 0rem 0.25rem 0.25rem rgba(50, 83, 248, 0.25),
                      0rem 0.5rem 0.5rem rgba(50, 83, 248, 0.25),
                      0rem 1rem 1rem rgba(50, 83, 248, 0.25),
                      0rem 2rem 2rem rgba(50, 83, 248, 0.25),
                      0rem 4rem 4rem rgba(50, 83, 248, 0.25);
  .main
    flex-grow 1
    display flex
    flex-direction row
    .sidebar
      width $sidebar-width
      border-right $border-l
      display flex
      flex-direction column
      font-family $font-r
      font-size $font-size-large
      flex-shrink 0
      .menu-title
        padding 50px 0 40px
        text-align left
        text-indent 4rem
      .sidebar-menu
        height $sidebar-menu-height
        line-height $sidebar-menu-height
        margin-bottom $margin-flow
      .active-menu
        background $color-background-l
        color $color-text-l
        border-left 5px solid $color-theme-d
    .content
      flex-grow 1
      background $color-background-d
      padding $padding $padding 0
      overflow-x hidden
      overflow-y scroll
      -ms-overflow-style none
    .content::-webkit-scrollbar
      display none

    //animate classs
    .animate
      opacity 0
    .fadeInDown
      animation fadeInDown 1s
    .zoomInDown
      animation zoomInDown 1s
</style>
