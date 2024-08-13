<template>
  <!-- <QuarkAutoTask></QuarkAutoTask> -->
  <!-- <test></test> -->
  <el-container>
    <el-header>
      <TopMenu></TopMenu>
    </el-header>
    <el-container>
      <el-aside width="200px">
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

<script setup lang="ts" name="App">
// JS或TS
import QuarkAutoTask from './views/QuarkAutoTask.vue';
import test from './components/test.vue';
import { RouterView } from 'vue-router'
import SideMenu from './components/SideMenu.vue';
import TopMenu from './components/TopMenu.vue';
</script>

<style>
/* 样式 */

h1 {
  font-size: 30px;
  margin: 0;
}
</style>
