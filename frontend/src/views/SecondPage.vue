<style scoped>
    .search-header {
        display:flex;
        padding-top: 24px;
        overflow: hidden;
    }

    .left {
        float: left;
        margin: 0 60px;
        font-weight:bold;
    }

    .right{
        float:flex;
        width:100%;
        justify-content: flex-end;
        margin:0;
    }
    .body{
        padding-left:200px;
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
        width:800px;
    }

    .button{
        height:40px;
    }
    .num{
        padding-top:10px;
        padding-left:200px;
        padding-bottom:20px ;
        display:flex;
        font-size:40px;
        justify-content: flex-start;
    }
    .numm{
        padding-left:200px;
        display:flex;
        justify-content:flex-start;
        font-size:17px;
        color:rgb(151, 151, 151);
    }
    .adivide{
        padding-left:200px;
      
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
            <el-button @click="goHome" class="button">首页</el-button> <el-button class="button">语言</el-button>
        </div>
    </div>
        <div class="num">“{{input}}”的搜索结果</div>
        <div class="numm">约{{len}}条结果</div>
        <el-button @click="setstate(1)" class="button">学术论文</el-button>
        <el-button @click="setstate(2)" class="button">学术视频</el-button>
        <el-button @click="setstate(3)" class="button">演示文稿</el-button>
        <el-button @click="setstate(4)" class="button">E-book</el-button>
        <el-divider class="adivide"></el-divider>

        <div v-if="dtype === 1">
            <div class="body" v-for="item in result" v-bind:key="item.id"  v-loading="loading">
                <searchResult :info="item"></searchResult>
            </div>
        </div>
        <div v-else>
            <div class="body" v-for="item in result" v-bind:key="item.id"  v-loading="loading">
                <searchOtherResult :info="item"></searchOtherResult>
            </div>
        </div>
        

</template>

<script>
    import axios from 'axios'
    import SearchResult from "../components/SearchResult";
    import SearchOtherResult from "../components/SearchOtherResult";
    
    let loading=false;
    export default {
        name: "SearchMy",
        data() {
            return {
                input:"",
                len:"",
                result: [],
                loading,
                dtype:1,
            }
        },
        components: {
            searchResult: SearchResult
        },

        methods: {
            goHome() {
                this.$router.push("/")
            },
            setstate(type){
                this.dtype=type
                this.$router.push({path: `/searchResult`, query: {q: this.input, dtype:type }})
            },
            searchResult() {
                if (this.input !== '') {
                    this.$router.push({path: `/searchResult`, query: {q: this.input}})
                }
                console.info("router query:" + this.$route.query.q)
                console.info("search text: " + this.input)
                console.info("search type: " + this.dtype)

                this.loading=true;

                const path = 'http://localhost:5000/search?query='+this.$route.query.q+'&'+'dtype='+this.dtype;
                console.info(path)

                axios.get(path)
                    .then((res) => {
                        console.log(res)
                        this.result = res.data;
                        console.info(this.result)
                        console.info("1111")
                        this.loading=false;
                        this.len=this.result.length;

                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            }
        },

        created() {
            this.input=this.$route.query.q;
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
    :focus{
      box-shadow: 0 0 0 0px;
    }
  }
</style>



