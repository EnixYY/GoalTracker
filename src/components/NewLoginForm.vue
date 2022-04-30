<template>
    <form @submit.prevent="submitLoginDetails">
        <div>
        <label>Email</label>
        <input type="email" v-model="email">
        </div>
        <div>
        <label>Password</label>
        <input type="password" v-model="password">
        </div>
        <button>Login</button>
    </form>
</template>

<script>
export default {
    name:"NewLoginForm",
    emits:["login-fn"],
    data(){
        return{
            email:"",
            password:"",
        }
    },
    methods:{
        submitLoginDetails(){
            this.$emit(
                "login-fn",
                this.email,
                this.password,
            )
            console.log(this.email)
        }
    }
}
</script>

<style>

</style>