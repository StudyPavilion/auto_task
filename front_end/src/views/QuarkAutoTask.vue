<template>
  <!-- 返回页面顶部的操作按钮 -->
  <el-backtop :right="100" :bottom="100" />

  <div class="common-layout">
    <el-container>
      <el-container>
        <el-container label-width="auto" style="min-width: 400px;">
          <!-- 顶栏 -->
          <el-header>
            <el-row justify="center">
              <h1>夸克自动任务</h1>
            </el-row>
          </el-header>
          <!-- 主要区域 -->
          <el-container>
            <el-main>
              <el-scrollbar height="70vh">
                <el-form size="large" label-width="auto" :model="softwareConfig" @submit.prevent="saveSoftConfig(softwareConfig)">
                  <el-form-item label="定时规则">
                    <el-input v-model="softwareConfig.crontab" clearable placeholder="请输入定时规则">
                    </el-input>
                  </el-form-item>
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
              </el-scrollbar>
            </el-main>

            <!-- 底栏 -->
            <el-footer>
              <!-- 将底栏固定在底部-->
              <el-affix position="bottom" :offset="0">
                <el-row justify="center" class="bottom-buttons">
                  <el-button-group>
                    <el-button type="success" @click="saveSoftConfig(softwareConfig)">保存配置</el-button>
                    <el-button type="primary" @click="runTaskAll(softwareConfig)">运行任务</el-button>
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
import { reactive, ref } from "vue";
import useTaskData from "@/hooks/useTaskData";

const isCollapse = ref(false);
let SidebarStatus = ref("折叠侧边栏");

let software = "quark";

let { softwareConfig, saveSoftConfig, runScriptNow, runTaskAll } = useTaskData(software);

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
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
header {
  display: flex;
  justify-content: center;
  align-items: center;
}

:deep(.el-form-it)em__label {  
  font-size: 25px; /* 更改字体大小 */  
  /* 你可以在这里添加更多的样式 */  
}  
.svg-icon {
  width: 18px;
  height: 18px;
}

.bottom-buttons {
  background-color: white;
}
</style>
