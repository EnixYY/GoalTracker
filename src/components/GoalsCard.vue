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
        justify-content: center;
        border: 1px solid black;
        }
</style>