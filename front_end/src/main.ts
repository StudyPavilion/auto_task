import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import SvgIcon from './components/SvgIcon.vue'
import './assets/iconfont/iconfont.js';
/* 引入createPinia，用于创建pinia */
import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


const app = createApp(App)

/* 创建pinia */
const pinia = createPinia()

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.use(ElementPlus)

app.use(pinia)

// 使用路由器
app.use(router)

app.component('SvgIcon', SvgIcon);

app.mount('#app')

