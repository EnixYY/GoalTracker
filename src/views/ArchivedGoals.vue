<template>
<div id="archivePageHolder">
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
    name: "ArchivedGoals",
    components: {
        GoalsCard,
        SideNavBar,
    },
    data(){
        return{
        goals:[
            {
                goalTitle:"Quarterly Story points",
                dueDate:"06 May 2021",
                percentage: 100,
            },
            {
                goalTitle:"Current Sprint Story Point",
                dueDate:"06 May 2021",
                percentage: 100,
            }
            ]
    }
    },
    methods:{
    }
}
</script>

<style scoped>
#archivePageHolder {
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