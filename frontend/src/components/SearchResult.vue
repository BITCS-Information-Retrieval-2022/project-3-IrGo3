<template>
    <div class="box-card">
      <div class="card-header-title" @click="ShowDetails(info.title)">
        {{info.title}}
      </div>
      <div v-if="info.authors != '[]'">
        <div class="card-header">{{info.authors}}</div>
      </div>
    <div class="card-body">
        <el-button class="button" text>引用</el-button><el-button class="button" @click="getPDF(info.url)" text>PDF</el-button><el-button class="button" text>来源</el-button>
        <el-tooltip popper-class="atooltip" placement="bottom" effect="light"><template v-slot:content>{{info.video_url}}</template>
        <el-button class="button" text @click="GetVedio(info.video_url)">相关视频</el-button></el-tooltip>
        <el-button class="button" text @click="GetPPT">演示文稿</el-button>
    </div>
</div>
</template>

<script>
    export default {
        name: "SearchResult",
        props: ["info"],
        methods:{
            getPDF(url){
                if(url!==''){
                    window.location.href =url;
                }
            },
            ShowDetails(id){
                console.log("ooooo")
                console.info(this.info)
                this.$router.push({path: `/searchDetails`, query: {res: this.info.arxiv_id}})
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

.atooltip.el-tooltip__popper [x-placement^="bottom"] .popper__arrow {
  background-color: pink !important;
}
.atooltip.el-tooltip__popper[x-placement^="bottom"] .popper__arrow::after {
  border-bottom-color: pink !important;
}
.atooltip {
    border:0;
    border-radius: 24px;
    background: rgb(203, 190, 240)!important;
}

</style>
<style scoped> 
    div {
        margin-top: 12px;
    }
    .box-card{
       box-shadow:0;
    }
    .card-header{
        display: flex;
        justify-content: start;
    }

    .card-header-title{
        display: flex;
        justify-content: start;
        font-size: 16px;
        color:rgb(93, 16, 188);
    }
    .card-body{
        display:flex;
    }
    .describe {
        padding: 12px 0 0 0;
        text-align: center;
        color: #d04713;
    }
  
</style>