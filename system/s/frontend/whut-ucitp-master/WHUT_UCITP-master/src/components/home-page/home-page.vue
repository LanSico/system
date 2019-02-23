<template>
  <div class="home-page">
    <navbar/>
  </div>
</template>

<script>
import Navbar from '@/components/navbar/navbar'
export default {
  name: 'HomePage',
  data () {
    return {
    }
  },
  components: {
    Navbar
  }
}
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  @import "~assets/stylus/variable"
</style>
