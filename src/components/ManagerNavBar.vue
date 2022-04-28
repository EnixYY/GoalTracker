<template>
  <div class="ManagerNavBar">
    <img v-bind:src="url" alt="Face"/>
    <h4>{{name}}</h4>
    <a>Home</a>
    <a>Create Goals</a>
    <a>Archived Goals</a>
    <a>Department</a>
    <a>Logout</a>
  </div>
</template>

<script>
export default {
  name: "ManagerNavBar",
  data(){
    return{
      name:"Lau Yu Yao",
      url:"",
    }
  }
};
</script>

<style>
.ManagerNavBar {
  height: 100vh;
  width: 25vw;
  background-color: salmon;
  display: flex;
  flex-direction: column;
  margin: 0;
  justify-content: space-evenly;
  align-items: center;
  color: black;
  position: sticky;
  top: 0;
}
</style>