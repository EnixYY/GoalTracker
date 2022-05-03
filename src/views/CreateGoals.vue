<template>
<div id="CreateGoalsPageHolder">
    <div>
        <SideNavBar />
        </div>
    <div id="mainHolder">
            <CreateGoalForm @create-goal="createGoal"/> 
    </div>
</div>
</template>

<script>
import CreateGoalForm from '../components/CreateGoalForm.vue'
import SideNavBar from '../components/SideNavBar.vue'
import router from '../router'
import jwt_decode from "jwt-decode";

export default {
    name: "CreateGoals",
    components: {
    CreateGoalForm,
    SideNavBar,
},
data(){
    return{
        newGoal:[],
    }
},
created(){
    this.decodeToken()
},
methods:{
    createGoal(goal, endDate, value, allocation, nameOfEmployee, percentage){
        const createNewGoal = {
            // id: name,
            goal: goal,
            endDate: endDate,
            value: value,
            allocation: allocation,
            nameOfEmployee: nameOfEmployee,
            percentage: percentage,
        }
        this.newGoal.push(createNewGoal);
        console.log(this.newGoal)
        router.push({name: 'home'})
    },
    decodeToken(){
        const token = localStorage.accessToken
        const decode = jwt_decode(token)

        console.log(decode)
    }
}
}
</script>

<style scoped>
#CreateGoalsPageHolder {
    display: flex;
    background-color: white;
}

</style>