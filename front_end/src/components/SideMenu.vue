<template>
    <div>
        <el-menu router >
            <MenuTree :menuList="sideMenu"></MenuTree>
        </el-menu>
    </div>
</template>

<script setup lang="ts" name="SideMenu">
import MenuTree from './MenuTree.vue'
import useMenu from "@/hooks/useMenu";
let { sideMenu } = useMenu();


</script>

<style scoped></style>
