<template>
<div id="assignedPageHolder">
    <div>
        <SideNavBar/>
    </div>
    <div id="goalsHolder">
        <GoalsCard 
        v-for="goal in goals" 
        :key="goal.goalTitle" 
        :goal-title="goal.goalTitle"
        :due-date="goal.dueDate"
        :percentage="goal.percentage"
        />
    </div>
</div>
</template>;

<script>
import GoalsCard from "../components/GoalsCard.vue"
import SideNavBar from "../components/SideNavBar.vue"

export default {
    name: "AssignedGoals",
    components: {
        GoalsCard,
        SideNavBar,
    },
    data(){
        return{
        goals:[
            {
                goalTitle:"Quarterly Story points",
                dueDate:"06 May 2022",
                percentage: 0,
            },
            {
                goalTitle:"Current Sprint Story Point",
                dueDate:"06 May 2022",
                percentage: 0,
            }
            ]
    }
    },
    methods:{
    }
}
</script>

<style scoped>
#assignedPageHolder {
    display: flex;
    background-color: white;
}
#goalsHolder{
    display: flex;
    justify-content: space-evenly;
    height: 100vh;
    width: 75vw;
}
</style>