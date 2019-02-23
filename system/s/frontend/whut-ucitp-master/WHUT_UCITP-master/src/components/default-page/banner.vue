<template>
<div>
  <swiper :options="swiperOption" ref="mySwiper" class="radius" v-if="banners.length>0">
    <swiper-slide v-for="banner in banners" :key="banner.src" :id="banner.id" class="banner animate" :style="banner.bgImg" data-ani="flipInX">
      <a :href="banner.link">
        <img :src="banner.src" class="banner-pic">
        <div class="banner-info">
          <div class="banner-info-bg" :style="banner.bgImg"></div>
          <div class="banner-text">{{banner.bannerText}}</div>
        </div>
      </a>
    </swiper-slide>
  <div class="swiper-pagination" slot="pagination"></div>
  </swiper>
</div>
</template> 

<script>
//import store from '@/store/index'
import api from '@/utils/axios'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import {mapState} from 'vuex'
export default {
  name: 'Banner',
  components: {
    swiper,
    swiperSlide
  },
  data () {
    return {
      banners: [], 
      swiperOption: {
        autoplay: true,
        speed: 1000,
        loop:true,
        pagination: {
          el: '.swiper-pagination',
          clickable:true,
        },
      }
    }
  },
  created () {
    this.$store.dispatch('banners/GET_BANNER_LIST')
    this.getdata()
  },
  computed:{
    swiper(){
      return this.$refs.mySwiper.swiper
    }
  },
  computed: mapState({
    bannerList: state => state.banners.bannerList
  }),
  methods: {
    getdata: function() {
      api.mock('/banners')
      .then(res => {
        this.banners = res.banners;
        console.log(res);
        this.$store.commit('banners/SET_BANNER_LIST',res.banners);
      })
    }
  }
}
</script>