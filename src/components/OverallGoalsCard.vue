<template>
    <div class="OverallGoalsCard">
        <button>View All</button>
        <h2>{{name}}</h2>
        <h4 v-for="goal in goals" :key="goal">{{goal}} {{percentage}}%</h4>
    </div>
</template>

<script>
export default {
    name:"OverallGoalsCard",
    data(){
        return{
        goals:["Quarterly", "Current Sprint"],
        name: "Lau Yu Yao",
        percentage: 0,
        }
    }
}
</script>

<style>
    .OverallGoalsCard {
        justify-content: center;
        border: 1px solid black;
        }
</style>