// 创建一个路由器，并暴露出去

// 第一步：引入createRouter
import { createRouter, createWebHistory } from 'vue-router'
// 引入一个一个可能要呈现组件
import Home from '@/views/Home.vue'
import Quark from '@/views/QuarkAutoTask.vue'

// 第二步：创建路由器
const router = createRouter({
  history: createWebHistory(), //路由器的工作模式（稍后讲解）
  routes: [ //一个一个的路由规则
    {
      name:'首页',
      path:'/',
      component:Home,
    },
    {
      name:'quark',
      path:'/quark',
      component:Quark,
    },
  ]
})

// 暴露出去router
export default router