<template>
<div>
<TopNavBar />
</div>
<div id="mainHolder">
  <h1>Goäl Träcker</h1>
  <img src="https://miro.medium.com/max/903/1*Vme2Cdne8NJhbaGuRc4rww.jpeg"/>
</div>
</template>

<script>
import TopNavBar from "../components/TopNavBar.vue"

export default {
  name: 'LandingPage',
  components:{
    TopNavBar,
  },
  data(){
    return{
    }
  }
  }

</script>

<style scoped>
img{
width: 100vw;
height: 70vh;
}
#mainHolder{
  display: flex;
  flex-direction: column;
}
</style>

