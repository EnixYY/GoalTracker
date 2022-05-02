<template>
    <form id="loginForm" @submit.prevent="submitLoginDetails">
        <div class="individual">
        <label>Email</label>
        <input type="email" v-model="email">
        </div>
        <div class="individual">
        <label>Password</label>
        <input type="password" v-model="password">
        </div>
        <div class="individual">
        <button>Login</button>
        </div>
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
        }
    }
}
</script>

<style scoped>
#loginForm{
    display: flex;
    flex-direction: column;
    width: 100vw;
    background-color: turquoise;
    width: 60vw;
    height: 30vh;
    justify-content: center;
    border-radius: 10px;
    margin-left: 150px;
}
.individual{
    display:flex;
    justify-content: center;
    padding: 10px;
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
label{
    font-weight: bold;
    padding-right: 10px;
}
</style>