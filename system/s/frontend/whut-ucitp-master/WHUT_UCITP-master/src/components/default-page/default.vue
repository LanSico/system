<template>
  <div class="box">
    <banner></banner>
    <recommend></recommend>
    <contest></contest>
  </div>
</template>

<script>

import Banner from './banner'
import Recommend from './recommend'
import Contest from './contest'

export default {
  name: 'default',
  components: {
    Banner,
    Recommend,
    Contest
  },
  data () {
    return {

    }
  },
  methods: {
    handleScroll () {
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
    handleAnimate () {
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
      this.handleAnimate(); //初始化第一次加载时在视口内就执行动画
      addEventListener("scroll", this.handleScroll);
      addEventListener("scroll", this.handleAnimate);
    });
  },
  destroyed() {
    removeEventListener("scroll", this.handleScroll); //避免影响其他页面
    removeEventListener("scroll", this.handleAnimate);
  }
}
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
</style>
