<template>
    <div>
        <div class="grid grid-cols-6 h-screen bg-white">
            <!-- 左边栏 -->
            <div class="col-span-6 md:col-span-3 sm:col-span-6">
                <div class="login-container-left flex justify-center items-center flex-col">
                    <div class="items-center flex flex-col animate-fade-right">
                        <h2 class="font-bold text-4xl mb-7 ">自动任务 登录</h2>
                        <p class="text-white">自动执行任务平台，解放双手，轻松工作！</p>
                        <img src="@/assets/images/developer.png" class="login-image">
                    </div>
                </div>
            </div>
            <!-- 右边栏 -->
            <div class=" col-span-6 px-3 md:col-span-3 sm:col-span-6">
                <div class="login-container-right flex justify-center items-center flex-col ">
                    <h2 class="animate-fade-left font-bold text-3xl text-gray-800 mt-5">欢迎回来</h2>
                    <div class="animate-fade-left flex items-center justify-center my-5 text-gray-400 space-x-2">
                        <span class="h-[1px] w-16 bg-gray-200"></span>
                        <span>账号密码登录</span>
                        <span class="h-[1px] w-16 bg-gray-200"></span>
                    </div>
                    <div class="animate-fade-left">
                        <el-form ref="formRef" :rules="rules" :model="loginData" class="w-[300px]">
                            <el-form-item prop="username">
                                <el-input v-model="loginData.account" prefix-icon="User" placeholder="请输入用户名" size="large"
                                    clearable />
                            </el-form-item>
                            <el-form-item prop="password">
                                <el-input v-model="loginData.password" type="password" autocomplete="off" prefix-icon="Lock"
                                    placeholder="请输入密码" show-password size="large" clearable />
                            </el-form-item>
                            <el-form-item>
                                <el-button round type="primary" @click="login()" :loading="loading"
                                    class="w-[300px] mt-4" size="large">
                                    登 录
                                </el-button>
                            </el-form-item>
                            <el-form-item>
                                <el-button round type="primary" @click="toRegister()" :loading="loading"
                                    class="w-[300px] mt-4" size="large">
                                    注 册
                                </el-button>
                            </el-form-item>
                            <el-form-item>
                                <el-button round type="primary" @click="guestLogin()" :loading="loading"
                                    class="w-[300px] mt-4" size="large">
                                    游客登录
                                </el-button>
                            </el-form-item>

                        </el-form>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>


<script setup lang="ts" name="LogIn">
import useLogin from '@/hooks/useLogin';
import router from '@/router';
import { ref, onMounted, onBeforeUnmount, reactive } from 'vue';


const loginData = reactive({
    account: '',
    password: '',
})

const onSubmit = () => {
    const path = loginData.account + '/home'
    console.log(path)
    router.replace({ path: path })
}
let { login } = useLogin(loginData);

function toRegister() {
    router.replace('/register');
}
function guestLogin() {
    const newPath = 'guest' + '/home'
    router.replace({ path: newPath })
}

const rules = {
    account: [
        {
            required: true,
            message: '用户名不能为空',
            trigger: 'blur'
        }
    ],
    password: [
        {
            required: true,
            message: '密码不能为空',
            trigger: 'blur',
        },
    ]
}


const formRef = ref(null)
const loading = ref(false)

function onKeyUp(e :any) {
    console.log(e)
    if (e.key == 'Enter') {
        login()
    }
}

// 添加键盘监听
onMounted(() => {
    console.log('添加键盘监听')
    document.addEventListener('keyup', onKeyUp)
})

// 移除键盘监听
onBeforeUnmount(() => {
    document.removeEventListener('keyup', onKeyUp)
})

</script>

<style scoped>

:deep([type='text']:focus) {
    border-color: transparent !important;
}

.login-container {
    height: 100vh;
    width: 100%;
    background-color: #fff;
}

.login-container-left {
    height: 100%;
    background: #001428;
    color: #fff;
}

.login-container-right {
    height: 100%;
}

.login-image {
    /* max-width: 500px;
    height: auto; */
    height: 450px;
}
</style>
