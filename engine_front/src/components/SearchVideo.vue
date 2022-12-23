<template>
    <div class="box-card">
      <div class="card-header-title" @click="ShowDetails(info.title)">
        {{info.title}}
      </div>
      <div class="card-header">Related papers:{{info.paper}}</div>
    <div class="card-body">
        <div id="absarea" class="abst"><label class="btn" for="showAbs"></label>{{ info.description}}</div>
        <el-row>
        <button class="button" text> <i class="elements-icons el-iconyuanshuju-yinyong"></i>引用</button>
        <button class="button" @click="getSource(info.bvid)"><i class="elements-icons el-iconpdf"></i>来源</button>
        </el-row>
    </div>
</div>
</template>

<script>
    export default {
        name: "SearchBooks",
        props: ["info"],
        data(){
            return {
                isabs:false,
            }
        },
        methods:{
            getPDF(url){
                if(url!==''){
                    window.location.href =url;
                }
            },
            ShowDetails(id){
                this.$router.push({path: `/searchDetails`, query: {res: this.info}})
            },
            getSource(url){
                if(url!==''){
                    window.open(url);
                }
            }
        },
        mounted:function(){
        this.$nextTick(function(){
            if(this.info.abstract){
                this.isabs=true;
            }
        })
    }
    }
</script>
<style>

.atooltip {
    border:0;
    border-radius: 12px;
    background: rgb(0, 0, 0,0.8)!important;
    color:rgb(255, 255, 255);
}

</style>
<style lang="scss" scoped> 
.card-body{
    margin:3px;
}
.Fabst {
    display:flex;
    width:800px;
    margin:0;
    }
.abst {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin:2px;
}
#showAbs:checked+.abst{
  -webkit-line-clamp: 999; 
}
#showAbs:checked + .abst .btn::after {
    content: '收起';
}
#showAbs:checked + .abst .btn::before {
    visibility: hidden;
}
.abst::before{
    content: '';
  height: calc(100% - 22px);
  float: right;
}
.btn{
    float: right;
  clear: both;
  background: rgb(93, 16, 188);
  line-height: 20px;
  border-radius: 5px;
  color:  #fff;
  border:0;
}
.btn::after{
    content: '展开';
}
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

   .button{
    padding:2px 20px 0px 0px;
    margin:0px 5px 5px 0px;
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
</style>