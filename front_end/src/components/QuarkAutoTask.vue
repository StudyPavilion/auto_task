<template>

  <el-backtop :right="100" :bottom="100" />

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

  <div class="common-layout">
    <el-container>

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
          </el-menu>
        </el-scrollbar>
      </el-aside>

      <el-container>
        <el-header>
          <el-row justify="center">
            <h1>夸克自动任务</h1>
          </el-row>
        </el-header>
        <el-container>
          <el-main>
            <el-form>
              <div v-for="(user, index) in userList" :key="index">
                <!-- <template> -->
                <hr>
                <el-row justify="space-between">
                  <el-col :span="3">
                    <span>用户{{ index + 1 }}</span>
                  </el-col>
                  <el-col :span="21">
                    <el-row justify="end">
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
                    </el-row>

                  </el-col>
                </el-row>
                <el-row>
                  <el-input v-model="userList[index].kps" clearable style="min-width: 600px">
                    <template #prepend>kps</template>
                  </el-input>
                </el-row>

                <el-row>
                  <el-input v-model="userList[index].sign" clearable style="min-width: 600px"
                    placeholder="Please input">
                    <template #prepend>sign</template>
                  </el-input>
                </el-row>

                <el-row>
                  <el-input v-model="userList[index].vcode" clearable style="min-width: 600px"
                    placeholder="Please input">
                    <template #prepend>vcode</template>
                  </el-input>
                </el-row>

                <!-- </template> -->
              </div>
              <el-button type="primary" @click="addUser">
                <el-icon style="vertical-align: middle">
                  <Plus />
                </el-icon>
                <span style="vertical-align: middle">增加用户</span>
              </el-button>
            </el-form>
          </el-main>
          <el-footer>Footer1</el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts" name="QuarkAutoTask">
import axios from 'axios';
import { reactive, ref } from 'vue';
import { ElMessage } from 'element-plus';
import useTaskData from '@/hooks/useTaskData';

const isCollapse = ref(false)
let SidebarStatus = ref("折叠侧边栏")
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

let url_base = "http://127.0.0.1:5000"
// 运行任务
let run_task = "/run_task"

let read_config = "/read_config"

let url = url_base + read_config
let software = "quark"
let { userList } = useTaskData({ url, software });

let newUser = reactive(
  {
    kps: "",
    sign: "",
    vcode: "",
  }
)

function toggleSidebarStatus() {
  isCollapse.value = !isCollapse.value
  if (isCollapse.value === false) {
    SidebarStatus.value = "折叠侧边栏"
  }
  else {
    SidebarStatus.value = "展开侧边栏"
  }
}

function addUser() {
  newUser = {
    kps: "",
    sign: "",
    vcode: "",
  }
  userList.push(newUser);
  console.log(userList)
}

function removeUser(index: number) {
  userList.splice(index, 1);
}

function runScriptNow(user_index: number) {
  console.log("runScriptNow", user_index)
  // 发起一个post请求
  axios({
    method: 'post',
    url: url_base + run_task,
    data: {
      kps: userList[user_index].kps,
      sign: userList[user_index].sign,
      vcode: userList[user_index].vcode,
    }
  }).then(response => {
    // console.log(response, response.data)
    if (response.data["task_result"] === "success") {
      ElMessage({
        message: response.data,
        type: 'success',
      })
      // console.log("任务执行成功")
    }
    else if (response.data["task_result"] === "error") {
      ElMessage.error(response.data)
      // console.log("任务执行失败")
    }
    else {

      console.log("未知错误")
    }

  }, error => {
    console.log('错误', error.message)
    ElMessage({
      message: error.message,
      type: 'error',
    })
  });
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
</style>
