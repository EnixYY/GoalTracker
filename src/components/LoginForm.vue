<template>
    <form @submit.prevent="">
        <div>
        <label>Username</label>
        <input type="text">
        </div>
        <div>
        <label>Password</label>
        <input type="text">
        </div>
    </form>
</template>

<script>
export default {
    name:"LoginForm",
    emits:[],
    data(){

    },
}
</script>

<style>

</style>
