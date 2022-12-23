<style lang="scss" scoped>
    .search-header {
        padding-top: 24px;
        overflow: hidden;
    }

    .left {
        font-weight:bold;
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
        display: flex;
        border: 1px solid rgb(165, 164, 164);
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
    .controld{
        margin-left:200px;
        margin-right:200px;
        overflow: hidden;
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
        <el-col :span="4">
            <button @click="goHome" class="button"><i class="elements-icons el-iconshouye"></i>首页</button> <button class="button"><i class="elements-icons el-iconduoyuyan"></i>语言</button>
        </el-col>
        </el-row>
    </div>
        <div class="num">“{{input}}”的搜索结果</div>
        <div class="numm">约{{len}}条结果</div>
        <button @click="setstate(1)" class="tbutton1">学术论文</button>
        <button @click="setstate(2)" class="tbutton2">学术视频</button>
        <button @click="setstate(3)" class="tbutton3">演示文稿</button>
        <button @click="setstate(4)" class="tbutton">E-book</button>
        <div class="controld"><el-divider></el-divider></div>

        <div v-if="dtype === 1">
            <div class="body" v-for="item in result" v-bind:key="item.id"  v-loading="loading">
                <searchResult :info="item"></searchResult>
            </div>
        </div>
        <div v-else-if="dtype===2">
            <div class="body" v-for="item in result" v-bind:key="item.id"  v-loading="loading">
                <searchVideo :info="item"></searchVideo>
            </div>
        </div>
        <div v-else-if="dtype===3">
            <div class="body" v-for="item in result" v-bind:key="item.id"  v-loading="loading">
                <searchPPT :info="item"></searchPPT>
            </div>
        </div>
        <div v-else>
            <div class="body" v-for="item in result" v-bind:key="item.id"  v-loading="loading">
                <searchBooks :info="item"></searchBooks>
            </div>
        </div>
        

</template>

<script>
    import axios from 'axios'
    import SearchResult from "../components/SearchResult";
    import SearchBooks from "../components/SearchBooks";
    import SearchVideo from "../components/SearchVideo";
    import SearchPPT from "../components/SearchPPT";
    
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
            searchResult: SearchResult,
            searchBooks: SearchBooks,
            searchVideo: SearchVideo,
            searchPPT:SearchPPT
        },

        methods: {
            goHome() {
                this.$router.push("/")
            },
            do_search(){
                const path = 'http://localhost:5000/search?query='+this.$route.query.q+'&'+'dtype='+this.dtype;
                console.info(path)

                axios.get(path)
                    .then((res) => {
                        this.result = res.data;
                        console.info(this.result)
                        this.loading=false;
                        this.len=this.result.length;

                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },
            setstate(type){
                this.dtype=type
                this.$router.push({path: `/searchResult`, query: {q: this.input, dtype:type }})
                this.do_search();
            },
            searchResult() {
                if (this.input !== '') {
                    this.$router.push({path: `/searchResult`, query: {q: this.input, dtype:this.dtype}})
                }
                console.info("router query:" + this.$route.query.q)
                console.info("search text: " + this.input)
                console.info("search type: " + this.dtype)

                this.loading=true;
                this.do_search();
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
  .el-iconshouye{
    font-size:18px;
    margin-right:4px;
  }
  .el-iconduoyuyan{
    font-size:18px;
    margin-right:4px;
  }
  .tbutton1{
    background-color: rgb(255,255,255);
   border:0;
    margin:0px 5px 0px 5px;
    font-size:17px;
  }
  .tbutton1:hover{
    color:rgb(255, 54, 128)!important;
  }
  .tbutton2{
    background-color: rgb(255,255,255);
    border:0;
    margin:0px 5px 0px 5px;
    font-size:17px;
  }
  .tbutton2:hover{
    color:rgb(0, 200, 255)!important;
  }
  .tbutton3{
    background-color: rgb(255,255,255);
    border:0;
    margin:0px 5px 0px 5px;
    font-size:17px;
  }
  .tbutton3:hover{
    color:rgb(127, 0, 195)!important;
  }
  .tbutton{
    background-color: rgb(255,255,255);
    border:0;
    margin:0px 5px 0px 5px;
    font-size:17px;
  }
  .tbutton:hover{
    color:rgb(255, 208, 0)!important;
  }
</style>