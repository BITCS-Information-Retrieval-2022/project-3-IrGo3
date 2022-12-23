<style lang="scss" scoped>
    .search-header {
        padding-top: 24px;
        overflow: hidden;
        zoom: 1;
    }

    .left {
        font-weight:bold;
    }


    .body{
        float:left;
        padding-left:110px;
    }
    .I{
        color: rgb(255, 54, 128);
        font-size:30px;
        font-family: 'Times New Roman',Arial;
    }
    .R{
        color: rgb(0, 200, 255);
        font-size:30px;
        font-family: 'Times New Roman', Arial;
    }
    span.G{
        color: rgb(127, 0, 195);
        font-size:30px;
        font-family: 'Times New Roman', Arial;
    }
    span.o1{
        color: rgb(255, 208, 0);
        font-size:30px;
        font-family: 'Times New Roman',Arial;
    }
    span.o2{
        color: rgb(76, 237, 111);
        font-size:30px;
        font-family: 'Times New Roman', Arial;

    }
    .myinput{
        height:40px;
        margin:0 10px 0 0;
        border: 1px solid rgb(165, 164, 164);
        display:flex;
        border-radius: 24px;
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
    .button{
        height:40px;
    }
    .player{
        width:400px;
        padding-left:50px;
    }
    .el-iconsousuo{
  position:relative;
  font-size:30px;
  color:rgb(255, 54, 128);
}
</style>

<template>
    <div class="search-header">
        <el-row>
        <el-col :span="4" class="left">
            <p><span class="I">I</span><span class="R">R</span><span class="G">G</span><span class="o1">o</span><span class="o2">o</span><span class="R">o</span></p>
        </el-col>
        <el-col :span="12">
            <el-input v-model="input" placeholder="输入关键字、作者、会议、期刊等" class="myinput">
            <template #append>
                <el-button @click="searchResult" class="searchbtn"><i class="elements-icons el-iconsousuo"></i></el-button>
            </template>
            </el-input>
        </el-col>
        <el-col :span="6">
            <button @click="goHome" class="button"><i class="elements-icons el-iconshouye"></i>首页</button> <button class="button"><i class="elements-icons el-iconduoyuyan"></i>语言</button><el-button @click="SearchVideo" class="button2">学术视频</el-button>
        </el-col>
        </el-row>
    </div>
    <div class="body"  v-loading="loading" v-bind:key="result._id">
        <searchDetail :info="result"></searchDetail>
    </div>
</template>

<script>
    import axios from 'axios'
    import vue from 'vue'
    import SearchDetail from "../components/SearchDetail";
    import { getIdFromURL } from "vue-youtube-embed";
    //let videourl="https://www.youtube-nocookie.com/embed/0QKhAdN-keY";
    //let videourl="https://aclanthology.org/2021.acl-long.337.mp4";
    //let videourl="https://www.bilibili.com/video/BV128411G7j6?t=0.0";
    export default {
        name: "SearchMy",
        data() {
            return {
                input: "",
                result: [],
                dialogVisible:false,
                loading:false,
                }
        },
        components: {
            searchDetail: SearchDetail
        },

        methods: {

            goHome() {
                this.$router.push("/")

            },
            searchResult() {
                if (this.input !== '') {
                    this.$router.push({path: `/searchResult`, query: {q: this.input}})
                }
                console.info("router query:" + this.$route.query.q)
                console.info("search text: " + this.input)
                
                this.loading=true;

                const path = 'http://localhost:5000/search?query='+this.$route.query.res+'&'+'dtype=5';
                axios.get(path)
                    .then((res) => {
                        this.result = res.data;
                        console.info(this.result)
                        this.loading=false;

                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            }
        },

        created() {
            this.searchResult();
        },

        watch: {
            '$route'(to, from) {
                // 对路由变化作出响应...
                this.searchResult()
            }
        }
    }
</script>
<style lang="scss" scoped>
.searchbtn{
    height:48px;
    background-color: rgb(255,255,255);
  }
  .button{
    background-color: rgb(255,255,255);
    width: 80px;
    height:40px;
    border:0;
    margin:0px 5px 0px 5px;
  }
  .button:hover{
    color:rgb(127, 0, 195);
  }
  .button:focus{
    color:rgb(127, 0, 195);
  }
  
  .button2{
    background-color: rgb(255,255,255);
    width: 80px;
    height:40px;
    border:0;
    margin:0px 5px 0px 5px;
  }
  .button2:hover{
    color:rgb(0, 200, 255);
  }
  .button2:focus{
    color:rgb(0, 200, 255);
  }
  .el-iconshouye{
    font-size:18px;
    margin-right:4px;
  }
  .el-iconduoyuyan{
    font-size:18px;
    margin-right:4px;
  }
</style>



