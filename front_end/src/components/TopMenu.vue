<template>
  <div>
    <el-menu router mode="horizontal" :ellipsis="false">
      <el-menu-item index="0">
        <img style="width: 50px" src="/favicon.ico" alt="Element logo" />
      </el-menu-item>

      <div class="flex-grow" />

      <el-sub-menu index="1">
        <template #title>
          <el-icon>
            <user />
          </el-icon>
          <span>用户</span>
        </template>
        <el-menu-item index="switch_account">
          <span>切换账号</span>
        </el-menu-item>
        <el-menu-item index="/login">
          <span>退出登录</span>
        </el-menu-item>
      </el-sub-menu>
    </el-menu>

  </div>
</template>

<script setup lang="ts" name="TopMenu">
import { reactive, toRefs } from 'vue'

const state = reactive({
  circleUrl:
    'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
  squareUrl:
    'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
  sizeList: ['small', '', 'large'] as const,
})

const { circleUrl, squareUrl, sizeList } = toRefs(state)

</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>
