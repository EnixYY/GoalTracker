<template>
    <SignUpForm @sign-up="signUp"/> 
</template>

<script>
import SignUpForm from '../components/SignUpForm.vue'
import router from '../router'

export default {
    name: "SignUp",
    components: {
    SignUpForm,
},
data(){
    return{
        signUpData:[],
    }
},
methods:{
    signUp(name, email, role, department, password){
        const newSignUp = {
            // id: name,
            name: name,
            email: email,
            role: role,
            department: department,
            password: password,
        }
        this.signUpData.push(newSignUp);
        console.log(this.signUpData)
        router.push({name: 'home'})
    }
}
}
</script>

<style>

</style>