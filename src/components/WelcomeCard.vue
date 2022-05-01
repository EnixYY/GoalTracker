<template>
    <div class="WelcomeCard">
        <h1>Welcome to Goals Tracker</h1>
        <h2>{{name}}</h2>
    </div>
</template>

<script>
export default {
    name:"WelcomeCard",
    data(){
        return{
        name: "Lau Yu Yao",
        }
    }
}
</script>

<style>
    .WelcomeCard {
        margin-top: 100px;
        border: 1px solid black;
        border-radius: 10px;
        width: 70vw;
        background-color: turquoise;
        }
</style>