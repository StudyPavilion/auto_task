import { reactive, onMounted, ref } from 'vue'
import axios, { AxiosError } from 'axios'
import { useUrlStore } from '@/store/url'
import { ElMessage, ElMessageBox } from 'element-plus';
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
    crontab: string,
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
    const softwareConfig = reactive<softwareConfig>({ software: '', userList: [], crontab: '' })

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
            console.log("getSoftwareConfig", data)
            // 维护数据
            softwareConfig.software = data["software"]
            softwareConfig.userList = data["userList"]
            softwareConfig.crontab = data["crontab"]
        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }
    }

    async function saveSoftConfig(softwareConfig: softwareConfig) {
        try {

            // 发请求
            await axios({
                method: 'post',
                url: urlStore.urlSaveConfig,
                data: softwareConfig
            }).then(
                (response) => {
                    console.log(response, response.data)
                    if (response.data["task_result"] === "success") {
                        ElMessage({
                            message: response.data.log,
                            type: "success",
                        });
                        // console.log("任务执行成功")
                    } else if (response.data["task_result"] === "error") {
                        console.log("任务执行失败")
                        console.log(response)
                        ElMessageBox.alert(response.data.log, '错误', {
                            confirmButtonText: '我已了解',
                        })
                    } else {
                        console.log("未知错误");
                    }
                },
                (error) => {
                    console.log("错误", error.message);
                    ElMessage({
                        message: error.message,
                        type: "error",
                    });
                }
            );
        } catch (error) {
            // 处理错误
            const err = <AxiosError>error
            console.log(err.message)
        }
    }

    async function runScriptNow(user_index: number) {
        // console.log("runScriptNow", user_index);
        // 发起一个post请求
        axios({
            method: "post",
            url: urlStore.urlRunTask,
            data: softwareConfig.userList[user_index]
        }).then(
            (response) => {
                // console.log(response, response.data)
                if (response.data["task_result"] === "success") {
                    ElMessage({
                        message: response.data.log,
                        type: "success",
                    });
                    // console.log("任务执行成功")
                } else if (response.data["task_result"] === "error") {
                    console.log("任务执行失败")
                    console.log(response)
                    ElMessageBox.alert(response.data.log, '错误', {
                        confirmButtonText: '我已了解',
                    })
                } else {
                    console.log("未知错误");
                }
            },
            (error) => {
                console.log("错误", error.message);
                ElMessage({
                    message: error.message,
                    type: "error",
                });
            }
        );
    }

    async function runTaskAll(softwareConfig: softwareConfig) {
        saveSoftConfig(softwareConfig)
        console.log("runTaskAll");
        axios({
            method: "post",
            url: urlStore.urlRunTask,
            data: softwareConfig.userList
        }).then(
            (response) => {
                // console.log(response, response.data)
                if (response.data["task_result"] === "success") {
                    ElMessage({
                        message: response.data.log,
                        type: "success",
                    });
                    // console.log("任务执行成功")
                } else if (response.data["task_result"] === "error") {
                    console.log("任务执行失败")
                    console.log(response)
                    ElMessageBox.alert(response.data.log, '错误', {
                        confirmButtonText: '我已了解',
                    })
                } else {
                    console.log("未知错误");
                }
            },
            (error) => {
                console.log("错误", error.message);
                ElMessage({
                    message: error.message,
                    type: "error",
                });
            }
        );
    }

    // 挂载钩子
    onMounted(() => {
        getSoftwareConfig(software)
    })

    //向外部暴露数据
    return { softwareConfig, getSoftwareConfig, saveSoftConfig, runScriptNow, runTaskAll }
}