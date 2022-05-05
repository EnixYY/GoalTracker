<template>
<div>
<TopNavBar />
</div>
<div id="mainHolder">
  <h1>Goäl Träcker</h1>
    <NewLoginForm @login-fn="loginFn"/>
    <div v-if="isError" id="error">
        <label>Please input the correct email or password!</label>
    </div> 
</div>
</template>

<script>
import NewLoginForm from '../components/NewLoginForm.vue'
import TopNavBar from '../components/TopNavBar.vue'
import axios from 'axios'
import router from '../router'

export default {
    name: "LoginPage",
    components: {
    NewLoginForm,
    TopNavBar,
},
data(){
    return{
        loginData:[],
        isError: false,
    }
},
methods:{
    loginFn(email, password){
        const that = this
        const login = {
            email: email,
            password: password,
        }

        const data = {
        "email": login.email,
        "password": login.password,
        };

        const config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/jwt_api/token/',
        data : data
        };

        axios(config)
        .then(function (response) {
        localStorage.accessToken = response.data.access;
        localStorage.email = email
        that.isError = false
        router.push({name: 'home'})
        })
        .catch(function (error) {
        that.isError = true
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
#error{
    display: flex;
    flex-direction: column;
    width: 100vw;
    background-color: salmon;
    width: 60vw;
    height: 10vh;
    justify-content: center;
    border-radius: 10px;
    margin-left: 150px;
}
</style>