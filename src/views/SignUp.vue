<template>
    <div>
        <TopNavBar />
        </div>
    <div id="mainHolder">
        <h1>Goäl Träcker</h1>
            <SignUpForm @sign-up="signUp"/>
    <div v-if="error" id="error">
        <label>{{errorMessage}}</label>
    </div> 
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
        errorMessage: "",
    }
},
methods:{
    signUp(name, email, role, department, password, confirmPassword){
        if(name === ""){
            this.error = true
            this.errorMessage = "Please fill in the name."
        }else if(email === ""){
            this.error = true
            this.errorMessage = "Please fill in the email."
        }else if(role === ""){
            this.error = true
            this.errorMessage = "Please select a role."
        }else if(department === ""){
            this.error = true
            this.errorMessage = "Please select a department."    
        }else if(password === ""){
            this.error = true
            this.errorMessage = "Please fill in the password."    
        }else if(password !== confirmPassword){
            this.error = true
            this.errorMessage = "Please ensure that password and confirm password matches."
        }else{
            this.error = false
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
        return response.data
        })
        .catch(function (error) {
        this.error = true
        console.log(error);
        });
    }
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
#error{
    display: flex;
    flex-direction: column;
    width: 100vw;
    background-color: salmon;
    width: 70vw;
    height: 10vh;
    justify-content: center;
    border-radius: 10px;
    margin-left: 115px;
}
</style>