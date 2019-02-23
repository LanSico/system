<template>
    <div class="contest">
      <span class="card-title">{{contestTitle}}</span>
      <div class="contest-card-wrapper">
        <div class="contest-card" v-for="item in contestList" :key="item.id" >
          <div class="contest-pic" style="background-position:center center;" :style="{backgroundImage:'url(' + item.picUrl + ')'}"></div>
          <div class="contest-info">
            <span class="contest-title" v-bind:title="item.title">{{item.title}}</span>
            <p class="contest-host">{{item.host}}</p>
            <div class="contest-period">
              <span v-for="period in item.periods" :key="period.id" class="period" :style="{background:item.color+'!important'}">
                {{period.time}}
              </span>
            </div>
          </div>
          <div class="contest-progress">
            <div class="progress-bar-bg"></div>
            <div class="progress-bar" :style="{width:0.6*item.percent+'%!important',background:item.color+'!important'}">
            </div>
          </div>
        </div>
      </div>
    </div>
</template> 

<script>
import api from '@/utils/axios'
export default {
  name: 'Contest',
  data () {
    return {
      contestTitle: '报名ing！',
      contestList: []
    }
  },
  created () {
    this.getdata()
  },
  methods: {
    getdata: function() {
      api.mock('/contest')
      .then(res => {
        console.log(res);
        this.contestList = res.contest;
      })
    }
  }
}
</script>