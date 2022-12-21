<template>
    <div class="box-card">
      <div class="card-header-title" @click="ShowDetails(info.title)">
        {{info.title}}
      </div>
      <div class="card-header">{{info.authors}}</div>
</div>
</template>

<script>
    export default {
        name: "SearchOtherResult",
        props: ["info"],
        methods:{
            ShowDetails(id){
                this.$router.push({path: `/searchDetails`, query: {q: id}})
            },
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