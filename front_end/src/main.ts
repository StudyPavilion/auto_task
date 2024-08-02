import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import SvgIcon from './components/SvgIcon.vue'
import './assets/iconfont/iconfont.js';

import { createApp } from 'vue'

import App from './App.vue'

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.use(ElementPlus)

app.component('SvgIcon', SvgIcon);

app.mount('#app')


