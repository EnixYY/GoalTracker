<template>
    <div>
        <TopNavBar />
        </div>
    <div id="mainHolder">
        <h1>Goäl Träcker</h1>
            <SignUpForm @sign-up="signUp" :errorChecker="error"/> 
    </div>
</template>

<script>
import SignUpForm from '../components/SignUpForm.vue'
import TopNavBar from '../components/TopNavBar.vue'
import axios from "axios";
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
        error: false,
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

        const data = {
        "email": newSignUp.email,
        "name": newSignUp.name,
        "role": newSignUp.role,
        "department": newSignUp.department,
        "password": newSignUp.password,
        };

        var config = {
        method: 'put',
        url: 'http://127.0.0.1:8000/account/create-account/',
        headers: { 
            'Content-Type': 'application/json'
        },
        data : data
        };

        axios(config)
        .then(function (response) {
        router.push({name: 'login'})
        console.log(response.data);
        })
        .catch(function (error) {
        this.error = true
        console.log(error);
        });
    }
}
}
</script>

<style scoped>
#mainHolder{
  display: flex;
  flex-direction: column;
  margin-top: 60px;
}
</style>