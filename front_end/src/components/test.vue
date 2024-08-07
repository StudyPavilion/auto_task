<template>
  <el-container label-width="auto" style="min-width: 400px;">
    <el-scrollbar height="75vh">
      <el-header>
        <el-row justify="center">
          <h1>夸克自动任务</h1>
        </el-row>
      </el-header>
      <el-main>
        <el-form :label-position="labelPosition" label-width="auto" :model="formLabelAlign" style="max-width: 600px">
          <div v-for="(item, index) in 4" :key="index">
            <el-form-item :label="'用户'">
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
              <el-input clearable placeholder="Please input">
              </el-input>
            </el-form-item>
            <el-form-item label="sign">
              <el-input clearable placeholder="Please input">
              </el-input>
            </el-form-item>
            <el-form-item label="vcode">
              <el-input clearable placeholder="Please input">
              </el-input>
            </el-form-item>
          </div>
        </el-form>
      </el-main>
    </el-scrollbar>
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
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormItemProps, FormProps } from 'element-plus'

const labelPosition = ref<FormProps['labelPosition']>('right')
const itemLabelPosition = ref<FormItemProps['labelPosition']>('')
const formLabelAlign = reactive({
  name: '',
  region: '',
  type: '',
})
</script>