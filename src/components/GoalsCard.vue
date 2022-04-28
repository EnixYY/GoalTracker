<template>
    <div class="goalcard">
        <h4>{{goalTitle}}</h4>
        <h4>{{percentage}}%</h4>
        <h4>{{dueDate}}</h4>
        <button>Edit</button>
    </div>
</template>

<script>
export default {
    name:"GoalsCard",
    data(){
        return{
            goalTitle:"Quarterly Story points",
            dueDate:"06 May 2022",
            percentage: 0,
        }
    },
    methods:{

    }
}
</script>

<style>
    .goalcard {
        justify-content: center;
        border: 1px solid black;
        }
</style>