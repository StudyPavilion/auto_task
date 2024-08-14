import { defineStore } from 'pinia'
import { reactive } from 'vue'
import Home from '@/views/Home.vue'
import Quark from '@/views/QuarkAutoTask.vue'
import User from '@/views/User.vue'
import LogIn from '@/views/LogIn.vue'
import { markRaw } from 'vue'

export const useMenuStore = defineStore('menu', () => {
    const sideMenu = reactive([
        {
            name:'用户',
            path:'/:user',
            component:markRaw(User),
            children:[
              {
                name:'首页',
                path:'home',
                component:markRaw(Home),
                meta: { iconType: 'elementPlus', icon: "HomeFilled" },
              },
              {
                name:'夸克',
                path:'quark',
                component:markRaw(Quark),
                meta: { iconType: 'iconfont', icon: "icon-kuake" },
              }
            ]
          },
          {
            name:'主页',
            path:'/',
            redirect:'/login'
          },
          {
            name:'登录',
            path:'/login',
            component:markRaw(LogIn),
          },
          {
            name:'退出登录',
            path:'/log_out',
            redirect:'/login'
          },

    ]);

    return { sideMenu }
})