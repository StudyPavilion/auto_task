<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <SideMenu></SideMenu>
      </el-aside>
      <el-main>
        <RouterView></RouterView>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup name="App">
import { RouterView } from 'vue-router'
import SideMenu from './SideMenu.vue'

</script>

<style>
</style>