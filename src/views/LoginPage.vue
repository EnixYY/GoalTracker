<template>
    <NewLoginForm @login-fn="loginFn"/> 
</template>

<script>
import NewLoginForm from '../components/NewLoginForm.vue'
import router from '../router'

export default {
    name: "LoginPage",
    components: {
    NewLoginForm,
},
data(){
    return{
        loginData:[],
    }
},
methods:{
    loginFn(email, password){
        const login = {
            // id: name,
            email: email,
            password: password,
        }
        this.loginData.push(login);
        console.log(this.signUpData)
        router.push({name: 'home'})
    }
}
}
</script>