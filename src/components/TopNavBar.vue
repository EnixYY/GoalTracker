<template>
  <div class="TopNavBar">
    <router-link class="routerLink" to="/SignUp">SignUp</router-link>
    <router-link class="routerLink" to="/Login">Login</router-link>
  </div>
</template>

<script>
export default {
  name: "TopNavBar",
  data(){
    return{

    }
  }
};
</script>

<style scoped>
.TopNavBar {
  height: 8vh;
  width: 100vw;
  background-color: turquoise;
  display: flex;
  margin: 0;
  justify-content: space-evenly;
  align-items: center;
  color: black;
  position: absolute;
  top: 0;
}
.routerLink{
  color: white;
}
.routerLink:hover{
  color: black;
}
</style>