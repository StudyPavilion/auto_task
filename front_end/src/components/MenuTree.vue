<template>
    <div class="menu-tree">
        <template v-for="item in props.menuList" :key="item.path">
            <!-- {{ item }} -->
            <!--      分为两种方式渲染：有子菜单和没有子菜单-->
            <el-sub-menu :index="item.path" v-if="item.children">
                <template #title>
                    <span>{{ item.name }}</span>
                </template>
                <!-- 有子菜单的继续遍历（递归）-->
                <MenuTree :menuList="item.children"></MenuTree>
            </el-sub-menu>
            <!-- 没有子菜单 -->
            <el-menu-item :index="item.path" v-if="!item.children">
                <el-icon>
                    <div v-if="item.meta.iconType =='iconfont'">
                        <svg-icon :iconName="item.meta.icon"></svg-icon>
                    </div>
                    <div v-else-if="item.meta.iconType == 'elementPlus'">
                        <component :is="item.meta.icon"></component>
                    </div>
                </el-icon>
                <span>{{ item.name }}</span>
                <!-- <span>{{ item.path }}</span> -->
            </el-menu-item>
        </template>
    </div>
</template>

<script setup lang="ts" name="MenuTree">

const props = defineProps(['menuList'])
console.log("props.menuList:", props.menuList)
</script>

<style scoped>
span, .svg-icon, .el-icon {
    font-size: 25px;
}
</style>
