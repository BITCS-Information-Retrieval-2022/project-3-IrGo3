<template>
    <!-- <p>{{info.meetings}}</p> -->
    <p class="title">{{info.title}}</p>
    <el-row>
    <el-button class="button" text>引用</el-button><el-button class="button" @click="getPDF(info.url)" text>PDF</el-button><el-button class="button" text>来源</el-button>
    <el-button class="button" text @click="GetPPT">演示文稿</el-button>
    </el-row>
    <el-card @click="openvideo" shadow="hover" class="video">视频</el-card>
    <el-dialog
      title="提示"
      v-model="dialogVisible"
      width="80%"
      height="100%"
    >
        <iframe id="showvideo" src="" 
        frameborder="0" width="100%" 
        height="600px" 
        sandbox="allow-scripts allow-same-origin allow-presentation"></iframe>
    </el-dialog>
    <el-tabs v-model="activeName" class="demo-tabs">
    <el-tab-pane label="参考文献" name="first">

    </el-tab-pane>
    <el-tab-pane label="被引用" name="second">
        <span>I sit at my window this morning where the world like a passer-by stops
      for a moment, nods to me and goes.</span>
    <el-divider />
    <span>There little thoughts are the rustle of leaves; they have their whisper
      of joy in my mind.</span>
    </el-tab-pane>
  </el-tabs>
</template>


<script>
import { ref } from 'vue'
import { TabsPaneContext } from 'element-plus'
const activeName = ref('first')
    let videourl="https://slideslive.com/38973182";
    export default {
        name: "SearchDetail",
        props: ["info"],
        data() {
            return {
                dialogVisible:false
                }
        },
        methods:{
            openvideo(){
                this.dialogVisible = true;
                this.$nextTick(()=>{
                let dom = document.getElementById('showvideo')
                dom.src=videourl
            })
                //var mydoc=document.getElementById("showvideo");
                //mydoc.src=videourl;
                //console.log(mydoc)
            },
            getPDF(url){
                if(url!==''){
                    window.location.href =url;
                }
            },
            GetVedio(url){
                if(url!==''){
                    window.location.href =url;
                }
            }
            
        }
    }
</script>
<style>
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}
.title{
    font-size:30px;
}
.button{
    float:left;
}
.video{
    padding:32px;
    margin:10px;
}
</style>
