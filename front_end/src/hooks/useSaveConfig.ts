import axios, { AxiosError } from "axios";
import { reactive, ref } from "vue";

/**
 * @description 保存配置
 * @param {String} url 接口地址
 * @param {String} software 软件名称
 * */
interface saveConfig {
    url: string;
    // software: string;
    config: {};
}

export default function ({ url, config }: saveConfig) {
    const saveConfigResult = ref(0)
    async function saveConfig() {
        try {

            // 发请求
            const { data, status } = await axios({
                method: 'post',
                url: url,
                // data: {
                //     software: software
                // }
                data: config
            })
            console.log("data: ", data, "status: ", status)

        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }


    }

    return { saveConfigResult, saveConfig };
}