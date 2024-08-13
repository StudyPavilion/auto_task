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
              <el-menu-item index="log_out">
                <span>退出登录</span>
              </el-menu-item>
            </el-sub-menu>
          </el-menu>
    </div>
</template>

<script setup lang="ts" name="TopMenu">


</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>
