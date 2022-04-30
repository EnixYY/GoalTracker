<template>
  <div class="TopNavBar">
    <router-link to="/SignUp">SignUp</router-link>
    <router-link to="/Login">Login</router-link>
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

<style>
.TopNavBar {
  height: 10vh;
  width: 100vw;
  background-color: salmon;
  display: flex;
  margin: 0;
  justify-content: space-evenly;
  align-items: center;
  color: black;
  position: absolute;
  top: 0;
}
</style>