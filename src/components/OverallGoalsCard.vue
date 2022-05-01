<template>
    <div class="OverallGoalsCard">
        <h2>{{name}}</h2>
        <h4 v-for="goal in goals" :key="goal">{{goal}} {{percentage}}%</h4>
                <button @click="viewAll">View All</button>

    </div>
</template>

<script>
import router from "../router"

export default {
    name:"OverallGoalsCard",
    data(){
        return{
        goals:["Quarterly", "Current Sprint"],
        name: "Lau Yu Yao",
        percentage: 0,
        }
    },
    methods:{
        viewAll(){
            router.push({ name: "assignedgoals"})
        }
    }
}
</script>

<style>
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
    color: turquoise;
}
</style>