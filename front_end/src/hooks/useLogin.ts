import axios, { AxiosError } from "axios";
import { useUrlStore } from '@/store/url'
import { ElNotification } from "element-plus";
import router from "@/router";

/**
 * @description 用户列表
 * @param {String} account 用户名
 * @param {String} password 密码
 * */
interface loginData {
    account: string;
    password: string;
}

export default function (loginData: loginData) {
    const urlStore = useUrlStore()
    async function login() {
        try {
            await axios({
                method: 'post',
                url: urlStore.urlLogin,
                data: loginData
            }).then(
                (response) => {
                    console.log(response, response.data)
                    if (response.data["login_result"] === "success") {
                        ElNotification({
                            message: response.data.log,
                            type: 'success',
                        })
                        const newPath = loginData.account + '/home'
                        console.log(newPath)
                        router.replace({ path: newPath })
                    } else if (response.data["login_result"] === "error") {
                        console.log("登录失败")
                        console.log(response)
                        ElNotification({
                            message: response.data.log,
                            type: 'error',
                        })
                    } else {
                        console.log("未知错误");
                    }
                },
                (error) => {
                    console.log("错误", error.message);
                    ElNotification({
                        title: '错误',
                        message: error.message,
                        type: 'error',
                    })
                }
            );
        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }
    }

    return { login }

}