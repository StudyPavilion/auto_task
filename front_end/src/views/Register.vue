<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <h1>注册</h1>
            </el-header>
            <el-main>
                <el-form :model="registerData" label-width="auto" style="min-width: 600px">
                    <el-form-item label="账户">
                        <el-input v-model="registerData.user_name" />
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="registerData.password" />
                    </el-form-item>
                    <el-form-item label="电子邮箱">
                        <el-input v-model="registerData.email" />
                    </el-form-item>
                </el-form>
            </el-main>
            <el-footer>
                <el-row justify="center">
                    <el-button type="primary" @click="register">立即注册</el-button>
                </el-row>
            </el-footer>
        </el-container>
    </div>
</template>

<script setup lang="ts" name="Register">
import useRegister from '@/hooks/useRegister';
import { reactive } from 'vue';

const registerData = reactive({
    user_name: '',
    password: '',
    email: ''
})

let { register } = useRegister(registerData);

</script>

<style scoped>
    
</style>
