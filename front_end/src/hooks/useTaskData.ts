import { reactive, onMounted, ref } from 'vue'
import axios, { AxiosError } from 'axios'
import {useUrlStore} from '@/store/url'
/**
 * @description 用户列表
 * @param {String} name 用户名
 * @param {String} kps 参数1
 * @param {String} sign 参数2
 * @param {String} vcode 参数3
 * */
interface userList {
    name: string;
    kps: string;
    sign: string;
    vcode: string;
} 

/**
 * @description 软件配置
 * @param {String} software 软件名称
 * @param {userList[]} userList 用户列表
 * */
interface softwareConfig {
    software: string;
    userList: userList[],
}

/**
 * @description 获取软件配置信息
 * @param {String} url 接口地址
 * @param {String} software 软件名称
 * */
interface getSoftwareConfig {
    url: string;
    software: string;
}



export default function (software: string) {
    const urlStore = useUrlStore()
    const userList = reactive<userList[]>([])
    const softwareConfig = reactive<softwareConfig>({software: '', userList: []})

    // 方法
    async function getUserList(software: string) {
        try {
            
            // 发请求
            const { data } = await axios({
                method: 'get',
                url: urlStore.urlReadConfig,
                params: {
                    software: software
                },

            })
            // console.log(data)
            // 维护数据
            for (const item of data) {
                userList.push(item);
            }
            
        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }
    }

    // 获取软件配置信息
    async function getSoftwareConfig(software: string) {
        try {
            
            // 发请求
            const { data } = await axios({
                method: 'get',
                url: urlStore.urlReadConfig,
                params: {
                    software: software
                },

            })
            console.log("getSoftwareConfig",data)
            // 维护数据
            softwareConfig.software = data["software"]
            softwareConfig.userList = data["userList"]

            
        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }
    }
    
    async function saveSoftConfig(config: any) {
        try {

            // 发请求
            const { data, status } = await axios({
                method: 'post',
                url: urlStore.urlSaveConfig,
                data: config
            })
            console.log("data: ", data, "status: ", status)

        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }


    }

    // 挂载钩子
    onMounted(() => {
        // getUserList(software)
        getSoftwareConfig(software)
    })

    //向外部暴露数据
    return { softwareConfig, getSoftwareConfig, saveSoftConfig }
}