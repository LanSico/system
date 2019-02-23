import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/home-page/home-page'
import DefaultContent from '@/components/default-page/default'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: HomePage,
      children: [
        {
          path: '/',
          name: 'DefaultContent',
          component: DefaultContent
        }
      ]
    }
  ]
})
