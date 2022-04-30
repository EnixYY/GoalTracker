<template>
<TopNavBar />
<!-- <SideNavBar v-if="hasLogin"/> -->
</template>

<script>
import TopNavBar from "../components/TopNavBar.vue"
// import SideNavBar from "./components/SideNavBar.vue"

export default {
  name: 'LandingPage',
  components:{
    TopNavBar,
    // SideNavBar,
  },
  data(){
    return{
      hasLogin:false,
    }
  }
  }

</script>