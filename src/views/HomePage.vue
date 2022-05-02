<template>
    <div id="HomePageHolder">
        <div>
        <SideNavbar :is-manager="isManager" :user-name="userName"/>
        </div>
        <div id="contentHolder">
        <WelcomeCard :user-name="userName"/>
        <OverallGoalsCard 
        :is-manager="isManager" 
        :user-name="userName" 
        :department="userDepartment"
        :department-goals-data="departmentGoalsData[0]"
        />
        </div>
    </div>
</template>;

<script>
import WelcomeCard from "../components/WelcomeCard.vue"
import OverallGoalsCard from "../components/OverallGoalsCard.vue"
import SideNavbar from "../components/SideNavBar.vue"
import axios from "axios"
import router from "../router"

export default {
    name:"HomePage",
    components:{
        WelcomeCard,
        OverallGoalsCard,
        SideNavbar,
    },
    data(){
        return{
            userData: [],
            departmentGoalsData: [],
            isManager: null,
            userName: "",
            userDepartment: "",
        }
    },
    created(){
        this.getUser()
    },
    methods:{
        checkUser(){
            if(this.userData[0].email !== localStorage.email && !localStorage.accessToken){
                router.push({name: 'home'})
            }
        },
        getDeparment(){
            const that = this;
            const config = {
            method: 'get',
            url: `http://127.0.0.1:8000/api/get-department-goals/${that.userDepartment}/`,
            headers: { }
            };

            axios(config)
            .then(function (response) {
            that.departmentGoalsData.push(response.data)
            console.log(that.departmentGoalsData[0]);
            })
            .catch(function (error) {
            console.log(error);
            });
        },
        getUser(){
            const that = this;
            const config = {
            method: 'get',
            url: `http://127.0.0.1:8000/account/get-account/${localStorage.email}`,
            headers: { }
            };

            axios(config)
            .then(function (response) {
            that.userData.push(response.data)
            console.log(that.userData)
            console.log(response.data);
            that.checkUser()
            that.userName = response.data.name
            that.userDepartment = response.data.department
            that.getDeparment()
            if (response.data.role === "Manager"){
            that.isManager = true
            }
            })
            .catch(function (error) {
            console.log(error);
            });
        },
    },
}
</script>

<style>
#HomePageHolder {
    display: flex;
    background-color: white;
}
#contentHolder{
    display: flex;
    flex-direction: column;
    padding: 18px;
}
</style>