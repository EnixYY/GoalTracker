<template>
  <div class="EmployeeNavBar">
    <img v-bind:src="url" alt="Face"/>
    <h4>{{name}}</h4>
    <router-link to="/home">Home</router-link>
    <router-link to="/assignedgoals" v-if="isManager === false">Assigned Goals</router-link>
    <router-link to="/creategoals" v-if="isManager">Create Goals</router-link>
    <router-link to="/archivedgoals">Archived Goals</router-link>
    <router-link to="/logout">Logout</router-link>
  </div>
      <!-- <router-view/> -->
</template>

<script>
export default {
  name: "EmployeeNavBar",
  data(){
    return{
      name:"Lau Yu Yao",
      url:"",
      isManager:false,
    }
  }
};
</script>

<style>
.EmployeeNavBar {
  height: 100vh;
  width: 25vw;
  background-color: salmon;
  display: flex;
  flex-direction: column;
  margin: 0;
  justify-content: space-evenly;
  align-items: center;
  color: black;
  position: absolute;
  top: 0;
}
</style>