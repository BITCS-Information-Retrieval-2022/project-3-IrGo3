<style scoped>
    .search-header {
        padding-top: 24px;
        overflow: hidden;
        zoom: 1;
    }

    .left {
        float: left;
        margin: 0 10px;
        
    }

    .right {
        float:left;
        overflow: hidden;
        zoom: 1;
    }

    .body{
        float:left;
        padding-left:110px;
    }
    .I{
        color: rgb(255, 54, 128);
        font-size:30px;
    }
    .R{
        color: rgb(0, 200, 255);
        font-size:30px;
    }
    span.G{
        color: rgb(127, 0, 195);
        font-size:30px;
    }
    span.o1{
        color: rgb(255, 208, 0);
        font-size:30px;
    }
    span.o2{
        color: rgb(76, 237, 111);
        font-size:30px;

    }
    .myinput{
        height:40px;
        width:1000px;
        margin:0 10px 0 0;
    }

    .button{
        height:40px;
    }
    .player{
        width:400px;
        padding-left:50px;
    }
</style>

<template>
    <div class="search-header">
        <div class="left">
            <p><span class="I">I</span><span class="R">R</span><span class="G">G</span><span class="o1">o</span><span class="o2">o</span><span class="R">o</span></p>
        </div>
        <div class="right">
            <el-input v-model="input" placeholder="输入关键字、作者、会议、期刊等" class="myinput">
            <template #append>
                <el-button @click="searchResult" class="searchbtn"><i class="elements-icons el-iconsousuo"></i></el-button>
            </template>
            </el-input>
            <el-button @click="goHome" class="button">首页</el-button><el-button class="button">语言</el-button><el-button @click="SearchVideo" class="button">学术视频</el-button>
        </div>
    </div>
    <div class="body"  v-loading="loading">
        <searchDetail :info="result"></searchDetail>
         <!-- v-bind:key="result.id" -->
    </div>
</template>

<script>
    import axios from 'axios'
    import vue from 'vue'
    import SearchDetail from "../components/SearchDetail";
    import { getIdFromURL } from "vue-youtube-embed";
    let videoId = getIdFromURL("https://www.youtube.com/watch?v=INgo33WyOP4");
    //let videourl="https://www.youtube-nocookie.com/embed/0QKhAdN-keY";
    //let videourl="https://aclanthology.org/2021.acl-long.337.mp4";
    let videourl="https://www.bilibili.com/video/BV128411G7j6?t=0.0";
    export default {
        name: "SearchMy",
        data() {
            return {
                videoId,
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
                    this.$router.push({path: `/searchResult`, query: {q: this.input, dtype:1 }})
                }
                // console.info("router query:" + this.$route.query.q)
                // console.info("search text: " + this.input)
                
                // this.loading=true;
                // console.log(this.result)

                // const path = 'http://localhost:5000/search?query='+this.$route.query.q+'&'+'dtype='+this.dtype;
                // axios.get(path)
                //     .then((res) => {
                //         this.result = res.data;
                //         console.info(this.result[0]._id)
                //         this.loading=false;

                //     })
                //     .catch((error) => {
                //         // eslint-disable-next-line
                //         console.error(error);
                //     });
            }
        },

        created() {
            console.log("kkkkk")
            this.result = this.$route.query.res
            console.log(this.result)
        }
    }
</script>
<style lang="scss" scoped>

.searchbtn{
    height:48px;
    :focus{
      box-shadow: 0 0 0 0px;
    }
  }
</style>



