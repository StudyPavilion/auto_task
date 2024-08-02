import { reactive, onMounted } from 'vue'
import axios, { AxiosError } from 'axios'
/**
 * @description 获取用户列表
 * @param {String} url 接口地址
 * @param {String} software 软件名称
 * */
interface useGetUserList {
    url: string;
    software: string;
} 

/**
 * @description 获取用户列表
 * @param {String} url 接口地址
 * @param {String} software 软件名称
 * */
interface userList {
    url: string;
    software: string;
} 

export default function ({url, software}: useGetUserList) {
    // const userList = reactive<string[]>([])
    const userList: any = reactive([])

    // 方法
    async function getUserList(software: string) {
        try {
            
            // 发请求
            const { data } = await axios({
                method: 'get',
                url: url,
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

    // 挂载钩子
    onMounted(() => {
        getUserList(software)
    })

    //向外部暴露数据
    return { userList, getUserList }
}