import vue from 'vue'
import vuex from 'vuex'
vue.use(vuex)

import banners from './modules/banners'

import getters from './getters'

const store = new vuex.Store({
    modules:{
      banners
    },
    getters
})

export default store