import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUrlStore = defineStore('url', () => {
    const urlBase = ref("http://127.0.0.1:5000");

    const urlLogin = ref(urlBase.value + "/login");

    const urlRegister = ref(urlBase.value + "/register");

    const urlGetCode = ref(urlBase.value + "/get_code");

    // 运行任务
    const urlRunTask = ref(urlBase.value + "/run_task");

    const urlReadConfig = ref(urlBase.value + "/read_config");

    const urlSaveConfig = ref(urlBase.value + "/save_config");

    return { urlBase, urlLogin, urlRegister, urlGetCode, urlRunTask, urlReadConfig, urlSaveConfig, }
})