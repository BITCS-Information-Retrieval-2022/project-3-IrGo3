<template>
  <div class="firstPage">
  <el-row><button class="drawer" @click="drawer = true">
    <i class="elements-icons el-icongengduo"></i>
  </button></el-row>

  <el-drawer v-model="drawer" title="I am the title" :with-header="false" :direction="direction" :size="250">
    <span>这是第七组设计的搜索引擎</span>
  </el-drawer>
    <el-row class="logo">
      <span class="I">I</span><span class="R">R</span><span class="G">G</span><span class="o1">o</span><span class="o2">o</span>
      <span class="body">
      <div class="bubble"> <span></span><span></span><span></span><span></span> <span></span></div>
      <div class="bubble"> <span></span><span></span><span></span><span></span> <span></span></div>
      <div class="bubble"> <span></span><span></span><span></span><span></span> <span></span></div>
      <div class="bubble"> <span></span><span></span><span></span><span></span> <span></span></div>
      <div class="bubble"> <span></span><span></span><span></span><span></span> <span></span></div>
    </span>
    </el-row>
    </div>
    <el-row class="GrandFInput">
      <el-col :span="12" :offset="6" class="FatherInput">
        <el-input v-model="input" placeholder="输入关键字、作者、会议、期刊等" class="myinput" @keyup.enter="startSearch()">
        <template #append>
          <el-button @click="startSearch()" class="searchbtn"><i class="elements-icons el-iconsousuo"></i></el-button>
        </template>
        </el-input>
      </el-col>
    </el-row>

</template>

  

<script setup lang="ts">
import router from '../router'
import { ref } from 'vue'
const input = ref('')
const drawer = ref(false)
const direction = ref('ltr')
function startSearch(){
  if(input.value!==''){
    router.push({path: `/searchResult`, query: {q: input.value, dtype:1 }})
  }
}
</script>

<style lang="scss" scoped>
.el-iconsousuo{
  position:relative;
  left:5px;
  font-size:30px;
  color:rgb(255, 54, 128);
}
span.body {
   position:relative;
  // margin: 0;
  width:100px;
  height:100px;
  // // box-sizing: border-box;
}

.bubble {
  position: absolute;

  width: 200px;
  height: 200px;
  border-radius: 50%;
  box-shadow: inset 0 0 25px rgba(255, 255, 255, 0.25);

  animation: animate 8s ease-in-out infinite;
  zoom:0.45;
}

@keyframes animate {
  0%,
  100% {
    transform: translateY(-20px);
  }
  50% {
    transform: translateY(20px);
  }
}

.bubble::before {
  content: "";
  position: absolute;
  top: 50px;
  left: 45px;

  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #ffffff;
  filter: blur(2px);

  z-index: 10;
}
.bubble::after {
  content: "";
  position: absolute;
  top: 80px;
  left: 85px;

  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: #ffffff;
  filter: blur(2px);

  z-index: 10;
}

.bubble span {
  position: absolute;

  border-radius: 50%;
  filter: blur(8px);
}
.bubble span:nth-child(1) {
  inset: 10px;
  border-left: 20px solid rgb(0, 200, 255);
}
.bubble span:nth-child(2) {
  inset: 10px;
  border-right: 15px solid #f676a9;
}
.bubble span:nth-child(3) {
  inset: 20px;
  border-top: 15px solid #ffeb3b;
}
.bubble span:nth-child(4) {
  inset: 30px;
  border-left: 15px solid rgb(108, 232, 134);
  filter: blur(12px);
}
.bubble span:nth-child(5) {
  inset: 10px;
  border-bottom: 10px solid rgb(192, 161, 236);

  transform: rotate(330deg);
}
.drawer{
  float:left;
  border:0;
  background-color:#ffffff;
  :hover{
    color:rgb(255, 54, 128)!important;
    box-shadow: 0 0 0 0px;
  }
  :focus{
    color:rgb(255, 54, 128)!important;
    box-shadow: 0 0 0 0px;
  }
}
.el-icongengduo{
  font-size:20px;
  color:rgb(151, 149, 149)
}
.GrandFInput{
  top:40px;

}
.FatherInput{
  border-radius: 24px;
  :focus-within{
    box-shadow: rgb(161, 161, 161) 0px 0px 10px;
  }
}
.myinput{
    height:48px;
    border-radius: 24px;
    border: 2px solid rgb(193, 193, 193);
}

.searchbtn{
  height:48px;
  :focus{
    box-shadow: 0 0 0 0px;
  }
}
:deep(.myinput .el-input__inner){
    font-size: 1.2em;
    padding: 0;
    box-shadow:0 0 0 0px;
}

:deep(.myinput .el-input__wrapper){
  background-color: transparent;/*覆盖原背景颜色，设置成透明 */
  border-radius: 24px;
  border: 0;
  box-shadow:0 0 0 0px;
}
  
:deep(.myinput .el-input-group__append){
  background-color: transparent;
  border-radius: 24px;
  border: 0;
  box-shadow: 0 0 0 0px;
  :focus{
    box-shadow: 0 0 0 0px;
  }
}

.firstPage{
  overflow:hidden;
  position:relative;
  height:300px;
}
.logo{
    display: flex;
    justify-content: center;
    align-items: center;
    top:100px;
    // left:590px;
    font-size: 120px;  /*字体大小*/
    letter-spacing: 2px; /*字母间距*/
    /*font-weight:900;*/  /*加粗*/
    font-family:"Microsoft YaHei",Arial,Helvetica, Sans-Serif;
    font-weight:bold;
}
span.I{
    color: rgb(255, 54, 128);
}
span.R{
    color: rgb(0, 200, 255);
}
span.G{
    color: rgb(127, 0, 195);
}
span.o1{
    color: rgb(255, 208, 0);
}
span.o2{
    color: rgb(76, 237, 111);
    //display:inline-block;   /*设置元素旋转*/
    //transform:rotate(-15deg);

}

</style>