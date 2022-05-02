<template>
    <div class="OverallGoalsCard">
        <h2 v-if="isManager === false">{{userName}}</h2>
        <h2 v-if="isManager">{{department}}</h2>
        <div v-if="isManager">
            <h4 v-for="goal in this.departmentGoalsData" :key="goal.id">{{goal.name}} 0/{{goal.value}} Due on {{goal.endDate}}</h4>
            <button @click="viewAll">View All</button>
        </div>
        <div v-if="isManager === false">
            <h4>Not done</h4>
            <button @click="viewAll">View All</button>
        </div>
    </div>
</template>

<script>
import router from "../router"

export default {
    name:"OverallGoalsCard",
    data(){
        return{
        }
    },
    props:[
        "userName",
        "department",
        "isManager",
        "departmentGoalsData"
    ],
    methods:{
        viewAll(){
            router.push({ name: "assignedgoals"})
        }
    }
}
</script>

<style scoped>
.OverallGoalsCard {
        margin-top: 100px;
        padding-bottom: 15px;
        border-radius: 10px;
        width: 70vw;
        background-color: turquoise;
        border: 1px solid black;
}
button{
    width: 80px;
    padding: 6px;
    text-align: center;
    border-radius: 10px;
    background-color: white;
    border: 1px solid black;
    color: black;
}
button:hover{
    color: white;
    background-color: turquoise;
}
</style>