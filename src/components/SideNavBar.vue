<template>
  <div class="EmployeeNavBar">
    <img src="https://cdn.dribbble.com/users/4226377/screenshots/14109330/cute_profile_1x.png" alt="Face"/>
    <h2>{{userName}}</h2>
    <router-link class="routerLink" to="/home">Home</router-link>
    <router-link class="routerLink" to="/assignedgoals" v-if="isManager === false">Assigned Goals</router-link>
    <router-link class="routerLink" to="/creategoals" v-if="isManager">Create Goals</router-link>
    <router-link class="routerLink" to="/archivedgoals" v-if="isManager === false">Archived Goals</router-link>
    <router-link class="routerLink" to="/managerarchivedgoals" v-if="isManager">Department Archives</router-link>
    <router-link @click="clearLocalstorage" class="routerLink" to="/logout">Logout</router-link>
  </div>
</template>

<script>
export default {
  name: "EmployeeNavBar",
  data(){
    return{
    }
  },
  props:[
    'isManager',
    'userName',
  ],
  methods:{
    clearLocalstorage(){
      localStorage.clear();
    }
  }
};
</script>

<style scoped>
.EmployeeNavBar {
  height: 100vh;
  width: 25vw;
  background-color: turquoise;
  display: flex;
  flex-direction: column;
  margin: 0;
  justify-content: space-evenly;
  align-items: center;
  color: black;
  top: 0;
  position: fixed;
}
img{
  width: 150px;
  height: 100px;
}
.routerLink{
  color: black;
}
.routerLink:hover{
  color: white;
}
</style>