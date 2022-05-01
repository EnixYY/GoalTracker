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
            // id: name,
            email: email,
            password: password,
        }
        this.loginData.push(login);
        console.log(this.loginData)
        router.push({name: 'home'})
    }
}
}
</script>

<style scoped>
#mainHolder{
  display: flex;
  flex-direction: column;
}
</style>