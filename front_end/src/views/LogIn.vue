<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <h1>登录</h1>
            </el-header>
            <el-main>
                <el-form :model="form" label-width="auto" style="min-width: 600px">
                    <el-form-item label="账户">
                        <el-input v-model="form.account" />
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="form.password" />
                    </el-form-item>
                </el-form>
            </el-main>
            <el-footer>
                <el-row justify="center">
                    <el-button type="success" @click="onSubmit">登录</el-button>
                    <el-button type="primary" @click="onSubmit">注册</el-button>
                </el-row>
            </el-footer>
        </el-container>
    </div>
</template>


<script setup lang="ts" name="LogIn">
import router from '@/router';
import { reactive } from 'vue';


const form = reactive({
    account: '',
    password: '',
})

const onSubmit = () => {
    const path = form.account + '/'
    console.log(path)
    router.replace({ path: path })
}

</script>

<style scoped>
header {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
