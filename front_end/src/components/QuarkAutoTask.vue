<template>
  <!-- 返回页面顶部的操作按钮 -->
  <el-backtop :right="100" :bottom="100" />

  <div class="common-layout">
    <el-container style="height: 100vh">
      <el-header>
        <!-- 将顶部菜单固定在顶部 -->
        <el-affix :offset="0">
          <el-menu class="el-menu-demo" mode="horizontal" :ellipsis="false" @select="handleSelect">
            <el-menu-item index="0">
              <img style="width: 100px" src="/favicon.ico" alt="Element logo" />
            </el-menu-item>
            <div class="flex-grow" />

            <el-sub-menu index="1">
              <template #title>
                <el-icon>
                  <user />
                </el-icon>
                <span>用户</span>
              </template>
              <el-menu-item index="1-1">
                <span>切换账号</span>
              </el-menu-item>
              <el-menu-item index="1-2">
                <span>退出登录</span>
              </el-menu-item>
            </el-sub-menu>
          </el-menu>
        </el-affix>
      </el-header>
      <el-container>

        <!-- 侧栏 -->
        <el-aside width="200px">
          <el-scrollbar>
            <div>
              <el-button type="" @click="toggleSidebarStatus()" style="margin-bottom: 20px">
                点我{{ SidebarStatus }}
              </el-button>
            </div>

            <el-menu default-active="2" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
              @close="handleClose">
              <el-menu-item index="1">
                <el-icon>
                  <svg-icon class="icon" iconName="icon-kuake"></svg-icon>
                </el-icon>
                <template #title>夸克</template>
              </el-menu-item>
              <el-menu-item index="2">
                <el-icon>
                  <setting />
                </el-icon>
                <template #title>设置</template>
              </el-menu-item>
              <el-menu-item index="3">
                <el-icon>
                  <setting />
                </el-icon>
                <template #title>设置</template>
              </el-menu-item>
              <el-menu-item index="4">
                <el-icon>
                  <setting />
                </el-icon>
                <template #title>设置</template>
              </el-menu-item>
              <el-menu-item index="5">
                <el-icon>
                  <setting />
                </el-icon>
                <template #title>设置</template>
              </el-menu-item>
              <el-menu-item index="6">
                <el-icon>
                  <setting />
                </el-icon>
                <template #title>设置</template>
              </el-menu-item>
              <el-menu-item index="7">
                <el-icon>
                  <setting />
                </el-icon>
                <template #title>设置</template>
              </el-menu-item>
            </el-menu>
          </el-scrollbar>
        </el-aside>

        <el-container label-width="auto" style="min-width: 400px;">
          <!-- 顶栏 -->
          <el-header>
            <el-row justify="center">
              <h1>夸克自动任务</h1>
            </el-row>
          </el-header>
          <!-- 主要区域 -->
          <el-container>
            <el-scrollbar>
              <el-main>
                <el-form :model="softwareConfig" @submit.prevent="saveSoftConfig(softwareConfig)">
                  <div v-for="(user, index) in softwareConfig.userList" :key="index">
                    <el-form-item :label="'用户' + (softwareConfig.userList[index].name)">
                      <el-button-group>
                        <el-button type="primary" @click="runScriptNow(index)">
                          <el-icon style="vertical-align: middle">
                            <Edit />
                          </el-icon>
                          <span style="vertical-align: middle">立即执行</span>
                        </el-button>

                        <el-button type="danger" @click="removeUser(index)">
                          <el-icon style="vertical-align: middle">
                            <Delete />
                          </el-icon>
                          <span style="vertical-align: middle">删除用户</span>
                        </el-button>
                      </el-button-group>
                    </el-form-item>
                    <el-form-item label="kps">
                      <el-input v-model="softwareConfig.userList[index].kps" clearable placeholder="Please input">
                      </el-input>
                    </el-form-item>
                    <el-form-item label="sign">
                      <el-input v-model="softwareConfig.userList[index].sign" clearable placeholder="Please input">
                      </el-input>
                    </el-form-item>
                    <el-form-item label="vcode">
                      <el-input v-model="softwareConfig.userList[index].vcode" clearable placeholder="Please input">
                      </el-input>
                    </el-form-item>
                  </div>
                  <el-form-item>
                    <el-button type="primary" @click="addUser">
                      <el-icon>
                        <Plus />
                      </el-icon>
                      <span>新增用户</span>
                    </el-button>
                  </el-form-item>
                </el-form>
              </el-main>
            </el-scrollbar>
            <!-- 底栏 -->
            <el-footer>
              <!-- 将底栏固定在底部-->
              <el-affix position="bottom" :offset="0">
                <el-row justify="center" class="bottom-buttons">
                  <el-button-group>
                    <el-button type="success" @click="saveSoftConfig(softwareConfig)">保存配置</el-button>
                    <el-button type="primary" @click="saveSoftConfig(softwareConfig)">运行任务</el-button>
                  </el-button-group>
                </el-row>
              </el-affix>
            </el-footer>
          </el-container>

        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts" name="QuarkAutoTask">
import axios from "axios";
import { reactive, ref } from "vue";
import { ElMessage } from "element-plus";
import useTaskData from "@/hooks/useTaskData";

const isCollapse = ref(false);
let SidebarStatus = ref("折叠侧边栏");
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};

let software = "test";

let { softwareConfig, saveSoftConfig, runScriptNow } = useTaskData(software);

let newUser = reactive({
  name: "",
  kps: "",
  sign: "",
  vcode: "",
});

function toggleSidebarStatus() {
  isCollapse.value = !isCollapse.value;
  if (isCollapse.value === false) {
    SidebarStatus.value = "折叠侧边栏";
  } else {
    SidebarStatus.value = "展开侧边栏";
  }
}

function addUser() {
  newUser = {
    name: "",
    kps: "",
    sign: "",
    vcode: "",
  };
  softwareConfig.userList.push(newUser);
  console.log(softwareConfig.userList);
}

function removeUser(index: number) {
  softwareConfig.userList.splice(index, 1);
}

function onSubmit() {
  console.log("submit!");
  console.log("form.name:",);
  console.log("form:", softwareConfig.software);
}

</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}

.svg-icon {
  width: 18px;
  height: 18px;
}

.bottom-buttons {
  background-color: white;
}
</style>
