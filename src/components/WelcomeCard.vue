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
        justify-content: center;
        border: 1px solid black;
        width: 75vw;
        }
</style>