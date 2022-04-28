<template>
  <EmployeeNavBar/>
  <WelcomeCard/>
  <OverallGoalsCard/>
</template>

<script>
import OverallGoalsCard from './components/OverallGoalsCard.vue'
import WelcomeCard from './components/WelcomeCard.vue'
import EmployeeNavBar from './components/EmployeeNavBar.vue'

export default {
  name: 'App',
  components: {
    OverallGoalsCard,
    WelcomeCard,
    EmployeeNavBar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
