<template>
  <!-- <QuarkAutoTask></QuarkAutoTask> -->
  <!-- <test></test> -->
  <RouterView></RouterView>


</template>

<script setup lang="ts" name="App">
// JS或TS
import QuarkAutoTask from './views/QuarkAutoTask.vue';
import test from './components/test.vue';
import { RouterView } from 'vue-router'
</script>

<style>
/* 样式 */

h1 {
  font-size: 30px;
  margin: 0;
}
</style>
