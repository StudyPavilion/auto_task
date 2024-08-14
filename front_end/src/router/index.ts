// 创建一个路由器，并暴露出去

// 第一步：引入createRouter
import { createRouter, createWebHistory } from 'vue-router'
// 引入一个一个可能要呈现组件
import { useMenuStore } from '@/store/menu'
import Home from '@/views/Home.vue'
import Quark from '@/views/QuarkAutoTask.vue'
import LogIn from '@/views/LogIn.vue'
import User from '@/views/User.vue'
// 第二步：创建路由器
const router = createRouter({
  history: createWebHistory(), //路由器的工作模式（稍后讲解）
  routes: [ //一个一个的路由规则
    {
      name:'用户',
      path:'/:user',
      component:User,
      children:[
        {
          name:'首页',
          path:'home',
          component:Home,
          meta: { iconType: 'elementPlus', icon: "HomeFilled" },
        },
        {
          name:'quark',
          path:'quark',
          component:Quark,
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
      component:LogIn,
    },
    {
      name:'退出登录',
      path:'/log_out',
      redirect:'/login'
    },
  ]
})


// 暴露出去router
export default router