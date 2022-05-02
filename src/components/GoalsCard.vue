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

        }
    },
    props:[
        'goalTitle',
        'percentage',
        'dueDate'
    ],
    methods:{

    }
}
</script>

<style>
.goalcard {
        background-color: turquoise;
        justify-content: center;
        border: 1px solid black;
        border-radius: 10px;
        padding: 10px;
        width: 200px;
        height: 200px;
        margin-top: 80px
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