<template>
<div>
<TopNavBar />
</div>
<div id="mainHolder">
  <h1>Goäl Träcker</h1>
    <NewLoginForm @login-fn="loginFn"/> 
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
    }
},
methods:{
    loginFn(email, password){
        const login = {
            email: email,
            password: password,
        }
        this.loginData.push(login);

        var data = {
        "email": this.loginData[0].email,
        "password": this.loginData[0].password,
        };

        var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/jwt_api/token/',
        data : data
        };

        axios(config)
        .then(function (response) {
        console.log(response.data.access);
        localStorage.accessToken = response.data.access;
        localStorage.email = email
        router.push({name: 'home'})
        })
        .catch(function (error) {
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