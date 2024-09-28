<template>
    <div>
        <el-menu router class="meun"  >
            <MenuTree :menuList="sideMenu"></MenuTree>
        </el-menu>
    </div>
</template>

<script setup lang="ts" name="SideMenu">
import MenuTree from './MenuTree.vue'
import useMenu from "@/hooks/useMenu";
let { sideMenu } = useMenu();


</script>

<style scoped>
.meun {
    transition: all 0.3s;
    width: 250px;
    top: 0;
    bottom: 0;
    left: 0;
    overflow-y: auto;
    overflow-x: hidden;
    /* background-color: #001428!important; */
}

</style>
