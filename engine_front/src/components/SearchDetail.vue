<template>
    <p class="title">{{info.title}}</p>
    <el-row>
    <button class="button"> <i class="elements-icons el-iconyuanshuju-yinyong"></i>引用</button><button class="button"><i class="elements-icons el-iconpdf"></i>来源</button>
    <button class="button" @click="GetPPT"><i class="elements-icons el-iconppt"></i>演示文稿</button>
    </el-row>

      <p class="pabs">摘要</p>
      <span class="abs">{{ info.abstract }}</span>

    <el-card @click="openvideo" shadow="hover" class="video">
      <img src="../../assert/video.png" class="image" />
      <input id="inputurl" class="videobutton" value="" />
    </el-card>
    <el-dialog
      v-model="dialogVisible"
      width="80%"
      height="100%"
      :fullscreen="true"
      :show-close="false"
    >
    <template #header="{ close }" >
      <el-row>
        <el-col :offset="23" :span="1">
      <button class="button" @click="close"><i class="elements-icons el-iconcha"></i></button>
    </el-col>
      </el-row>
   </template>
   <el-row>
   <el-col :offset="3" :span="4" ><button class="videohead" @click="GetVideo(info.video_url)">跳转至视频源地址</button></el-col>
   </el-row>
   <el-row>
    <el-col :offset="3" :span="18">
      <div class="conloading" v-loading="loading">
        <iframe v-loading="loading" ref="iframm" id="showvideo" src="" 
        frameborder="0" width="100%" 
        height="600px" 
        sandbox="allow-scripts allow-same-origin allow-presentation"></iframe>
      </div>
      </el-col>
   </el-row>
    </el-dialog>
    <el-tabs v-model="activeName" class="demo-tabs">
    <el-tab-pane label="参考文献" name="first">

    </el-tab-pane>
    <el-tab-pane label="被引用" name="second">
      <span class="cited">hi</span>
        <el-divider/>
    </el-tab-pane>
  </el-tabs>
</template>


<script>
import { ref } from 'vue'
import { TabsPaneContext } from 'element-plus'
const activeName = ref('first');
    export default {
        name: "SearchDetail",
        props: ["info"],
        data() {
            return {
                dialogVisible:false,
                loading:false,
                isabs:false,
                }
        },
        methods:{
            openvideo(){
                this.dialogVisible = true;
                this.$nextTick(()=>{
                let dom = document.getElementById('showvideo')
                dom.src=this.info.video_url;
                console.log(dom.src);
                this.loading=true;
                const iframe = this.$refs.iframm;
                if (iframe.attachEvent) { // IE
                  iframe.attachEvent('onload', () => { this.loading = false; });
                } else { // 非IE
                  iframe.onload =  () => { this.loading = false; };
                }

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
            GetVideo(url){
                if(url!==''){
                    window.open(url);
                }
            }
            
        },
        mounted:function(){
        this.$nextTick(function(){
                //调用需要执行的方法
                let dom = document.getElementById('inputurl')
                var str= this.info.video_url;
                if(str==null){
                  dom.value="Not Found";
                }else{
                if(str.match("youtube")){
                  dom.value="www.youtube.com";
                }else if(str.match("bilibili")){
                  dom.value="www.bilibili.com";
                }else if(str.match("slideslive")){
                  dom.value="www.slideslive.com";
                }
              }
                console.log(dom.value);
                if(this.infoabstract){
                this.isabs=true;
            }
        })      
        }
    }
</script>
<style>
.Fabs{
  padding-left:20px;
  padding-right:100px;
  margin-bottom:20px;
}
.pabs{
  font-size:18px;
  font-weight: bold;
  display:flex;
  justify-content: start;
  margin-top:5px;
  margin-bottom:5px;
}
.abs{
  display:flex;
  justify-content: start;
  margin-bottom:10px;
  text-align: justify;
  text-justify:distribute-all-lines;
  width: 550px;
}
.el-divider{
  margin:2px;
  
}
.cited{
  font-size:18px;
  font-family:Arial,Microsoft;
  color:black;
  display:flex;
  justify-content: flex-start;
}
.conloading{
  background-color:rgb(155, 151, 151)
}
.el-loading-spinner .path{
      stroke: rgb(255, 54, 128);
      stroke-width:4px;
    }
.videohead{
  border:0;
  background-color:#ffffff;
  display:flex;
  font-size:20px;
}
  .videohead:hover{
color:rgb(255, 54, 128);
  }
.demo-tabs{
  padding-right:100px;
}
.demo-tabs > .el-tabs__content {
  padding: 0px;
}
.demo-tabs .el-tabs__item:hover {
  color: rgb(0, 200, 255);
}
/*选中样式*/
.demo-tabs .el-tabs__item.is-active {
  color: rgb(0, 200, 255);
}
.demo-tabs .el-tabs__active-bar {
  background-color: rgb(0, 200, 255);
}
.title{
    font-size:30px;
}
.button{
    padding:2px 20px 0px 0px;
    margin:0px 5px 0px 5px;
  border:0;
  background-color:#ffffff;
   }
    .button:hover{
    color:rgb(255, 54, 128)!important;
    box-shadow: 0 0 0 0px;
  }
  .button:focus{
    color:rgb(255, 54, 128)!important;
    box-shadow: 0 0 0 0px;
  }

  .el-iconcha{
    font-size:25px;
    
  }
.video{
    padding:32px;
    margin:10px;
    width:480px;
    height:250px;
}
.image{
  width:100px;
  position:absolute;
  text-align:center;
  vertical-align:middle;
}
.videobutton{
  width:140px;
  height:40px;
  border-radius:4px;
  position: relative;
  top:-30px;
  left:150px;
  border:0;
  font-size:14px;
  padding-left:14px;
  color:rgb(255,255,255);
  background-color:rgb(241, 81, 140) ;
}
</style>

