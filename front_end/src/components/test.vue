<!-- eslint-disable vue/multi-word-component-names -->
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
          <h2 class="animate-fade-left font-bold text-3xl text-gray-800 mt-5">注册</h2>
          <div class="animate-fade-left flex items-center justify-center my-5 text-gray-400 space-x-2">
            <span class="h-[1px] w-16 bg-gray-200"></span>
            <span>电子邮箱注册</span>
            <span class="h-[1px] w-16 bg-gray-200"></span>
          </div>
          <div class="animate-fade-left">
            <el-form ref="formRef" :rules="rules" :model="registerData" class="w-[300px]">
              <el-form-item prop="username">
                <el-input v-model="registerData.user_name" prefix-icon="User" placeholder="请输入用户名" size="large" clearable />
              </el-form-item>
              <el-form-item prop="password">
                <el-input v-model="registerData.password" type="password" autocomplete="off" prefix-icon="Lock"
                  placeholder="请输入密码" show-password size="large" clearable />
              </el-form-item>
              <el-form-item>
                <el-input v-model="registerData.email" placeholder="请输入电子邮箱">
                  <template #append>
                    <el-select v-model="emailType" style="width: 120px">
                      <el-option label="@qq.com" value="@qq.com" />
                      <el-option label="@163.com" value="@163.com" />
                    </el-select>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item prop="code">
                <div class="grid grid-cols-5 gap-2">
                  <el-input class="col-span-3" v-model="registerData.code" size="large" autocomplete="off"
                    placeholder="请输入验证码" />
                  <el-button class="col-span-2" type="primary" size="large" @click="getCode()">获取验证码</el-button>
                </div>
              </el-form-item>
              <el-form-item>
                <el-button round type="primary" @click="register()" :loading="loading" class="w-[300px] mt-4"
                  size="large">
                  注 册
                </el-button>
              </el-form-item>
              <el-form-item>
                <el-button round type="primary" @click="toLogin()" :loading="loading" class="w-[300px] mt-4" size="large">
                  去 登 录
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
import router from '@/router';
import { ref, onMounted, onBeforeUnmount, reactive } from 'vue';

let emailType = ref('@qq.com')


const formRef = ref(null)
const loading = ref(false)

import useRegister from '@/hooks/useRegister';

const registerData = reactive({
  user_name: '',
  password: '',
  email: '',
  code: '',
  emailType
})

const rules = {
  user_name: [
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
  ],
  confirmPassword: [
    {
      required: true,
      message: '确认密码不能为空',
      trigger: 'blur',
    },
  ],
  email: [
    {
      required: true,
      message: '邮箱不能为空',
      trigger: 'blur',
    },
  ],
  code: [
    {
      required: true,
      message: '验证码不能为空',
      trigger: 'blur',
    },
  ],
}

let { register, getCode } = useRegister(registerData);
function toLogin() {
    router.replace('/login');
}
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
