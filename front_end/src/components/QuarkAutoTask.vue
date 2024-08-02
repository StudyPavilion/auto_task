<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-container>
          <el-main>
            <el-form>
              <div v-for="(user, index) in userList" :key="index">
                <!-- <template> -->
                <hr>
                <el-row justify="start">

                  <el-col :span="6">
                    <span>用户{{ index + 1 }}</span>
                  </el-col>

                  <el-col :span="6">
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
                  </el-col>
                </el-row>
                <el-row>
                  <el-input v-model="userList[index].kps" clearable style="max-width: 600px" >
                    <template #prepend>kps</template>
                  </el-input>
                </el-row>

                <el-row>
                  <el-input v-model="userList[index].sign" clearable style="max-width: 600px"
                    placeholder="Please input">
                    <template #prepend>sign</template>
                  </el-input>
                </el-row>

                <el-row>
                  <el-input v-model="userList[index].vcode" clearable style="max-width: 600px"
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
          <el-footer>Footer</el-footer>
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


let url_base = "http://127.0.0.1:5000"
// 运行任务
let run_task = "/run_task"

let read_config = "/read_config"

let url = url_base + read_config
let software = "quark"
let { userList } = useTaskData({ url, software });

// let userList: any = reactive([])

let newUser = reactive(
  {
    kps: "",
    sign: "",
    vcode: "",
  }
)

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

<style scoped></style>
