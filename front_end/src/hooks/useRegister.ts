import axios, { AxiosError } from "axios";
import { useUrlStore } from '@/store/url'
import { ElNotification } from "element-plus";
import router from "@/router";

/**
 * @description 用户注册信息
 * @param {String} user_name 用户名
 * @param {String} password 密码
 * @param {String} email 邮箱
 * */
interface registerData {
    user_name: string;
    password: string;
    email: string;
}

export default function (registerData: registerData) {
    const urlStore = useUrlStore()
    async function register() {
        try {
            await axios({
                method: 'post',
                url: urlStore.urlRegister,
                data: registerData
            }).then(
                (response) => {
                    console.log(response, response.data)
                    if (response.data["register_result"] === "success") {
                        ElNotification({
                            message: response.data.log,
                            type: 'success',
                        })
                        const newPath = '/login'
                        console.log(newPath)
                        router.replace({ path: newPath })
                    } else if (response.data["register_result"] === "error") {
                        console.log("注册失败")
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

    return { register }

}