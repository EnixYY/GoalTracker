<template>
    <div>
        <TopNavBar />
        </div>
    <div id="mainHolder">
        <h1>Goäl Träcker</h1>
            <SignUpForm @sign-up="signUp"/> 
    </div>
</template>

<script>
import SignUpForm from '../components/SignUpForm.vue'
import TopNavBar from '../components/TopNavBar.vue'
import router from '../router'

export default {
    name: "SignUp",
    components: {
    SignUpForm,
    TopNavBar
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