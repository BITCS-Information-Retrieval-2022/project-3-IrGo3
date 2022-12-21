import { createApp } from 'vue'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import '/assert/font_engine/iconfont.css'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.min.css'
import VideoPlayer from 'vue-video-player'
import 'video.js/dist/video-js.css'

createApp(App).use(store).use(router).use(ElementPlus).use(Antd).use(VideoPlayer).mount('#app')

