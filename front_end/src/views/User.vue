<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <el-container>
        <el-header>
            <TopMenu></TopMenu>
        </el-header>
        <el-container>
            <el-aside width="250px">
                <SideMenu></SideMenu>
            </el-aside>
            <el-container>
                <el-main>
                    <RouterView></RouterView>
                </el-main>
            </el-container>
        </el-container>
    </el-container>
</template>

<script setup lang="ts" name="user">
import { RouterView } from 'vue-router'
import SideMenu from '@/components/SideMenu.vue';
import TopMenu from '@/components/TopMenu.vue';

</script>

<style scoped></style>
