import { defineStore } from 'pinia'
import { reactive } from 'vue'
import Home from '@/views/Home.vue'
import Quark from '@/views/QuarkAutoTask.vue'

export const useMenuStore = defineStore('menu', () => {
    const sideMenu = reactive([
        {
            name: '首页',
            path: '/',
            component:Home,
            meta: { iconType: 'elementPlus', icon: "HomeFilled" },
        },
        {
            name: '夸克',
            path: '/quark',
            component:Quark,
            meta: { iconType: 'iconfont', icon: "icon-kuake" },
        },

    ]);

    return { sideMenu }
})