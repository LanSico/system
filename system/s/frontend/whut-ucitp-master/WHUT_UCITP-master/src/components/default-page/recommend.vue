<template>
    <div class="recommend">
      <span class="card-title">{{recommendTitle}}</span>
      <div class="recommend-card-wrapper">
        <div class="recommend-card" v-for="item in recommenList" :key="item.id" >
          <div class="recommend-pic" :style="{backgroundImage:'url(' + item.picUrl + ')',backgroundSize:'cover'}"></div>
          <div class="recommend-info">
            <span class="recommend-title" v-bind:title="item.title">{{item.title}}</span>
            <p class="recommend-introduce">{{item.introduce}}</p>
            <div class="participants">
              <div v-for="(participant,index) in item.participants" :key="index" class="participant" :style="{backgroundImage:'url(' + participant.picUrl + ')'}">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template> 

<script>

import api from '@/utils/axios'
export default {
  name: 'Recommend',
  data () {
    return {
      recommendTitle: '今日推荐',
      recommenList: []
    }
  },
  created () {
    this.getdata()
  },
  methods: {
    getdata: function() {
      api.mock('/recommend')
      .then(res => {
        console.log(res);
        this.recommenList = res.recommenList;
      })
    }
  }
}
</script>